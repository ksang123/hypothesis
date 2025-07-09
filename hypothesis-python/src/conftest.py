from hypothesis.internal.unit_tests import UnitTestGenerator
# conftest.py
import sys
import traceback
from hypothesis.strategies import SearchStrategy

def trace_lines(frame, event, arg):
    if event == 'line':
        filename = frame.f_code.co_filename
        lineno = frame.f_lineno
        func_name = frame.f_code.co_name
        print(f"LINE {filename}:{lineno} in {func_name}")
    return trace_lines


def traced_do_draw(self, data):
    """Trace only draw calls and important choices without line-by-line tracing."""
    strategy_name = self.__class__.__name__
    print(f"\n=== DRAW from {strategy_name}: {self} ===", flush=True)

    # Capture the original choose_integer method to monitor choices
    original_choose = getattr(data, "choose_integer", None)

    def traced_choose(self, start, end):
        result = original_choose(self, start, end)
        print(f"  CHOICE: {start} to {end} → {result}", flush=True)
        return result

    # Only patch if the method exists
    if original_choose:
        data.choose_integer = type(data.choose_integer)(traced_choose, data)

    # Call original without line tracing
    result = original_do_draw(self, data)
    print(f"=== END DRAW: {result} ===", flush=True)

    # Restore original choose method if we patched it
    if original_choose:
        data.choose_integer = original_choose

    return result


def pytest_configure(config):
    """Called once at the start of pytest session."""
    global original_do_draw
    original_do_draw = SearchStrategy.do_draw
    SearchStrategy.do_draw = traced_do_draw
    print("Hypothesis draw tracing ENABLED.", flush=True)

def pytest_unconfigure(config):
    """Restore original behavior after session ends."""
    SearchStrategy.do_draw = original_do_draw
    print("Hypothesis draw tracing DISABLED.", flush=True)

# def pytest_runtest_call(item):
#     """Trace the test function itself."""
#     sys.settrace(trace_lines)

def pytest_sessionfinish(session, exitstatus):
    # TODO: maybe pass a path here
    # TODO: maybe find a better place to put this
    UnitTestGenerator().render()