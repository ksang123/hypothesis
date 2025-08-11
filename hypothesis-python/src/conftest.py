# from _typeshed import TraceFunction
from types import FrameType
from typing import Any

from hypothesis.internal.unit_tests import UnitTestGenerator
# conftest.py
import sys
import traceback
from hypothesis.strategies import SearchStrategy
import linecache


flag = False

def shortenName(name: str) -> str:
    """Take only the last 2 subdirectories of a path."""
    parts = name.split('\\')
    if len(parts) > 2:
        return '/'.join(parts[-2:])
    return name


# Add a flag to track if we're inside do_draw execution
inside_do_draw = False


def trace_lines(frame, event, arg):
    global inside_do_draw

    # Check if we're returning from do_draw
    if event == 'return' and frame.f_code.co_name == 'do_draw':
        inside_do_draw = False
        print("Finished tracing do_draw calls")

    # Print line information as before
    code = frame.f_code
    filename = frame.f_code.co_filename
    lineno = frame.f_lineno
    func_name = frame.f_code.co_name
    line = linecache.getline(filename, lineno).strip()
    print(f"{shortenName(filename)}:{func_name}:{lineno}: {line}")

    return trace_lines


def trace_calls(frame: FrameType, event: str, arg: Any):
    global inside_do_draw

    if event != 'call':
        return

    func_name = frame.f_code.co_name

    # Set flag when entering do_draw
    if func_name == "do_draw":
        inside_do_draw = True
        print("Started tracing do_draw calls")
        return trace_lines
    # Trace any function called while inside do_draw
    elif inside_do_draw:
        print(f"Tracing nested call to {func_name}")
        return trace_lines

    return


def pytest_configure(config):
    """Called once at the start of pytest session."""
    # global original_do_draw
    # original_do_draw = SearchStrategy.do_draw
    # SearchStrategy.do_draw = traced_do_draw
    # print("Hypothesis draw tracing ENABLED.", flush=True)

def pytest_unconfigure(config):
    """Restore original behavior after session ends."""
    # SearchStrategy.do_draw = original_do_draw
    # print("Hypothesis draw tracing DISABLED.", flush=True)

def pytest_runtest_call(item):
    """Trace the test function itself."""
    sys.settrace(trace_calls)

def pytest_sessionfinish(session, exitstatus):
    # TODO: maybe pass a path here
    # TODO: maybe find a better place to put this
    UnitTestGenerator().render()

# def traced_do_draw(self, data):
#     """Trace only draw calls and important choices without line-by-line tracing."""
#     strategy_name = self.__class__.__name__
#     print(f"\n=== SHITDRAW from {strategy_name}: {self} ===", flush=True)
#
#     # Capture the original choose_integer method to monitor choices
#     original_choose = getattr(data, "choose_integer", None)
#
#     def traced_choose(self, start, end):
#         result = original_choose(self, start, end)
#         print(f"  CHOICE: {start} to {end} → {result}", flush=True)
#         return result
#
#     # Only patch if the method exists
#     if original_choose:
#         data.choose_integer = type(data.choose_integer)(traced_choose, data)
#
#     # Call original without line tracing
#     result = original_do_draw(self, data)
#     print(f"=== END DRAW: {result} ===", flush=True)
#
#     # Restore original choose method if we patched it
#     if original_choose:
#         data.choose_integer = original_choose
#
#     return result
