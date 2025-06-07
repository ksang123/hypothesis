import os
from collections import defaultdict
from ..vendor.pretty import RepresentationPrinter

class UnitTestGenerator:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(UnitTestGenerator, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if self._initialized:
            return
        self._tests = {}
        self._initialized = True

    def add_test(self, test_name, test_info):
        self._tests[test_name] = test_info

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

    def _generate_test_body(self, test_name, test):
        lines = []
        filename = os.path.basename(test["filename"])
        lineno = test.get("lineno")
        lines.append(f"# Failure occurred in: {filename}")
        if lineno:
            lines.append(f"# Line number: {lineno}")
        lines.append(f"def test_run_failing_test_{test_name}():")
        lines.append(f"    {test['func_name']}.hypothesis.inner_test(")

        printer = RepresentationPrinter(context=test["context"])
        printer.repr_call(
            f"{test['func_name']}.hypothesis.inner_test",
            test["args"],
            test["kwargs"],
            force_split=True,
            arg_slices=test["arg_slices"],
        )
        call_lines = printer.getvalue().replace("Trying example: ", "").splitlines()
        for line in call_lines[1:]:
            lines.append("    " + line)
        return "\n".join(lines) + "\n"

    def render(self) -> None:
        output_file = "failing_test.py"  # TODO: we might wanna improve this

        existing_imports = defaultdict(set)
        existing_funcs = {}
        if os.path.exists(output_file):
            import ast

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

        module_to_names = defaultdict(set)
        new_funcs = {}
        for test_name, test in self._tests.items():
            module_to_names[test["module"]].add(test["func_name"])
            seen = set()
            for arg in list(test["args"]) + list(test["kwargs"].values()):
                for mod, cls in self._collect_types(arg, seen):
                    module_to_names[mod].add(cls)

            func_code = self._generate_test_body(test_name, test)
            new_funcs[f"test_run_failing_test_{test_name}"] = func_code

        for mod, names in existing_imports.items():
            module_to_names[mod].update(names)

        final_funcs = existing_funcs
        final_funcs.update(new_funcs)

        with open(output_file, "w", encoding="utf-8") as f:
            f.write("# Failing tests extracted from Hypothesis\n\n")

            for module, names in sorted(module_to_names.items()):
                f.write(f"from {module} import (\n")
                for name in sorted(names):
                    f.write(f"    {name},\n")
                f.write(")\n\n")

            for name, code in final_funcs.items():
                f.write(code.rstrip() + "\n\n")

        print(f"[unit-test-generator] Wrote {len(new_funcs)} test(s) to {output_file}")


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