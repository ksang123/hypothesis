import linecache
from typing import Set, List


# flag = False
#
# def shortenName(name: str) -> str:
#     """Take only the last 2 subdirectories of a path."""
#     parts = name.split('\\')
#     if len(parts) > 3:
#         return '/'.join(parts[-3:])
#     return name
#
#
# # Add a flag to track if we're inside do_draw execution
# inside_do_draw = False
# inside_custom = False
# depth = 0
# custom: Set[str] = {'rb_functional_tree', 'rb_imperative_tree'}
#
#
# def trace_lines(frame, event, arg):
#     global inside_do_draw, captured_values
#
#     # Check if we're returning from do_draw
#     if event == 'return':
#         func_name = frame.f_code.co_name
#         if func_name == "do_draw":
#             inside_do_draw = False
#             # Capture the return value of do_draw
#             captured_values['do_draw_result'] = arg
#             print(f"Captured do_draw return value: {arg}")
#         elif inside_do_draw:
#             # Capture return values of nested calls
#             captured_values['nested_results'][func_name] = arg
#             print(f"Captured nested call to {func_name} with return value: {arg}")
#     # if event == 'return' and frame.f_code.co_name == 'do_draw':
#     #     inside_do_draw = False
#     #     print("Finished tracing do_draw calls")
#
#     # Print line information as before
#     code = frame.f_code
#     filename = frame.f_code.co_filename
#     lineno = frame.f_lineno
#     func_name = frame.f_code.co_name
#     line = linecache.getline(filename, lineno).strip()
#     print(f"{shortenName(filename)}:{func_name}:{lineno}: {line}")
#
#     return trace_lines


# def trace_calls(frame: FrameType, event: str, arg: Any):
#     global inside_do_draw
#
#     if event != 'call':
#         return
#
#     func_name = frame.f_code.co_name
#
#     # Set flag when entering do_draw
#     if func_name == "do_draw":
#         inside_do_draw = True
#         print("Started tracing do_draw calls")
#         return trace_lines
#     # Trace any function called while inside do_draw
#     elif inside_do_draw:
#         print(f"Tracing nested call to {func_name}")
#         return trace_lines
#
#     return


def myLog(s: str, pre = "-----------------") -> None:
    pass
    with open("hypothesis_trace.log", "a") as f:
        print(f"{pre}{s}", file=f)


class DrawResult:
    def __init__(self, st, r = None, c = False, b = None, p = None):
        self.result = r
        # self.composite = c
        self.innerBody: List[DrawResult] = b
        self.parent = p
        self.strategy = st

    def __repr__(self):
        return f"DrawResult(strat={self.strategy}, result={self.result}, innerBody={"\n\t" if self.innerBody else ""}{self.innerBody})"


captured_values: List[DrawResult] = []

recordStarts = False
def open_recording():
    global recordStarts
    recordStarts = True
def close_recording():
    global recordStarts
    recordStarts = False
def add_strat(s):
    if recordStarts:
        strats.append(s)
        # myLog(f"Strats is {strats}", "")

def clear():
    global captured_values
    clearStrats()
    captured_values = []
def clearStrats():
    global strats
    strats = []
    last = None
strats = []

last = None
#     {
#     'draw_result': None,
#     'nested_results': {}  # Function name -> return value
# }


def trace_calls(frame, event, arg):
    global captured_values, last
    # Still print line information if inside_do_draw

    func_name = frame.f_code.co_name
    if event == 'call':
        if func_name == "draw":
            if not last:
                captured_values.append(DrawResult(strats[-1]))
                last = captured_values[-1]
                myLog("==================Made a new draw")
            else:
                myLog("Made a new composite draw")
                if last.innerBody is None:
                    last.innerBody = []
                newOne = DrawResult(strats[-1])
                last.innerBody.append(newOne)
                newOne.parent = last
                last = newOne

        if func_name.startswith("draw_"):
            myLog("Made a new basic draw")
            # last.composite = False
    if event == 'return':
        if func_name == "draw":
            myLog(f"Returned from draw with {arg}")
            if last.parent:
                last.parent.result = "<This will swapped out>" #last.innerBody
            if not last.innerBody:
                last.result = arg
            else:
                last.result = None
            last = last.parent
            if last is None:
                myLog("===================Not composite")
            myLog(f"Now the list is {"\n".join(map(lambda x: f"{x}", captured_values))}")
            # myLog(f"Now the strats are {strats}")


draw_log = []

def instrument_hypothesis():
    from hypothesis.internal.conjecture.data import ConjectureData, Status
    from hypothesis.internal.conjecture.engine import ConjectureRunner

    # Add tracking attributes to ConjectureData
    original_init = ConjectureData.__init__

    def instrumented_init(self, *args, **kwargs):
        original_init(self, *args, **kwargs)
        # self.draw_log = []
        if not hasattr(self, 'arg_slices'):
            self.arg_slices = set()
        if not hasattr(self, 'slice_comments'):
            self.slice_comments = {}

    ConjectureData.__init__ = instrumented_init

    # Instrument the draw method
    original_draw = ConjectureData.draw

    def instrumented_draw(self, strategy, label=None, observe_as=None):
        # Track draw index
        draw_index = len(self.nodes)
        add_strat(strategy)
        # Call original
        result = original_draw(self, strategy, label, observe_as)

        # Log the draw
        draw_log.append({
            "index": draw_index,
            "strategy": strategy,
            "result": result
        })

        # If this is an interesting (failing) example, show draws
        if hasattr(self, 'status') and self.status == Status.INTERESTING:
            in_failing_arg = False
            arg_name = "unknown"

            # Check if this draw is part of a failing argument slice
            if hasattr(self, 'arg_slices'):
                for start_idx, end_idx in self.arg_slices:
                    if start_idx <= draw_index < end_idx:
                        in_failing_arg = True
                        arg_name = self.slice_comments.get((start_idx, end_idx), "unknown arg")
                        break

            print(f"Draw #{draw_index} contributed to failure:")
            print(f"  Strategy: {strategy}")
            print(f"  Value: {result}")
            if in_failing_arg:
                print(f"  Part of failing argument: {arg_name}")

        return result

    ConjectureData.draw = instrumented_draw

    # Hook into test execution
    original_run = ConjectureRunner.run

    def instrumented_run(self, *args, **kwargs):
        result = original_run(self, *args, **kwargs)

        # After run completes, check if we found interesting examples
        if hasattr(self, 'interesting_examples') and self.interesting_examples:
            print(f"\n{'=' * 30} DRAWS THAT LED TO FAILING TEST {'=' * 30}")
            for key, example in self.interesting_examples.items():
                print(f"Failing example key: {key}")

                # Access buffer correctly - try different attributes
                if hasattr(example, 'buffer'):
                    print(f"  Buffer: {example.buffer.hex() if hasattr(example.buffer, 'hex') else example.buffer}")

                # Print arg_slices if available
                if hasattr(example, 'arg_slices') and example.arg_slices:
                    print("  Argument slices:")
                    for start_idx, end_idx in example.arg_slices:
                        arg_name = example.slice_comments.get((start_idx, end_idx), "unknown")
                        print(f"    {arg_name}: draws {start_idx} to {end_idx}")

                # Print all logged draws
                if True:  # hasattr(example, 'draw_log') and example.draw_log:
                    print("  Draw log:")
                    for entry in draw_log:
                        print(f"    Draw #{entry['index']}: {entry['result']} from {entry['strategy']}")
                print("=" * 30)
        return result

    ConjectureRunner.run = instrumented_run
