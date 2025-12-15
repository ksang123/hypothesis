import linecache

flag = False
captured_values = {
    'draw_result': None,
    'nested_results': {}  # Function name -> return value
}
#
def shortenName(name: str) -> str:
    """Take only the last 2 subdirectories of a path."""
    parts = name.split('\\')
    if len(parts) > 2:
        return '/'.join(parts[-2:])
    return name
#
#
# # Add a flag to track if we're inside do_draw execution
inside_do_draw = False
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


def myLog(s: str) -> None:
    pass
    with open("hypothesis_trace.log", "a") as f:
        print(f"----------------{s}", file=f)

def trace_calls(frame, event, arg):
    global inside_do_draw, captured_values

    # Profile needs to handle both 'call' and 'return' in the same function
    if event == 'call':
        func_name = frame.f_code.co_name
        if func_name == "draw":
            inside_do_draw = True
            myLog(f"Started tracing draw calls")
        elif inside_do_draw:
            myLog(f"Tracing nested call to {func_name}")

    elif event == 'return':
        func_name = frame.f_code.co_name
        if func_name == "draw":
            inside_do_draw = False
            captured_values['draw_result'] = arg
            myLog(f"Captured draw return value: {arg}")
            myLog("Finished tracing draw calls")
        elif inside_do_draw:
            captured_values['nested_results'][func_name] = arg
            myLog(f"Captured nested call to {func_name} with return value: {arg}")
        else:
            pass
            # myLog(f"Unexpected return event for {func_name}")

    # Still print line information if inside_do_draw
    if inside_do_draw and event in ('call', 'return'):
        filename = frame.f_code.co_filename
        lineno = frame.f_lineno
        line = linecache.getline(filename, lineno).strip()
        myLog(f"{shortenName(filename)}:{func_name}:{lineno}: {line}")

    return trace_calls  # Always return self to continue tracing

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
