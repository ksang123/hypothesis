import linecache

flag = False
captured_values = {
    'do_draw_result': None,
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

def trace_calls(frame, event, arg):
    global inside_do_draw, captured_values

    # Profile needs to handle both 'call' and 'return' in the same function
    if event == 'call':
        func_name = frame.f_code.co_name
        if func_name == "do_draw":
            inside_do_draw = True
            print("Started tracing do_draw calls")
        elif inside_do_draw:
            print(f"Tracing nested call to {func_name}")

    elif event == 'return':
        func_name = frame.f_code.co_name
        if func_name == "do_draw":
            inside_do_draw = False
            captured_values['do_draw_result'] = arg
            # print(f"Captured do_draw return value: {arg}")
        elif inside_do_draw:
            captured_values['nested_results'][func_name] = arg
            # print(f"Captured nested call to {func_name} with return value: {arg}")

    # Still print line information if inside_do_draw
    if inside_do_draw and event in ('call', 'return'):
        filename = frame.f_code.co_filename
        lineno = frame.f_lineno
        line = linecache.getline(filename, lineno).strip()
        print(f"{shortenName(filename)}:{func_name}:{lineno}: {line}")

    return trace_calls  # Always return self to continue tracing
