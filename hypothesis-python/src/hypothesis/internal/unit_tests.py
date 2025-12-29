import os
from collections import defaultdict

from ..strategies._internal.core import CompositeStrategy
from ..control import BuildContext
from .conjecture.data import ConjectureData
from pathlib import Path
import inspect
import ast

from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[2]))
from tracing import trace_calls, captured_values, open_recording, close_recording


class UnitTestGenerator:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if self._initialized:
            return
        self._COPY_CODE = False
        self._KEEP_FUNCS = False
        self._PRINT_SOURCE = False
        self._tests = {}
        self._initialized = True
        script_path = Path(__file__).resolve()
        src_path = script_path.parents[2]
        self.output_file = f"{src_path}/failing_test.py"

    def add_test(self, test_name, test_info, of):
        self.output_file = of
        self._tests[test_name] = test_info

    def _extract_source_code(self, func):
        """Extract the source code of a function without decorators."""
        try:
            source_lines, _ = inspect.getsourcelines(func)
            # Skip decorator lines (starting with @)
            function_lines = []
            for line in source_lines:
                if not line.strip().startswith('@'):
                    function_lines.append(line)
            return "".join(function_lines)
        except (OSError, TypeError):
            return None

    def _collect_types(self, value, seen):
        if id(value) in seen:
            return
        seen.add(id(value))
        if isinstance(value, (list, tuple, set, frozenset)):
            for item in value:
                yield from self._collect_types(item, seen)
        elif isinstance(value, dict):
            for k, v in value.items():
                yield from self._collect_types(k, seen)
                yield from self._collect_types(v, seen)
        else:
            cls = value.__class__
            if cls.__module__ != "builtins":
                yield cls.__module__, cls.__name__

    def _eval_strategies(self, given_kwargs, choices):
        data = ConjectureData.for_choices(choices)
        values = {}
        draws = {}
        with BuildContext(data) as ctx:
            with open("hypothesis_trace.log", "a") as f:
                print("=" * 50, file=f)
            open_recording()
            sys.setprofile(trace_calls)
            for name, strat in given_kwargs.items():
                st = strat._LazyStrategy__wrapped_strategy
                if isinstance(st, CompositeStrategy):
                    local = []

                    def dr(s):
                        v = ctx.data.draw(s)
                        local.append(v)
                        return v

                    values[name] = st.definition(dr, *st.args, **st.kwargs)
                    draws[name] = local
                else:
                    values[name] = ctx.data.draw(st)
                    draws[name] = [values[name]]
            sys.setprofile(None)
        return values, draws

    class _Prefixer(ast.NodeTransformer):
        def __init__(self, mapping):
            super().__init__()
            self.mapping = mapping

        def visit_Name(self, node):
            if node.id in self.mapping:
                return ast.copy_location(ast.Name(id=self.mapping[node.id], ctx=node.ctx), node)
            return node

    class _DrawReplacer(ast.NodeTransformer):
        def __init__(self, draws):
            super().__init__()
            self.draws = draws
            self.idx = 0

        def visit_Call(self, node):
            if (
                isinstance(node.func, ast.Name)
                and node.func.id == "draw"
                and self.idx < len(self.draws)
            ):
                if self.draws[self.idx].result is not None:
                    val = self.draws[self.idx].result # Todo: swap recursively but not inside function
                else:
                    val = ast.Call(func=ast.Name(id=f"Some random shit"), args=[], keywords=[])
                    self.idx += 1
                    return val
                    # val = f"Need to copy {name} into here and call it with {args}"#self.draws[self.idx]
                self.idx += 1
                return ast.copy_location(ast.Constant(value=val), node)
            return self.generic_visit(node)


    def swap(self, stmt, prefix, var_name, mapping, lines, indent=1):
        indent_str = "\t" * indent

        # Keep names replaced
        if isinstance(stmt, ast.Assign) and len(stmt.targets) == 1 and isinstance(stmt.targets[0], ast.Name):
            orig = stmt.targets[0].id
            new_name = prefix + orig
            mapping[orig] = new_name
            value = self._Prefixer(mapping).visit(stmt.value)
            src = ast.unparse(value)
            for l in src.split("\n"):
                lines.append(f"{indent_str}{new_name} = {l}")
            return

        # Treat return uniformly no matter where it appears
        if isinstance(stmt, ast.Return):
            value = self._Prefixer(mapping).visit(stmt.value) if stmt.value is not None else ast.Constant(value=None)
            src = ast.unparse(value)
            for l in src.split("\n"):
                lines.append(f"{indent_str}{var_name} = {l}")
            return

        # Recurse into blocks (if/for/while/with) so inner returns are handled the same
        if isinstance(stmt, ast.If):
            test = self._Prefixer(mapping).visit(stmt.test)
            lines.append(f"{indent_str}if {ast.unparse(test)}:")
            for s in stmt.body:
                self.swap(s, prefix, var_name, mapping, lines, indent + 1)
            if stmt.orelse:
                lines.append(f"{indent_str}else:")
                for s in stmt.orelse:
                    self.swap(s, prefix, var_name, mapping, lines, indent + 1)
            return

        if isinstance(stmt, (ast.For, ast.While)):
            node = stmt
            # Prefix target and iter/test
            node = self._Prefixer(mapping).visit(node)
            header = ast.unparse(node).split(":", 1)[0] + ":"
            lines.append(f"{indent_str}{header}")
            body = node.body
            orelse = node.orelse
            for s in body:
                self.swap(s, prefix, var_name, mapping, lines, indent + 1)
            if orelse:
                lines.append(f"{indent_str}else:")
                for s in orelse:
                    self.swap(s, prefix, var_name, mapping, lines, indent + 1)
            return

        if isinstance(stmt, ast.With):
            node = self._Prefixer(mapping).visit(stmt)
            header = ast.unparse(node).split(":", 1)[0] + ":"
            lines.append(f"{indent_str}{header}")
            for s in node.body:
                self.swap(s, prefix, var_name, mapping, lines, indent + 1)
            return

        # Fallback: apply prefixer and unparse, preserving indentation for multi-line output
        value = self._Prefixer(mapping).visit(stmt)
        for l in ast.unparse(value).split("\n"):
            lines.append(f"{indent_str}{l}")

    def _render_strategy_lines(self, df, draws, var_name):
        source = self._extract_source_code(df)
        tree = ast.parse(source)
        body = tree.body[0].body
        prefix = f"{var_name}_"
        mapping = {}
        lines = []
        replacer = self._DrawReplacer(draws)
        for stmt in body:
            stmt = replacer.visit(stmt)
            self.swap(stmt, prefix, var_name, mapping, lines)
        return lines

    def _generate_test_body(self, test_name, test):


        lines = []
        filename = os.path.basename(test["filename"])
        lineno = test.get("lineno")
        lines.append(f"# Failure occurred in: {filename}")
        if lineno:
            lines.append(f"# Line number: {lineno}")
        lines.append(f"def test_run_failing_test_{test_name}():")
        given_kwargs = test.get("given_kwargs", {})
        values, draws = self._eval_strategies(given_kwargs, test.get("choices", []))

        if self._PRINT_SOURCE:
            lines.append('\t"""')
            for var_name, strat in given_kwargs.items():
                lines.append(f"\t{var_name}:")
                st = strat._LazyStrategy__wrapped_strategy  # private? nah
                if isinstance(st, CompositeStrategy):
                    df = st.definition
                    lines.append("STRATEGY CODE:")
                    lines.append(strip_leading_indent_after_first_line(self._extract_source_code(df)))
                else:
                    # For built-in strategies we only show the strategy name
                    name = repr(strat)
                    if "(" in name:
                        name = name.split("(")[0] + "()"
                    value = values.get(var_name)
                    lines.append(f"\t{name} -> {value!r}")
            lines.append('\t"""')

        for var_name, strat in given_kwargs.items():
            st = strat._LazyStrategy__wrapped_strategy  # private? nah
            if isinstance(st, CompositeStrategy):
                for default in zip(ast.parse(self._extract_source_code(st.definition)).body[0].args.args[1:], st.args):
                    lines.append(f"\t{default[0].arg}={default[1]}")
                lines.extend(self._render_strategy_lines(st.definition, captured_values, var_name))
            else:
                lines.append(f"\t{var_name} = {values[var_name]!r}")

        if self._COPY_CODE:
            lines.append(f"\t{test['func_name']}(")
        else:
            lines.append(f"\t{test['func_name']}.hypothesis.inner_test(")
        for arg in test["args"]:
            lines.append(f"        {arg!r},")
        for k, v in test["kwargs"].items():
            if k in given_kwargs:
                lines.append(f"\t\t{k}={k},")
            else:
                lines.append(f"\t\t{k}={v!r},")
        lines.append("\t)")
        with open("hypothesis_trace.log", "a") as f:
            print("=" * 50, file=f)
        close_recording()
        return "\n".join(lines) + "\n"

    def render(self) -> None:
        output_file = self.output_file

        existing_imports = defaultdict(set)
        existing_funcs = {}
        if os.path.exists(output_file) and self._KEEP_FUNCS:
            try:
                with open(output_file, "r", encoding="utf-8") as f:
                    source = f.read()

                tree = ast.parse(source)
                for node in tree.body:
                    if isinstance(node, ast.ImportFrom) and node.module:
                        for alias in node.names:
                            existing_imports[node.module].add(alias.name)
                    elif isinstance(node, ast.FunctionDef):
                        name = node.name
                        start, end = node.lineno - 1, node.end_lineno
                        func_src = "\n".join(source.splitlines()[start:end])
                        existing_funcs[name] = func_src
            except Exception:
                print("failed to keep tests :(")

        module_to_names = defaultdict(set)
        new_funcs = {}
        for test_name, test in self._tests.items():
            if not self._COPY_CODE:
                module_to_names[test["module"]].add(test["func_name"])
            elif self._KEEP_FUNCS:
                existing_imports[test["module"]].discard(test["func_name"])
            seen = set()
            for arg in list(test["args"]) + list(test["kwargs"].values()):
                for mod, cls in self._collect_types(arg, seen):
                    module_to_names[mod].add(cls)

            # Only add the original test function if copy_code is True
            if self._COPY_CODE and "test_func" in test:
                source_code = self._extract_source_code(test["test_func"])
                if source_code:
                    # Add the original test function
                    new_funcs[test_name] = source_code

            func_code = self._generate_test_body(test_name, test)
            new_funcs[f"test_run_failing_test_{test_name}"] = func_code

        if self._KEEP_FUNCS:
            for mod, names in existing_imports.items():
                if names:
                    module_to_names[mod].update(names)

        final_funcs = existing_funcs if self._KEEP_FUNCS else {}
        final_funcs.update(new_funcs)

        with open(output_file, "w", encoding="utf-8") as f:
            f.write("# Failing tests extracted from Hypothesis\n\n")

            for module, names in sorted(module_to_names.items()):
                if not names:
                    continue
                f.write(f"from {module} import (\n")
                for name in sorted(names):
                    f.write(f"    {name},\n")
                f.write(")\n\n")

            for name, code in final_funcs.items():
                f.write(code.rstrip() + "\n\n")

        print(f"[unit-test-generator] Wrote {len(new_funcs)} test(s) to {output_file}")


def strip_leading_indent_after_first_line(source: str) -> str:
    first, _, rest = source.partition("\n")
    if not rest:
        return ''

    lines = rest.splitlines()
    first_line_indent = len(lines[0]) - len(lines[0].lstrip())

    return "\n".join(line[first_line_indent:] if len(line) >= first_line_indent else line for line in lines)


# def save_failing_test_info(self, data: ConjectureResult, output_file: str = None) -> None:
#     """Save complete information needed to reproduce a failing test."""
#     import os.path
#     from ...control import BuildContext
#     from ...vendor.pretty import RepresentationPrinter
#
#     # Get test function details
#     state = self._test_function.__self__
#     tmp = ConjectureData.for_choices(data.choices)
#     test_func = state.test  # The actual test function
#
#     # Get the failing file path and directory
#     if hasattr(self.tree.root.transition, 'interesting_origin'):
#         source_filename = self.tree.root.transition.interesting_origin.filename
#         source_dir = os.path.dirname(source_filename)
#         module_name = os.path.basename(source_filename)
#         if module_name.endswith('.py'):
#             module_name = module_name[:-3]
#
#         # Set the output file to be in the same directory
#         if output_file is None:
#             output_file = os.path.join(source_dir, "failing_test.py")
#     else:
#         print("Probably a State machine")
#         return
#
#     with open(output_file, "a") as f:
#         # Simple header
#         f.write("# Failing test extracted from Hypothesis\n\n")
#
#         # Save the failure location as a comment
#         f.write(f"# Failure occurred in: {os.path.basename(source_filename)}\n")
#         if hasattr(self.tree.root.transition.interesting_origin, 'lineno'):
#             f.write(f"# Line number: {self.tree.root.transition.interesting_origin.lineno}\n\n")
#
#         # Save the direct values for reproduction
#         f.write("# Test reproduction with exact failing values:\n")
#
#         # Create the function call with exact values
#         with BuildContext(tmp) as ctx:
#             args = state.stuff.args
#             kwargs = dict(state.stuff.kwargs)
#             kw, arg_slices = ctx.prep_args_kwargs_from_strategies(state.stuff.given_kwargs)
#             kwargs.update(kw)
#
#             # Write a function that calls the test with exact values
#             f.write(f"def test_run_failing_test_{test_func.__name__}():\n")
#
#             # Simple import statement without path
#             f.write(f"    from {module_name} import {test_func.__name__}\n\n")
#
#             # Create the function call representation
#             printer = RepresentationPrinter(context=ctx)
#             printer.repr_call(
#                 f"{test_func.__name__}.hypothesis.inner_test", # access the actual internal function
#                 args,
#                 kwargs,
#                 force_split=True,
#                 arg_slices=arg_slices,
#             )
#
#             # Format and write the actual call with proper indentation
#             call_str = printer.getvalue().replace("Trying example: ", "")
#             # Ensure proper indentation for all lines
#             indented_call = "\n".join(("    " + line) if line.strip() else line
#                                       for line in call_str.splitlines())
#             f.write(f"{indented_call}\n\n")
#
#     print(f"Saved clean failing test to {output_file}")
