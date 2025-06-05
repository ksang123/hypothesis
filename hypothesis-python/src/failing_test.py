# Failing test extracted from Hypothesis

# Failure occurred in: C:\Users\danir\PycharmProjects\hypothesis\hypothesis-python\src\test_bank.py
# Line number: 88

# Original test function implementation:
def test_002_subtraction_commutative(x, y):
    assert x - y == y - x

# Test reproduction with exact failing values:
def test_run_failing_test_test_002_subtraction_commutative():
    test_002_subtraction_commutative(
        x=0,
        y=1,
    )

# Failing test extracted from Hypothesis

# Failure occurred in: C:\Users\danir\PycharmProjects\hypothesis\hypothesis-python\src\test_bank.py
# Line number: 126

# Original test function implementation:
def test_030_add_one_greater(x):
    assume(not math.isinf(x))
    assert x + 1 > x

# Test reproduction with exact failing values:
def test_run_failing_test_test_030_add_one_greater():
    test_030_add_one_greater(
        x=9744221326946804.0,
    )

# Failing test extracted from Hypothesis

# Failure occurred in: C:\Users\danir\PycharmProjects\hypothesis\hypothesis-python\src\test_bank.py
# Line number: 140

# Original test function implementation:
def test_005_upper_is_lower(s):
    assert s.upper().islower()

# Test reproduction with exact failing values:
def test_run_failing_test_test_005_upper_is_lower():
    test_005_upper_is_lower(
        s='',
    )

# Failing test extracted from Hypothesis

# Failure occurred in: C:\Users\danir\PycharmProjects\hypothesis\hypothesis-python\src\test_bank.py
# Line number: 159

# Original test function implementation:
def test_032_string_is_upper(s):
    assert s.isupper()

# Test reproduction with exact failing values:
def test_run_failing_test_test_032_string_is_upper():
    test_032_string_is_upper(
        s='',
    )

# Failing test extracted from Hypothesis

# Failure occurred in: C:\Users\danir\PycharmProjects\hypothesis\hypothesis-python\src\test_bank.py
# Line number: 170

# Original test function implementation:
def test_034_ascii_only(s):
    assert all(ord(c) < 128 for c in s)

# Test reproduction with exact failing values:
def test_run_failing_test_test_034_ascii_only():
    test_034_ascii_only(
        s='\x80',
    )

# Failing test extracted from Hypothesis

# Failure occurred in: C:\Users\danir\PycharmProjects\hypothesis\hypothesis-python\src\test_bank.py
# Line number: 195

# Original test function implementation:
def test_009_sort_is_identity(lst):
    assert sorted(lst) == lst

# Test reproduction with exact failing values:
def test_run_failing_test_test_009_sort_is_identity():
    test_009_sort_is_identity(
        lst=[0, -1],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: C:\Users\danir\PycharmProjects\hypothesis\hypothesis-python\src\test_bank.py
# Line number: 206

# Original test function implementation:
def test_037_list_unique(lst):
    assert len(lst) == len(set(lst))

# Test reproduction with exact failing values:
def test_run_failing_test_test_037_list_unique():
    test_037_list_unique(
        lst=[0, 0],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: C:\Users\danir\PycharmProjects\hypothesis\hypothesis-python\src\test_bank.py
# Line number: 222

# Original test function implementation:
def test_040_list_always_empty(lst):
    assert len(lst) == 0

# Test reproduction with exact failing values:
def test_run_failing_test_test_040_list_always_empty():
    test_040_list_always_empty(
        lst=[0],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: C:\Users\danir\PycharmProjects\hypothesis\hypothesis-python\src\test_bank.py
# Line number: 230

# Original test function implementation:
def test_010_keys_values_equal(d):
    assert set(d.keys()) == set(d.values())

# Test reproduction with exact failing values:
def test_run_failing_test_test_010_keys_values_equal():
    test_010_keys_values_equal(
        d={'': 0},
    )

# Failing test extracted from Hypothesis

# Failure occurred in: C:\Users\danir\PycharmProjects\hypothesis\hypothesis-python\src\test_bank.py
# Line number: 254

# Original test function implementation:
def test_042_dict_values_unique(d):
    assert len(d.values()) == len(set(d.values()))

# Test reproduction with exact failing values:
def test_run_failing_test_test_042_dict_values_unique():
    test_042_dict_values_unique(
        d={'': 0, '0': 0},
    )

# Failing test extracted from Hypothesis

# Failure occurred in: C:\Users\danir\PycharmProjects\hypothesis\hypothesis-python\src\test_bank.py
# Line number: 265

# Original test function implementation:
def test_044_set_difference_empty(a, b):
    assert a - b == set()

# Test reproduction with exact failing values:
def test_run_failing_test_test_044_set_difference_empty():
    test_044_set_difference_empty(
        a={0},
        b=set(),
    )

# Failing test extracted from Hypothesis

# Failure occurred in: C:\Users\danir\PycharmProjects\hypothesis\hypothesis-python\src\test_bank.py
# Line number: 331

# Original test function implementation:
def test_017_dummy_inequality(obj):
    assert obj != obj

# Test reproduction with exact failing values:
def test_run_failing_test_test_017_dummy_inequality():
    test_017_dummy_inequality(
        obj=Dummy(0),
    )

# Failing test extracted from Hypothesis

# Failure occurred in: C:\Users\danir\PycharmProjects\hypothesis\hypothesis-python\src\test_bank.py
# Line number: 356

# Original test function implementation:
def test_053_point_x_positive(p):
    assert p.x > 0

# Test reproduction with exact failing values:
def test_run_failing_test_test_053_point_x_positive():
    test_053_point_x_positive(
        p=Point(0, 0),
    )

# Failing test extracted from Hypothesis

# Failure occurred in: C:\Users\danir\PycharmProjects\hypothesis\hypothesis-python\src\test_bank.py
# Line number: 500

# Original test function implementation:
def test_068_fail_on_42(x):
    assert x != 42

# Test reproduction with exact failing values:
def test_run_failing_test_test_068_fail_on_42():
    test_068_fail_on_42(
        x=42,
    )

# Failing test extracted from Hypothesis

# Failure occurred in: C:\Users\danir\PycharmProjects\hypothesis\hypothesis-python\src\test_bank.py
# Line number: 506

# Original test function implementation:
def test_069_fail_on_drawn(data):
    x = data.draw(st.integers())
    assert x != 0

# Test reproduction with exact failing values:
def test_run_failing_test_test_069_fail_on_drawn():
    test_069_fail_on_drawn(
        data=data(...),
    )

# Failing test extracted from Hypothesis

# Failure occurred in: C:\Users\danir\PycharmProjects\hypothesis\hypothesis-python\src\test_bank.py
# Line number: 512

# Original test function implementation:
def test_070_fail_on_empty(lst):
    assume(len(lst) == 0)
    assert False

# Test reproduction with exact failing values:
def test_run_failing_test_test_070_fail_on_empty():
    test_070_fail_on_empty(
        lst=[],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: C:\Users\danir\PycharmProjects\hypothesis\hypothesis-python\src\test_bank.py
# Line number: 526

# Original test function implementation:
def test_072_permutations(lst):
    from itertools import permutations

    perms = list(permutations(lst))
    assert lst in perms

# Test reproduction with exact failing values:
def test_run_failing_test_test_072_permutations():
    test_072_permutations(
        lst=[0, 0, 0],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: C:\Users\danir\PycharmProjects\hypothesis\hypothesis-python\src\test_bank.py
# Line number: 534

# Original test function implementation:
def test_073_permutation_fail(lst):
    from itertools import permutations

    perms = list(permutations(lst))
    assert [0, 0, 0] in perms

# Test reproduction with exact failing values:
def test_run_failing_test_test_073_permutation_fail():
    test_073_permutation_fail(
        lst=[0, 0, 0],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: C:\Users\danir\PycharmProjects\hypothesis\hypothesis-python\src\test_bank.py
# Line number: 548

# Original test function implementation:
def test_075_bytes_fail(b):
    assert b == b"abc"

# Test reproduction with exact failing values:
def test_run_failing_test_test_075_bytes_fail():
    test_075_bytes_fail(
        b=b'',
    )

# Failing test extracted from Hypothesis

# Failure occurred in: C:\Users\danir\PycharmProjects\hypothesis\hypothesis-python\src\test_bank.py
# Line number: 563

# Original test function implementation:
def test_078_booleans_fail(x):
    assert x is True

# Test reproduction with exact failing values:
def test_run_failing_test_test_078_booleans_fail():
    test_078_booleans_fail(
        x=False,
    )

# Failing test extracted from Hypothesis

# Failure occurred in: C:\Users\danir\PycharmProjects\hypothesis\hypothesis-python\src\test_bank.py
# Line number: 574

# Original test function implementation:
def test_080_list_just_one_fail(lst):
    assert all(x == 2 for x in lst)

# Test reproduction with exact failing values:
def test_run_failing_test_test_080_list_just_one_fail():
    test_080_list_just_one_fail(
        lst=[1],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: C:\Users\danir\PycharmProjects\hypothesis\hypothesis-python\src\test_bank.py
# Line number: 584

# Original test function implementation:
def test_082_unicode_fail(s):
    assert s == "abc"

# Test reproduction with exact failing values:
def test_run_failing_test_test_082_unicode_fail():
    test_082_unicode_fail(
        s='',
    )

# Failing test extracted from Hypothesis

# Failure occurred in: C:\Users\danir\PycharmProjects\hypothesis\hypothesis-python\src\test_bank.py
# Line number: 594

# Original test function implementation:
def test_084_floats_fail(lst):
    assert all(x == 0.0 for x in lst)

# Test reproduction with exact failing values:
def test_run_failing_test_test_084_floats_fail():
    test_084_floats_fail(
        lst=[1.0],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: C:\Users\danir\PycharmProjects\hypothesis\hypothesis-python\src\test_bank.py
# Line number: 604

# Original test function implementation:
def test_086_dict_keys_fail(d):
    assert all(k == 0 for k in d.keys())

# Test reproduction with exact failing values:
def test_run_failing_test_test_086_dict_keys_fail():
    test_086_dict_keys_fail(
        d={1: ''},
    )

# Failing test extracted from Hypothesis

# Failure occurred in: C:\Users\danir\PycharmProjects\hypothesis\hypothesis-python\src\test_bank.py
# Line number: 615

# Original test function implementation:
def test_088_list_of_lists_fail(lst):
    assert all(x == [] for x in lst)

# Test reproduction with exact failing values:
def test_run_failing_test_test_088_list_of_lists_fail():
    test_088_list_of_lists_fail(
        lst=[[0]],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: C:\Users\danir\PycharmProjects\hypothesis\hypothesis-python\src\test_bank.py
# Line number: 625

# Original test function implementation:
def test_090_tuple_fail(t):
    assert t == (0, "", 0.0)

# Test reproduction with exact failing values:
def test_run_failing_test_test_090_tuple_fail():
    test_090_tuple_fail(
        t=(0, '', 1.0),
    )

# Failing test extracted from Hypothesis

# Failure occurred in: C:\Users\danir\PycharmProjects\hypothesis\hypothesis-python\src\test_bank.py
# Line number: 630

# Original test function implementation:
def test_108_point_origin(obj):
    assert obj.x == 0 and obj.y == 0

# Test reproduction with exact failing values:
def test_run_failing_test_test_108_point_origin():
    test_108_point_origin(
        obj=Point(0, 1),
    )

# Failing test extracted from Hypothesis

# Failure occurred in: C:\Users\danir\PycharmProjects\hypothesis\hypothesis-python\src\test_bank.py
# Line number: 766

# Original test function implementation:
    def run_state_machine(factory, data):
        cd = data.conjecture_data
        machine = factory()
        check_type(RuleBasedStateMachine, machine, "state_machine_factory()")
        cd.hypothesis_runner = machine
        machine._observability_predicates = cd._observability_predicates  # alias

        print_steps = (
            current_build_context().is_final or current_verbosity() >= Verbosity.debug
        )
        cd._stateful_repr_parts = []

        def output(s):
            if print_steps:
                report(s)
            if TESTCASE_CALLBACKS:
                cd._stateful_repr_parts.append(s)

        try:
            output(f"state = {machine.__class__.__name__}()")
            machine.check_invariants(settings, output, cd._stateful_run_times)
            max_steps = settings.stateful_step_count
            steps_run = 0

            while True:
                # We basically always want to run the maximum number of steps,
                # but need to leave a small probability of terminating early
                # in order to allow for reducing the number of steps once we
                # find a failing test case, so we stop with probability of
                # 2 ** -16 during normal operation but force a stop when we've
                # generated enough steps.
                cd.start_span(STATE_MACHINE_RUN_LABEL)
                must_stop = None
                if steps_run >= max_steps:
                    must_stop = True
                elif steps_run <= _min_steps:
                    must_stop = False
                elif cd.length > (0.8 * BUFFER_SIZE):
                    # Better to stop after fewer steps, than always overrun and retry.
                    # See https://github.com/HypothesisWorks/hypothesis/issues/3618
                    must_stop = True

                start_draw = perf_counter()
                start_gc = gc_cumulative_time()
                if cd.draw_boolean(p=2**-16, forced=must_stop):
                    break
                steps_run += 1

                # Choose a rule to run, preferring an initialize rule if there are
                # any which have not been run yet.
                if machine._initialize_rules_to_run:
                    init_rules = [
                        st.tuples(st.just(rule), st.fixed_dictionaries(rule.arguments))
                        for rule in machine._initialize_rules_to_run
                    ]
                    rule, data = cd.draw(st.one_of(init_rules))
                    machine._initialize_rules_to_run.remove(rule)
                else:
                    rule, data = cd.draw(machine._rules_strategy)
                draw_label = f"generate:rule:{rule.function.__name__}"
                cd.draw_times.setdefault(draw_label, 0.0)
                in_gctime = gc_cumulative_time() - start_gc
                cd.draw_times[draw_label] += perf_counter() - start_draw - in_gctime

                # Pretty-print the values this rule was called with *before* calling
                # _add_results_to_targets, to avoid printing arguments which are also
                # a return value using the variable name they are assigned to.
                # See https://github.com/HypothesisWorks/hypothesis/issues/2341
                if print_steps or TESTCASE_CALLBACKS:
                    data_to_print = {
                        k: machine._pretty_print(v) for k, v in data.items()
                    }

                # Assign 'result' here in case executing the rule fails below
                result = multiple()
                try:
                    data = dict(data)
                    for k, v in list(data.items()):
                        if isinstance(v, VarReference):
                            data[k] = machine.names_to_values[v.name]
                        elif isinstance(v, list) and all(
                            isinstance(item, VarReference) for item in v
                        ):
                            data[k] = [machine.names_to_values[item.name] for item in v]

                    label = f"execute:rule:{rule.function.__name__}"
                    start = perf_counter()
                    start_gc = gc_cumulative_time()
                    result = rule.function(machine, **data)
                    in_gctime = gc_cumulative_time() - start_gc
                    cd._stateful_run_times[label] += perf_counter() - start - in_gctime

                    if rule.targets:
                        if isinstance(result, MultipleResults):
                            machine._add_results_to_targets(rule.targets, result.values)
                        else:
                            machine._add_results_to_targets(rule.targets, [result])
                    elif result is not None:
                        fail_health_check(
                            settings,
                            "Rules should return None if they have no target bundle, "
                            f"but {rule.function.__qualname__} returned {result!r}",
                            HealthCheck.return_value,
                        )
                finally:
                    if print_steps or TESTCASE_CALLBACKS:
                        # 'result' is only used if the step has target bundles.
                        # If it does, and the result is a 'MultipleResult',
                        # then 'print_step' prints a multi-variable assignment.
                        output(machine._repr_step(rule, data_to_print, result))
                machine.check_invariants(settings, output, cd._stateful_run_times)
                cd.stop_span()
        finally:
            output("state.teardown()")
            machine.teardown()

# Test reproduction with exact failing values:
def test_run_failing_test_run_state_machine():
    run_state_machine(
        factory=test_bank.FailingStateMachine,
        data=data(...),
    )

# Failing test extracted from Hypothesis

