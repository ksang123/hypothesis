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

    def parse_existing_test_file(self, output_file: str):
        raise NotImplementedError()

    def render(self) -> None:
        output_file = "failing_test.py" # TODO: improve this
        # self.parse_existing_test_file(output_file)

        with open(output_file, "w", encoding="utf-8") as f:
            f.write("# Failing tests extracted from Hypothesis\n\n")

            # --- Header: unique imports ---
            module_to_funcs = defaultdict(list)
            for test in self._tests.values():
                module_to_funcs[test["module"]].append(test["func_name"])

            for module, funcs in sorted(module_to_funcs.items()):
                f.write(f"from {module} import (\n")
                for func in sorted(set(funcs)):
                    f.write(f"    {func},\n")
                f.write(")\n\n")

            # --- Body: test functions ---
            for test_name, test in self._tests.items():
                filename = os.path.basename(test["filename"])
                lineno = test.get("lineno")

                # Metadata comments
                f.write(f"# Failure occurred in: {filename}\n")
                if lineno:
                    f.write(f"# Line number: {lineno}\n")

                f.write(f"def test_run_failing_test_{test_name}():\n")

                f.write(f"    {test['func_name']}.hypothesis.inner_test(\n")

                # Format the call with printer for nice formatting
                printer = RepresentationPrinter(context=test["context"])
                printer.repr_call(
                    f"{test['func_name']}.hypothesis.inner_test",
                    test["args"],
                    test["kwargs"],
                    force_split=True,
                    arg_slices=test["arg_slices"],
                )
                call_lines = printer.getvalue().replace("Trying example: ", "").splitlines()
                for line in call_lines[1:]:  # skip the first line (function name)
                    f.write("    " + line + "\n")

                f.write("\n\n")

        print(f"[unit-test-generator] Wrote {len(self._tests)} test(s) to {output_file}")


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
#     with open(output_file, "a") as f: # TODO: idk if we wanna append or erase it
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