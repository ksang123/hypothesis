# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 88

# Test reproduction with exact failing values:
def test_run_failing_test_test_002_subtraction_commutative():
    from test_bank import test_002_subtraction_commutative

    test_002_subtraction_commutative.hypothesis.inner_test(
        x=0,
        y=1,
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 126

# Test reproduction with exact failing values:
def test_run_failing_test_test_030_add_one_greater():
    from test_bank import test_030_add_one_greater

    test_030_add_one_greater.hypothesis.inner_test(
        x=9007199254740992.0,
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 140

# Test reproduction with exact failing values:
def test_run_failing_test_test_005_upper_is_lower():
    from test_bank import test_005_upper_is_lower

    test_005_upper_is_lower.hypothesis.inner_test(
        s='',
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 159

# Test reproduction with exact failing values:
def test_run_failing_test_test_032_string_is_upper():
    from test_bank import test_032_string_is_upper

    test_032_string_is_upper.hypothesis.inner_test(
        s='',
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 170

# Test reproduction with exact failing values:
def test_run_failing_test_test_034_ascii_only():
    from test_bank import test_034_ascii_only

    test_034_ascii_only.hypothesis.inner_test(
        s='\x80',
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 195

# Test reproduction with exact failing values:
def test_run_failing_test_test_009_sort_is_identity():
    from test_bank import test_009_sort_is_identity

    test_009_sort_is_identity.hypothesis.inner_test(
        lst=[0, -1],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 206

# Test reproduction with exact failing values:
def test_run_failing_test_test_037_list_unique():
    from test_bank import test_037_list_unique

    test_037_list_unique.hypothesis.inner_test(
        lst=[0, 0],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 222

# Test reproduction with exact failing values:
def test_run_failing_test_test_040_list_always_empty():
    from test_bank import test_040_list_always_empty

    test_040_list_always_empty.hypothesis.inner_test(
        lst=[0],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 230

# Test reproduction with exact failing values:
def test_run_failing_test_test_010_keys_values_equal():
    from test_bank import test_010_keys_values_equal

    test_010_keys_values_equal.hypothesis.inner_test(
        d={'': 0},
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 254

# Test reproduction with exact failing values:
def test_run_failing_test_test_042_dict_values_unique():
    from test_bank import test_042_dict_values_unique

    test_042_dict_values_unique.hypothesis.inner_test(
        d={'': 0, '0': 0},
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 265

# Test reproduction with exact failing values:
def test_run_failing_test_test_044_set_difference_empty():
    from test_bank import test_044_set_difference_empty

    test_044_set_difference_empty.hypothesis.inner_test(
        a={0},
        b=set(),
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 331

# Test reproduction with exact failing values:
def test_run_failing_test_test_017_dummy_inequality():
    from test_bank import test_017_dummy_inequality

    test_017_dummy_inequality.hypothesis.inner_test(
        obj=Dummy(0),
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 356

# Test reproduction with exact failing values:
def test_run_failing_test_test_053_point_x_positive():
    from test_bank import test_053_point_x_positive

    test_053_point_x_positive.hypothesis.inner_test(
        p=Point(0, 0),
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 500

# Test reproduction with exact failing values:
def test_run_failing_test_test_068_fail_on_42():
    from test_bank import test_068_fail_on_42

    test_068_fail_on_42.hypothesis.inner_test(
        x=42,
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 506

# Test reproduction with exact failing values:
def test_run_failing_test_test_069_fail_on_drawn():
    from test_bank import test_069_fail_on_drawn

    test_069_fail_on_drawn.hypothesis.inner_test(
        data=data(...),
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 512

# Test reproduction with exact failing values:
def test_run_failing_test_test_070_fail_on_empty():
    from test_bank import test_070_fail_on_empty

    test_070_fail_on_empty.hypothesis.inner_test(
        lst=[],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 526

# Test reproduction with exact failing values:
def test_run_failing_test_test_072_permutations():
    from test_bank import test_072_permutations

    test_072_permutations.hypothesis.inner_test(
        lst=[0, 0, 0],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 534

# Test reproduction with exact failing values:
def test_run_failing_test_test_073_permutation_fail():
    from test_bank import test_073_permutation_fail

    test_073_permutation_fail.hypothesis.inner_test(
        lst=[0, 0, 0],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 548

# Test reproduction with exact failing values:
def test_run_failing_test_test_075_bytes_fail():
    from test_bank import test_075_bytes_fail

    test_075_bytes_fail.hypothesis.inner_test(
        b=b'',
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 563

# Test reproduction with exact failing values:
def test_run_failing_test_test_078_booleans_fail():
    from test_bank import test_078_booleans_fail

    test_078_booleans_fail.hypothesis.inner_test(
        x=False,
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 574

# Test reproduction with exact failing values:
def test_run_failing_test_test_080_list_just_one_fail():
    from test_bank import test_080_list_just_one_fail

    test_080_list_just_one_fail.hypothesis.inner_test(
        lst=[1],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 584

# Test reproduction with exact failing values:
def test_run_failing_test_test_082_unicode_fail():
    from test_bank import test_082_unicode_fail

    test_082_unicode_fail.hypothesis.inner_test(
        s='',
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 594

# Test reproduction with exact failing values:
def test_run_failing_test_test_084_floats_fail():
    from test_bank import test_084_floats_fail

    test_084_floats_fail.hypothesis.inner_test(
        lst=[1.0],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 604

# Test reproduction with exact failing values:
def test_run_failing_test_test_086_dict_keys_fail():
    from test_bank import test_086_dict_keys_fail

    test_086_dict_keys_fail.hypothesis.inner_test(
        d={1: ''},
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 615

# Test reproduction with exact failing values:
def test_run_failing_test_test_088_list_of_lists_fail():
    from test_bank import test_088_list_of_lists_fail

    test_088_list_of_lists_fail.hypothesis.inner_test(
        lst=[[0]],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 625

# Test reproduction with exact failing values:
def test_run_failing_test_test_090_tuple_fail():
    from test_bank import test_090_tuple_fail

    test_090_tuple_fail.hypothesis.inner_test(
        t=(0, '', 1.0),
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 630

# Test reproduction with exact failing values:
def test_run_failing_test_test_108_point_origin():
    from test_bank import test_108_point_origin

    test_108_point_origin.hypothesis.inner_test(
        obj=Point(0, 1),
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 766

# Test reproduction with exact failing values:
def test_run_failing_test_run_state_machine():
    from test_bank import run_state_machine

    run_state_machine.hypothesis.inner_test(
        factory=test_bank.FailingStateMachine,
        data=data(...),
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 88

# Test reproduction with exact failing values:
def test_run_failing_test_test_002_subtraction_commutative():
    from test_bank import test_002_subtraction_commutative

    test_002_subtraction_commutative.hypothesis.inner_test(
        x=0,
        y=1,
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 126

# Test reproduction with exact failing values:
def test_run_failing_test_test_030_add_one_greater():
    from test_bank import test_030_add_one_greater

    test_030_add_one_greater.hypothesis.inner_test(
        x=9007199254740992.0,
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 140

# Test reproduction with exact failing values:
def test_run_failing_test_test_005_upper_is_lower():
    from test_bank import test_005_upper_is_lower

    test_005_upper_is_lower.hypothesis.inner_test(
        s='',
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 159

# Test reproduction with exact failing values:
def test_run_failing_test_test_032_string_is_upper():
    from test_bank import test_032_string_is_upper

    test_032_string_is_upper.hypothesis.inner_test(
        s='',
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 170

# Test reproduction with exact failing values:
def test_run_failing_test_test_034_ascii_only():
    from test_bank import test_034_ascii_only

    test_034_ascii_only.hypothesis.inner_test(
        s='\x80',
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 195

# Test reproduction with exact failing values:
def test_run_failing_test_test_009_sort_is_identity():
    from test_bank import test_009_sort_is_identity

    test_009_sort_is_identity.hypothesis.inner_test(
        lst=[0, -1],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 206

# Test reproduction with exact failing values:
def test_run_failing_test_test_037_list_unique():
    from test_bank import test_037_list_unique

    test_037_list_unique.hypothesis.inner_test(
        lst=[0, 0],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 222

# Test reproduction with exact failing values:
def test_run_failing_test_test_040_list_always_empty():
    from test_bank import test_040_list_always_empty

    test_040_list_always_empty.hypothesis.inner_test(
        lst=[0],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 230

# Test reproduction with exact failing values:
def test_run_failing_test_test_010_keys_values_equal():
    from test_bank import test_010_keys_values_equal

    test_010_keys_values_equal.hypothesis.inner_test(
        d={'': 0},
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 254

# Test reproduction with exact failing values:
def test_run_failing_test_test_042_dict_values_unique():
    from test_bank import test_042_dict_values_unique

    test_042_dict_values_unique.hypothesis.inner_test(
        d={'': 0, '0': 0},
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 265

# Test reproduction with exact failing values:
def test_run_failing_test_test_044_set_difference_empty():
    from test_bank import test_044_set_difference_empty

    test_044_set_difference_empty.hypothesis.inner_test(
        a={0},
        b=set(),
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 331

# Test reproduction with exact failing values:
def test_run_failing_test_test_017_dummy_inequality():
    from test_bank import test_017_dummy_inequality

    test_017_dummy_inequality.hypothesis.inner_test(
        obj=Dummy(0),
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 356

# Test reproduction with exact failing values:
def test_run_failing_test_test_053_point_x_positive():
    from test_bank import test_053_point_x_positive

    test_053_point_x_positive.hypothesis.inner_test(
        p=Point(0, 0),
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 500

# Test reproduction with exact failing values:
def test_run_failing_test_test_068_fail_on_42():
    from test_bank import test_068_fail_on_42

    test_068_fail_on_42.hypothesis.inner_test(
        x=42,
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 506

# Test reproduction with exact failing values:
def test_run_failing_test_test_069_fail_on_drawn():
    from test_bank import test_069_fail_on_drawn

    test_069_fail_on_drawn.hypothesis.inner_test(
        data=data(...),
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 512

# Test reproduction with exact failing values:
def test_run_failing_test_test_070_fail_on_empty():
    from test_bank import test_070_fail_on_empty

    test_070_fail_on_empty.hypothesis.inner_test(
        lst=[],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 526

# Test reproduction with exact failing values:
def test_run_failing_test_test_072_permutations():
    from test_bank import test_072_permutations

    test_072_permutations.hypothesis.inner_test(
        lst=[0, 0, 0],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 534

# Test reproduction with exact failing values:
def test_run_failing_test_test_073_permutation_fail():
    from test_bank import test_073_permutation_fail

    test_073_permutation_fail.hypothesis.inner_test(
        lst=[0, 0, 0],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 548

# Test reproduction with exact failing values:
def test_run_failing_test_test_075_bytes_fail():
    from test_bank import test_075_bytes_fail

    test_075_bytes_fail.hypothesis.inner_test(
        b=b'',
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 563

# Test reproduction with exact failing values:
def test_run_failing_test_test_078_booleans_fail():
    from test_bank import test_078_booleans_fail

    test_078_booleans_fail.hypothesis.inner_test(
        x=False,
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 574

# Test reproduction with exact failing values:
def test_run_failing_test_test_080_list_just_one_fail():
    from test_bank import test_080_list_just_one_fail

    test_080_list_just_one_fail.hypothesis.inner_test(
        lst=[1],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 584

# Test reproduction with exact failing values:
def test_run_failing_test_test_082_unicode_fail():
    from test_bank import test_082_unicode_fail

    test_082_unicode_fail.hypothesis.inner_test(
        s='',
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 594

# Test reproduction with exact failing values:
def test_run_failing_test_test_084_floats_fail():
    from test_bank import test_084_floats_fail

    test_084_floats_fail.hypothesis.inner_test(
        lst=[1.0],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 604

# Test reproduction with exact failing values:
def test_run_failing_test_test_086_dict_keys_fail():
    from test_bank import test_086_dict_keys_fail

    test_086_dict_keys_fail.hypothesis.inner_test(
        d={1: ''},
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 615

# Test reproduction with exact failing values:
def test_run_failing_test_test_088_list_of_lists_fail():
    from test_bank import test_088_list_of_lists_fail

    test_088_list_of_lists_fail.hypothesis.inner_test(
        lst=[[0]],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 625

# Test reproduction with exact failing values:
def test_run_failing_test_test_090_tuple_fail():
    from test_bank import test_090_tuple_fail

    test_090_tuple_fail.hypothesis.inner_test(
        t=(0, '', 1.0),
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 630

# Test reproduction with exact failing values:
def test_run_failing_test_test_108_point_origin():
    from test_bank import test_108_point_origin

    test_108_point_origin.hypothesis.inner_test(
        obj=Point(0, 1),
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 766

# Test reproduction with exact failing values:
def test_run_failing_test_run_state_machine():
    from test_bank import run_state_machine

    run_state_machine.hypothesis.inner_test(
        factory=test_bank.FailingStateMachine,
        data=data(...),
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 88

# Test reproduction with exact failing values:
def test_run_failing_test_test_002_subtraction_commutative():
    from test_bank import test_002_subtraction_commutative

    test_002_subtraction_commutative.hypothesis.inner_test(
        x=0,
        y=1,
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 126

# Test reproduction with exact failing values:
def test_run_failing_test_test_030_add_one_greater():
    from test_bank import test_030_add_one_greater

    test_030_add_one_greater.hypothesis.inner_test(
        x=9007199254740992.0,
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 140

# Test reproduction with exact failing values:
def test_run_failing_test_test_005_upper_is_lower():
    from test_bank import test_005_upper_is_lower

    test_005_upper_is_lower.hypothesis.inner_test(
        s='',
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 159

# Test reproduction with exact failing values:
def test_run_failing_test_test_032_string_is_upper():
    from test_bank import test_032_string_is_upper

    test_032_string_is_upper.hypothesis.inner_test(
        s='',
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 170

# Test reproduction with exact failing values:
def test_run_failing_test_test_034_ascii_only():
    from test_bank import test_034_ascii_only

    test_034_ascii_only.hypothesis.inner_test(
        s='\x80',
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 195

# Test reproduction with exact failing values:
def test_run_failing_test_test_009_sort_is_identity():
    from test_bank import test_009_sort_is_identity

    test_009_sort_is_identity.hypothesis.inner_test(
        lst=[0, -1],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 206

# Test reproduction with exact failing values:
def test_run_failing_test_test_037_list_unique():
    from test_bank import test_037_list_unique

    test_037_list_unique.hypothesis.inner_test(
        lst=[0, 0],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 222

# Test reproduction with exact failing values:
def test_run_failing_test_test_040_list_always_empty():
    from test_bank import test_040_list_always_empty

    test_040_list_always_empty.hypothesis.inner_test(
        lst=[0],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 230

# Test reproduction with exact failing values:
def test_run_failing_test_test_010_keys_values_equal():
    from test_bank import test_010_keys_values_equal

    test_010_keys_values_equal.hypothesis.inner_test(
        d={'': 0},
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 254

# Test reproduction with exact failing values:
def test_run_failing_test_test_042_dict_values_unique():
    from test_bank import test_042_dict_values_unique

    test_042_dict_values_unique.hypothesis.inner_test(
        d={'': 0, '0': 0},
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 265

# Test reproduction with exact failing values:
def test_run_failing_test_test_044_set_difference_empty():
    from test_bank import test_044_set_difference_empty

    test_044_set_difference_empty.hypothesis.inner_test(
        a={0},
        b=set(),
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 331

# Test reproduction with exact failing values:
def test_run_failing_test_test_017_dummy_inequality():
    from test_bank import test_017_dummy_inequality

    test_017_dummy_inequality.hypothesis.inner_test(
        obj=Dummy(0),
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 356

# Test reproduction with exact failing values:
def test_run_failing_test_test_053_point_x_positive():
    from test_bank import test_053_point_x_positive

    test_053_point_x_positive.hypothesis.inner_test(
        p=Point(0, 0),
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 500

# Test reproduction with exact failing values:
def test_run_failing_test_test_068_fail_on_42():
    from test_bank import test_068_fail_on_42

    test_068_fail_on_42.hypothesis.inner_test(
        x=42,
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 506

# Test reproduction with exact failing values:
def test_run_failing_test_test_069_fail_on_drawn():
    from test_bank import test_069_fail_on_drawn

    test_069_fail_on_drawn.hypothesis.inner_test(
        data=data(...),
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 512

# Test reproduction with exact failing values:
def test_run_failing_test_test_070_fail_on_empty():
    from test_bank import test_070_fail_on_empty

    test_070_fail_on_empty.hypothesis.inner_test(
        lst=[],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 526

# Test reproduction with exact failing values:
def test_run_failing_test_test_072_permutations():
    from test_bank import test_072_permutations

    test_072_permutations.hypothesis.inner_test(
        lst=[0, 0, 0],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 534

# Test reproduction with exact failing values:
def test_run_failing_test_test_073_permutation_fail():
    from test_bank import test_073_permutation_fail

    test_073_permutation_fail.hypothesis.inner_test(
        lst=[0, 0, 0],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 548

# Test reproduction with exact failing values:
def test_run_failing_test_test_075_bytes_fail():
    from test_bank import test_075_bytes_fail

    test_075_bytes_fail.hypothesis.inner_test(
        b=b'',
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 563

# Test reproduction with exact failing values:
def test_run_failing_test_test_078_booleans_fail():
    from test_bank import test_078_booleans_fail

    test_078_booleans_fail.hypothesis.inner_test(
        x=False,
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 574

# Test reproduction with exact failing values:
def test_run_failing_test_test_080_list_just_one_fail():
    from test_bank import test_080_list_just_one_fail

    test_080_list_just_one_fail.hypothesis.inner_test(
        lst=[1],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 584

# Test reproduction with exact failing values:
def test_run_failing_test_test_082_unicode_fail():
    from test_bank import test_082_unicode_fail

    test_082_unicode_fail.hypothesis.inner_test(
        s='',
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 594

# Test reproduction with exact failing values:
def test_run_failing_test_test_084_floats_fail():
    from test_bank import test_084_floats_fail

    test_084_floats_fail.hypothesis.inner_test(
        lst=[1.0],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 604

# Test reproduction with exact failing values:
def test_run_failing_test_test_086_dict_keys_fail():
    from test_bank import test_086_dict_keys_fail

    test_086_dict_keys_fail.hypothesis.inner_test(
        d={1: ''},
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 615

# Test reproduction with exact failing values:
def test_run_failing_test_test_088_list_of_lists_fail():
    from test_bank import test_088_list_of_lists_fail

    test_088_list_of_lists_fail.hypothesis.inner_test(
        lst=[[0]],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 625

# Test reproduction with exact failing values:
def test_run_failing_test_test_090_tuple_fail():
    from test_bank import test_090_tuple_fail

    test_090_tuple_fail.hypothesis.inner_test(
        t=(0, '', 1.0),
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 630

# Test reproduction with exact failing values:
def test_run_failing_test_test_108_point_origin():
    from test_bank import test_108_point_origin

    test_108_point_origin.hypothesis.inner_test(
        obj=Point(0, 1),
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 88

# Test reproduction with exact failing values:
def test_run_failing_test_test_002_subtraction_commutative():
    from test_bank import test_002_subtraction_commutative

    test_002_subtraction_commutative.hypothesis.inner_test(
        x=0,
        y=1,
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 126

# Test reproduction with exact failing values:
def test_run_failing_test_test_030_add_one_greater():
    from test_bank import test_030_add_one_greater

    test_030_add_one_greater.hypothesis.inner_test(
        x=9007199254740992.0,
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 140

# Test reproduction with exact failing values:
def test_run_failing_test_test_005_upper_is_lower():
    from test_bank import test_005_upper_is_lower

    test_005_upper_is_lower.hypothesis.inner_test(
        s='',
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 159

# Test reproduction with exact failing values:
def test_run_failing_test_test_032_string_is_upper():
    from test_bank import test_032_string_is_upper

    test_032_string_is_upper.hypothesis.inner_test(
        s='',
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 170

# Test reproduction with exact failing values:
def test_run_failing_test_test_034_ascii_only():
    from test_bank import test_034_ascii_only

    test_034_ascii_only.hypothesis.inner_test(
        s='\x80',
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 195

# Test reproduction with exact failing values:
def test_run_failing_test_test_009_sort_is_identity():
    from test_bank import test_009_sort_is_identity

    test_009_sort_is_identity.hypothesis.inner_test(
        lst=[0, -1],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 206

# Test reproduction with exact failing values:
def test_run_failing_test_test_037_list_unique():
    from test_bank import test_037_list_unique

    test_037_list_unique.hypothesis.inner_test(
        lst=[0, 0],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 222

# Test reproduction with exact failing values:
def test_run_failing_test_test_040_list_always_empty():
    from test_bank import test_040_list_always_empty

    test_040_list_always_empty.hypothesis.inner_test(
        lst=[0],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 230

# Test reproduction with exact failing values:
def test_run_failing_test_test_010_keys_values_equal():
    from test_bank import test_010_keys_values_equal

    test_010_keys_values_equal.hypothesis.inner_test(
        d={'': 0},
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 254

# Test reproduction with exact failing values:
def test_run_failing_test_test_042_dict_values_unique():
    from test_bank import test_042_dict_values_unique

    test_042_dict_values_unique.hypothesis.inner_test(
        d={'': 0, '0': 0},
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 265

# Test reproduction with exact failing values:
def test_run_failing_test_test_044_set_difference_empty():
    from test_bank import test_044_set_difference_empty

    test_044_set_difference_empty.hypothesis.inner_test(
        a={0},
        b=set(),
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 331

# Test reproduction with exact failing values:
def test_run_failing_test_test_017_dummy_inequality():
    from test_bank import test_017_dummy_inequality

    test_017_dummy_inequality.hypothesis.inner_test(
        obj=Dummy(0),
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 356

# Test reproduction with exact failing values:
def test_run_failing_test_test_053_point_x_positive():
    from test_bank import test_053_point_x_positive

    test_053_point_x_positive.hypothesis.inner_test(
        p=Point(0, 0),
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 500

# Test reproduction with exact failing values:
def test_run_failing_test_test_068_fail_on_42():
    from test_bank import test_068_fail_on_42

    test_068_fail_on_42.hypothesis.inner_test(
        x=42,
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 506

# Test reproduction with exact failing values:
def test_run_failing_test_test_069_fail_on_drawn():
    from test_bank import test_069_fail_on_drawn

    test_069_fail_on_drawn.hypothesis.inner_test(
        data=data(...),
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 512

# Test reproduction with exact failing values:
def test_run_failing_test_test_070_fail_on_empty():
    from test_bank import test_070_fail_on_empty

    test_070_fail_on_empty.hypothesis.inner_test(
        lst=[],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 526

# Test reproduction with exact failing values:
def test_run_failing_test_test_072_permutations():
    from test_bank import test_072_permutations

    test_072_permutations.hypothesis.inner_test(
        lst=[0, 0, 0],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 534

# Test reproduction with exact failing values:
def test_run_failing_test_test_073_permutation_fail():
    from test_bank import test_073_permutation_fail

    test_073_permutation_fail.hypothesis.inner_test(
        lst=[0, 0, 0],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 548

# Test reproduction with exact failing values:
def test_run_failing_test_test_075_bytes_fail():
    from test_bank import test_075_bytes_fail

    test_075_bytes_fail.hypothesis.inner_test(
        b=b'',
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 563

# Test reproduction with exact failing values:
def test_run_failing_test_test_078_booleans_fail():
    from test_bank import test_078_booleans_fail

    test_078_booleans_fail.hypothesis.inner_test(
        x=False,
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 574

# Test reproduction with exact failing values:
def test_run_failing_test_test_080_list_just_one_fail():
    from test_bank import test_080_list_just_one_fail

    test_080_list_just_one_fail.hypothesis.inner_test(
        lst=[1],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 584

# Test reproduction with exact failing values:
def test_run_failing_test_test_082_unicode_fail():
    from test_bank import test_082_unicode_fail

    test_082_unicode_fail.hypothesis.inner_test(
        s='',
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 594

# Test reproduction with exact failing values:
def test_run_failing_test_test_084_floats_fail():
    from test_bank import test_084_floats_fail

    test_084_floats_fail.hypothesis.inner_test(
        lst=[1.0],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 604

# Test reproduction with exact failing values:
def test_run_failing_test_test_086_dict_keys_fail():
    from test_bank import test_086_dict_keys_fail

    test_086_dict_keys_fail.hypothesis.inner_test(
        d={1: ''},
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 615

# Test reproduction with exact failing values:
def test_run_failing_test_test_088_list_of_lists_fail():
    from test_bank import test_088_list_of_lists_fail

    test_088_list_of_lists_fail.hypothesis.inner_test(
        lst=[[0]],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 625

# Test reproduction with exact failing values:
def test_run_failing_test_test_090_tuple_fail():
    from test_bank import test_090_tuple_fail

    test_090_tuple_fail.hypothesis.inner_test(
        t=(0, '', 1.0),
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 630

# Test reproduction with exact failing values:
def test_run_failing_test_test_108_point_origin():
    from test_bank import test_108_point_origin

    test_108_point_origin.hypothesis.inner_test(
        obj=Point(0, 1),
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 766

# Test reproduction with exact failing values:
def test_run_failing_test_run_state_machine():
    from test_bank import run_state_machine

    run_state_machine.hypothesis.inner_test(
        factory=test_bank.FailingStateMachine,
        data=data(...),
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 88

# Test reproduction with exact failing values:
def test_run_failing_test_test_002_subtraction_commutative():
    from test_bank import test_002_subtraction_commutative

    test_002_subtraction_commutative.hypothesis.inner_test(
        x=0,
        y=1,
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 126

# Test reproduction with exact failing values:
def test_run_failing_test_test_030_add_one_greater():
    from test_bank import test_030_add_one_greater

    test_030_add_one_greater.hypothesis.inner_test(
        x=9007199254740992.0,
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 140

# Test reproduction with exact failing values:
def test_run_failing_test_test_005_upper_is_lower():
    from test_bank import test_005_upper_is_lower

    test_005_upper_is_lower.hypothesis.inner_test(
        s='',
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 159

# Test reproduction with exact failing values:
def test_run_failing_test_test_032_string_is_upper():
    from test_bank import test_032_string_is_upper

    test_032_string_is_upper.hypothesis.inner_test(
        s='',
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 170

# Test reproduction with exact failing values:
def test_run_failing_test_test_034_ascii_only():
    from test_bank import test_034_ascii_only

    test_034_ascii_only.hypothesis.inner_test(
        s='\x80',
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 195

# Test reproduction with exact failing values:
def test_run_failing_test_test_009_sort_is_identity():
    from test_bank import test_009_sort_is_identity

    test_009_sort_is_identity.hypothesis.inner_test(
        lst=[0, -1],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 206

# Test reproduction with exact failing values:
def test_run_failing_test_test_037_list_unique():
    from test_bank import test_037_list_unique

    test_037_list_unique.hypothesis.inner_test(
        lst=[0, 0],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 222

# Test reproduction with exact failing values:
def test_run_failing_test_test_040_list_always_empty():
    from test_bank import test_040_list_always_empty

    test_040_list_always_empty.hypothesis.inner_test(
        lst=[0],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 230

# Test reproduction with exact failing values:
def test_run_failing_test_test_010_keys_values_equal():
    from test_bank import test_010_keys_values_equal

    test_010_keys_values_equal.hypothesis.inner_test(
        d={'': 0},
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 254

# Test reproduction with exact failing values:
def test_run_failing_test_test_042_dict_values_unique():
    from test_bank import test_042_dict_values_unique

    test_042_dict_values_unique.hypothesis.inner_test(
        d={'': 0, '0': 0},
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 265

# Test reproduction with exact failing values:
def test_run_failing_test_test_044_set_difference_empty():
    from test_bank import test_044_set_difference_empty

    test_044_set_difference_empty.hypothesis.inner_test(
        a={0},
        b=set(),
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 331

# Test reproduction with exact failing values:
def test_run_failing_test_test_017_dummy_inequality():
    from test_bank import test_017_dummy_inequality

    test_017_dummy_inequality.hypothesis.inner_test(
        obj=Dummy(0),
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 356

# Test reproduction with exact failing values:
def test_run_failing_test_test_053_point_x_positive():
    from test_bank import test_053_point_x_positive

    test_053_point_x_positive.hypothesis.inner_test(
        p=Point(0, 0),
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 500

# Test reproduction with exact failing values:
def test_run_failing_test_test_068_fail_on_42():
    from test_bank import test_068_fail_on_42

    test_068_fail_on_42.hypothesis.inner_test(
        x=42,
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 506

# Test reproduction with exact failing values:
def test_run_failing_test_test_069_fail_on_drawn():
    from test_bank import test_069_fail_on_drawn

    test_069_fail_on_drawn.hypothesis.inner_test(
        data=data(...),
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 512

# Test reproduction with exact failing values:
def test_run_failing_test_test_070_fail_on_empty():
    from test_bank import test_070_fail_on_empty

    test_070_fail_on_empty.hypothesis.inner_test(
        lst=[],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 526

# Test reproduction with exact failing values:
def test_run_failing_test_test_072_permutations():
    from test_bank import test_072_permutations

    test_072_permutations.hypothesis.inner_test(
        lst=[0, 0, 0],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 534

# Test reproduction with exact failing values:
def test_run_failing_test_test_073_permutation_fail():
    from test_bank import test_073_permutation_fail

    test_073_permutation_fail.hypothesis.inner_test(
        lst=[0, 0, 0],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 548

# Test reproduction with exact failing values:
def test_run_failing_test_test_075_bytes_fail():
    from test_bank import test_075_bytes_fail

    test_075_bytes_fail.hypothesis.inner_test(
        b=b'',
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 563

# Test reproduction with exact failing values:
def test_run_failing_test_test_078_booleans_fail():
    from test_bank import test_078_booleans_fail

    test_078_booleans_fail.hypothesis.inner_test(
        x=False,
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 574

# Test reproduction with exact failing values:
def test_run_failing_test_test_080_list_just_one_fail():
    from test_bank import test_080_list_just_one_fail

    test_080_list_just_one_fail.hypothesis.inner_test(
        lst=[1],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 584

# Test reproduction with exact failing values:
def test_run_failing_test_test_082_unicode_fail():
    from test_bank import test_082_unicode_fail

    test_082_unicode_fail.hypothesis.inner_test(
        s='',
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 594

# Test reproduction with exact failing values:
def test_run_failing_test_test_084_floats_fail():
    from test_bank import test_084_floats_fail

    test_084_floats_fail.hypothesis.inner_test(
        lst=[1.0],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 604

# Test reproduction with exact failing values:
def test_run_failing_test_test_086_dict_keys_fail():
    from test_bank import test_086_dict_keys_fail

    test_086_dict_keys_fail.hypothesis.inner_test(
        d={1: ''},
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 615

# Test reproduction with exact failing values:
def test_run_failing_test_test_088_list_of_lists_fail():
    from test_bank import test_088_list_of_lists_fail

    test_088_list_of_lists_fail.hypothesis.inner_test(
        lst=[[0]],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 625

# Test reproduction with exact failing values:
def test_run_failing_test_test_090_tuple_fail():
    from test_bank import test_090_tuple_fail

    test_090_tuple_fail.hypothesis.inner_test(
        t=(0, '', 1.0),
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 630

# Test reproduction with exact failing values:
def test_run_failing_test_test_108_point_origin():
    from test_bank import test_108_point_origin

    test_108_point_origin.hypothesis.inner_test(
        obj=Point(0, 1),
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 766

# Test reproduction with exact failing values:
def test_run_failing_test_run_state_machine():
    from test_bank import run_state_machine

    run_state_machine.hypothesis.inner_test(
        factory=test_bank.FailingStateMachine,
        data=data(...),
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 88

# Test reproduction with exact failing values:
def test_run_failing_test_test_002_subtraction_commutative():
    from test_bank import test_002_subtraction_commutative

    test_002_subtraction_commutative.hypothesis.inner_test(
        x=0,
        y=1,
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 126

# Test reproduction with exact failing values:
def test_run_failing_test_test_030_add_one_greater():
    from test_bank import test_030_add_one_greater

    test_030_add_one_greater.hypothesis.inner_test(
        x=9007199254740992.0,
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 140

# Test reproduction with exact failing values:
def test_run_failing_test_test_005_upper_is_lower():
    from test_bank import test_005_upper_is_lower

    test_005_upper_is_lower.hypothesis.inner_test(
        s='',
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 159

# Test reproduction with exact failing values:
def test_run_failing_test_test_032_string_is_upper():
    from test_bank import test_032_string_is_upper

    test_032_string_is_upper.hypothesis.inner_test(
        s='',
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 170

# Test reproduction with exact failing values:
def test_run_failing_test_test_034_ascii_only():
    from test_bank import test_034_ascii_only

    test_034_ascii_only.hypothesis.inner_test(
        s='\x80',
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 195

# Test reproduction with exact failing values:
def test_run_failing_test_test_009_sort_is_identity():
    from test_bank import test_009_sort_is_identity

    test_009_sort_is_identity.hypothesis.inner_test(
        lst=[0, -1],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 206

# Test reproduction with exact failing values:
def test_run_failing_test_test_037_list_unique():
    from test_bank import test_037_list_unique

    test_037_list_unique.hypothesis.inner_test(
        lst=[0, 0],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 222

# Test reproduction with exact failing values:
def test_run_failing_test_test_040_list_always_empty():
    from test_bank import test_040_list_always_empty

    test_040_list_always_empty.hypothesis.inner_test(
        lst=[0],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 230

# Test reproduction with exact failing values:
def test_run_failing_test_test_010_keys_values_equal():
    from test_bank import test_010_keys_values_equal

    test_010_keys_values_equal.hypothesis.inner_test(
        d={'': 0},
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 254

# Test reproduction with exact failing values:
def test_run_failing_test_test_042_dict_values_unique():
    from test_bank import test_042_dict_values_unique

    test_042_dict_values_unique.hypothesis.inner_test(
        d={'': 0, '0': 0},
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 265

# Test reproduction with exact failing values:
def test_run_failing_test_test_044_set_difference_empty():
    from test_bank import test_044_set_difference_empty

    test_044_set_difference_empty.hypothesis.inner_test(
        a={0},
        b=set(),
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 331

# Test reproduction with exact failing values:
def test_run_failing_test_test_017_dummy_inequality():
    from test_bank import test_017_dummy_inequality

    test_017_dummy_inequality.hypothesis.inner_test(
        obj=Dummy(0),
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 356

# Test reproduction with exact failing values:
def test_run_failing_test_test_053_point_x_positive():
    from test_bank import test_053_point_x_positive

    test_053_point_x_positive.hypothesis.inner_test(
        p=Point(0, 0),
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 500

# Test reproduction with exact failing values:
def test_run_failing_test_test_068_fail_on_42():
    from test_bank import test_068_fail_on_42

    test_068_fail_on_42.hypothesis.inner_test(
        x=42,
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 506

# Test reproduction with exact failing values:
def test_run_failing_test_test_069_fail_on_drawn():
    from test_bank import test_069_fail_on_drawn

    test_069_fail_on_drawn.hypothesis.inner_test(
        data=data(...),
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 512

# Test reproduction with exact failing values:
def test_run_failing_test_test_070_fail_on_empty():
    from test_bank import test_070_fail_on_empty

    test_070_fail_on_empty.hypothesis.inner_test(
        lst=[],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 526

# Test reproduction with exact failing values:
def test_run_failing_test_test_072_permutations():
    from test_bank import test_072_permutations

    test_072_permutations.hypothesis.inner_test(
        lst=[0, 0, 0],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 534

# Test reproduction with exact failing values:
def test_run_failing_test_test_073_permutation_fail():
    from test_bank import test_073_permutation_fail

    test_073_permutation_fail.hypothesis.inner_test(
        lst=[0, 0, 0],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 548

# Test reproduction with exact failing values:
def test_run_failing_test_test_075_bytes_fail():
    from test_bank import test_075_bytes_fail

    test_075_bytes_fail.hypothesis.inner_test(
        b=b'',
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 563

# Test reproduction with exact failing values:
def test_run_failing_test_test_078_booleans_fail():
    from test_bank import test_078_booleans_fail

    test_078_booleans_fail.hypothesis.inner_test(
        x=False,
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 574

# Test reproduction with exact failing values:
def test_run_failing_test_test_080_list_just_one_fail():
    from test_bank import test_080_list_just_one_fail

    test_080_list_just_one_fail.hypothesis.inner_test(
        lst=[1],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 584

# Test reproduction with exact failing values:
def test_run_failing_test_test_082_unicode_fail():
    from test_bank import test_082_unicode_fail

    test_082_unicode_fail.hypothesis.inner_test(
        s='',
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 594

# Test reproduction with exact failing values:
def test_run_failing_test_test_084_floats_fail():
    from test_bank import test_084_floats_fail

    test_084_floats_fail.hypothesis.inner_test(
        lst=[1.0],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 604

# Test reproduction with exact failing values:
def test_run_failing_test_test_086_dict_keys_fail():
    from test_bank import test_086_dict_keys_fail

    test_086_dict_keys_fail.hypothesis.inner_test(
        d={1: ''},
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 615

# Test reproduction with exact failing values:
def test_run_failing_test_test_088_list_of_lists_fail():
    from test_bank import test_088_list_of_lists_fail

    test_088_list_of_lists_fail.hypothesis.inner_test(
        lst=[[0]],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 625

# Test reproduction with exact failing values:
def test_run_failing_test_test_090_tuple_fail():
    from test_bank import test_090_tuple_fail

    test_090_tuple_fail.hypothesis.inner_test(
        t=(0, '', 1.0),
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 630

# Test reproduction with exact failing values:
def test_run_failing_test_test_108_point_origin():
    from test_bank import test_108_point_origin

    test_108_point_origin.hypothesis.inner_test(
        obj=Point(0, 1),
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 766

# Test reproduction with exact failing values:
def test_run_failing_test_run_state_machine():
    from test_bank import run_state_machine

    run_state_machine.hypothesis.inner_test(
        factory=test_bank.FailingStateMachine,
        data=data(...),
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 88

# Test reproduction with exact failing values:
def test_run_failing_test_test_002_subtraction_commutative():
    from test_bank import test_002_subtraction_commutative

    test_002_subtraction_commutative.hypothesis.inner_test(
        x=0,
        y=1,
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 126

# Test reproduction with exact failing values:
def test_run_failing_test_test_030_add_one_greater():
    from test_bank import test_030_add_one_greater

    test_030_add_one_greater.hypothesis.inner_test(
        x=9007199254740992.0,
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 140

# Test reproduction with exact failing values:
def test_run_failing_test_test_005_upper_is_lower():
    from test_bank import test_005_upper_is_lower

    test_005_upper_is_lower.hypothesis.inner_test(
        s='',
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 159

# Test reproduction with exact failing values:
def test_run_failing_test_test_032_string_is_upper():
    from test_bank import test_032_string_is_upper

    test_032_string_is_upper.hypothesis.inner_test(
        s='',
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 170

# Test reproduction with exact failing values:
def test_run_failing_test_test_034_ascii_only():
    from test_bank import test_034_ascii_only

    test_034_ascii_only.hypothesis.inner_test(
        s='\x80',
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 195

# Test reproduction with exact failing values:
def test_run_failing_test_test_009_sort_is_identity():
    from test_bank import test_009_sort_is_identity

    test_009_sort_is_identity.hypothesis.inner_test(
        lst=[0, -1],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 206

# Test reproduction with exact failing values:
def test_run_failing_test_test_037_list_unique():
    from test_bank import test_037_list_unique

    test_037_list_unique.hypothesis.inner_test(
        lst=[0, 0],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 222

# Test reproduction with exact failing values:
def test_run_failing_test_test_040_list_always_empty():
    from test_bank import test_040_list_always_empty

    test_040_list_always_empty.hypothesis.inner_test(
        lst=[0],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 230

# Test reproduction with exact failing values:
def test_run_failing_test_test_010_keys_values_equal():
    from test_bank import test_010_keys_values_equal

    test_010_keys_values_equal.hypothesis.inner_test(
        d={'': 0},
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 254

# Test reproduction with exact failing values:
def test_run_failing_test_test_042_dict_values_unique():
    from test_bank import test_042_dict_values_unique

    test_042_dict_values_unique.hypothesis.inner_test(
        d={'': 0, '0': 0},
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 265

# Test reproduction with exact failing values:
def test_run_failing_test_test_044_set_difference_empty():
    from test_bank import test_044_set_difference_empty

    test_044_set_difference_empty.hypothesis.inner_test(
        a={0},
        b=set(),
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 331

# Test reproduction with exact failing values:
def test_run_failing_test_test_017_dummy_inequality():
    from test_bank import test_017_dummy_inequality

    test_017_dummy_inequality.hypothesis.inner_test(
        obj=Dummy(0),
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 356

# Test reproduction with exact failing values:
def test_run_failing_test_test_053_point_x_positive():
    from test_bank import test_053_point_x_positive

    test_053_point_x_positive.hypothesis.inner_test(
        p=Point(0, 0),
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 500

# Test reproduction with exact failing values:
def test_run_failing_test_test_068_fail_on_42():
    from test_bank import test_068_fail_on_42

    test_068_fail_on_42.hypothesis.inner_test(
        x=42,
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 506

# Test reproduction with exact failing values:
def test_run_failing_test_test_069_fail_on_drawn():
    from test_bank import test_069_fail_on_drawn

    test_069_fail_on_drawn.hypothesis.inner_test(
        data=data(...),
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 512

# Test reproduction with exact failing values:
def test_run_failing_test_test_070_fail_on_empty():
    from test_bank import test_070_fail_on_empty

    test_070_fail_on_empty.hypothesis.inner_test(
        lst=[],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 526

# Test reproduction with exact failing values:
def test_run_failing_test_test_072_permutations():
    from test_bank import test_072_permutations

    test_072_permutations.hypothesis.inner_test(
        lst=[0, 0, 0],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 534

# Test reproduction with exact failing values:
def test_run_failing_test_test_073_permutation_fail():
    from test_bank import test_073_permutation_fail

    test_073_permutation_fail.hypothesis.inner_test(
        lst=[0, 0, 0],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 548

# Test reproduction with exact failing values:
def test_run_failing_test_test_075_bytes_fail():
    from test_bank import test_075_bytes_fail

    test_075_bytes_fail.hypothesis.inner_test(
        b=b'',
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 563

# Test reproduction with exact failing values:
def test_run_failing_test_test_078_booleans_fail():
    from test_bank import test_078_booleans_fail

    test_078_booleans_fail.hypothesis.inner_test(
        x=False,
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 574

# Test reproduction with exact failing values:
def test_run_failing_test_test_080_list_just_one_fail():
    from test_bank import test_080_list_just_one_fail

    test_080_list_just_one_fail.hypothesis.inner_test(
        lst=[1],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 584

# Test reproduction with exact failing values:
def test_run_failing_test_test_082_unicode_fail():
    from test_bank import test_082_unicode_fail

    test_082_unicode_fail.hypothesis.inner_test(
        s='',
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 594

# Test reproduction with exact failing values:
def test_run_failing_test_test_084_floats_fail():
    from test_bank import test_084_floats_fail

    test_084_floats_fail.hypothesis.inner_test(
        lst=[1.0],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 604

# Test reproduction with exact failing values:
def test_run_failing_test_test_086_dict_keys_fail():
    from test_bank import test_086_dict_keys_fail

    test_086_dict_keys_fail.hypothesis.inner_test(
        d={1: ''},
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 615

# Test reproduction with exact failing values:
def test_run_failing_test_test_088_list_of_lists_fail():
    from test_bank import test_088_list_of_lists_fail

    test_088_list_of_lists_fail.hypothesis.inner_test(
        lst=[[0]],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 625

# Test reproduction with exact failing values:
def test_run_failing_test_test_090_tuple_fail():
    from test_bank import test_090_tuple_fail

    test_090_tuple_fail.hypothesis.inner_test(
        t=(0, '', 1.0),
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 630

# Test reproduction with exact failing values:
def test_run_failing_test_test_108_point_origin():
    from test_bank import test_108_point_origin

    test_108_point_origin.hypothesis.inner_test(
        obj=Point(0, 1),
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 766

# Test reproduction with exact failing values:
def test_run_failing_test_run_state_machine():
    from test_bank import run_state_machine

    run_state_machine.hypothesis.inner_test(
        factory=test_bank.FailingStateMachine,
        data=data(...),
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 88

# Test reproduction with exact failing values:
def test_run_failing_test_test_002_subtraction_commutative():
    from test_bank import test_002_subtraction_commutative

    test_002_subtraction_commutative.hypothesis.inner_test(
        x=0,
        y=1,
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 126

# Test reproduction with exact failing values:
def test_run_failing_test_test_030_add_one_greater():
    from test_bank import test_030_add_one_greater

    test_030_add_one_greater.hypothesis.inner_test(
        x=9007199254740992.0,
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 140

# Test reproduction with exact failing values:
def test_run_failing_test_test_005_upper_is_lower():
    from test_bank import test_005_upper_is_lower

    test_005_upper_is_lower.hypothesis.inner_test(
        s='',
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 159

# Test reproduction with exact failing values:
def test_run_failing_test_test_032_string_is_upper():
    from test_bank import test_032_string_is_upper

    test_032_string_is_upper.hypothesis.inner_test(
        s='',
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 170

# Test reproduction with exact failing values:
def test_run_failing_test_test_034_ascii_only():
    from test_bank import test_034_ascii_only

    test_034_ascii_only.hypothesis.inner_test(
        s='\x80',
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 195

# Test reproduction with exact failing values:
def test_run_failing_test_test_009_sort_is_identity():
    from test_bank import test_009_sort_is_identity

    test_009_sort_is_identity.hypothesis.inner_test(
        lst=[0, -1],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 206

# Test reproduction with exact failing values:
def test_run_failing_test_test_037_list_unique():
    from test_bank import test_037_list_unique

    test_037_list_unique.hypothesis.inner_test(
        lst=[0, 0],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 222

# Test reproduction with exact failing values:
def test_run_failing_test_test_040_list_always_empty():
    from test_bank import test_040_list_always_empty

    test_040_list_always_empty.hypothesis.inner_test(
        lst=[0],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 230

# Test reproduction with exact failing values:
def test_run_failing_test_test_010_keys_values_equal():
    from test_bank import test_010_keys_values_equal

    test_010_keys_values_equal.hypothesis.inner_test(
        d={'': 0},
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 254

# Test reproduction with exact failing values:
def test_run_failing_test_test_042_dict_values_unique():
    from test_bank import test_042_dict_values_unique

    test_042_dict_values_unique.hypothesis.inner_test(
        d={'': 0, '0': 0},
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 265

# Test reproduction with exact failing values:
def test_run_failing_test_test_044_set_difference_empty():
    from test_bank import test_044_set_difference_empty

    test_044_set_difference_empty.hypothesis.inner_test(
        a={0},
        b=set(),
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 331

# Test reproduction with exact failing values:
def test_run_failing_test_test_017_dummy_inequality():
    from test_bank import test_017_dummy_inequality

    test_017_dummy_inequality.hypothesis.inner_test(
        obj=Dummy(0),
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 356

# Test reproduction with exact failing values:
def test_run_failing_test_test_053_point_x_positive():
    from test_bank import test_053_point_x_positive

    test_053_point_x_positive.hypothesis.inner_test(
        p=Point(0, 0),
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 500

# Test reproduction with exact failing values:
def test_run_failing_test_test_068_fail_on_42():
    from test_bank import test_068_fail_on_42

    test_068_fail_on_42.hypothesis.inner_test(
        x=42,
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 506

# Test reproduction with exact failing values:
def test_run_failing_test_test_069_fail_on_drawn():
    from test_bank import test_069_fail_on_drawn

    test_069_fail_on_drawn.hypothesis.inner_test(
        data=data(...),
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 512

# Test reproduction with exact failing values:
def test_run_failing_test_test_070_fail_on_empty():
    from test_bank import test_070_fail_on_empty

    test_070_fail_on_empty.hypothesis.inner_test(
        lst=[],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 526

# Test reproduction with exact failing values:
def test_run_failing_test_test_072_permutations():
    from test_bank import test_072_permutations

    test_072_permutations.hypothesis.inner_test(
        lst=[0, 0, 0],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 534

# Test reproduction with exact failing values:
def test_run_failing_test_test_073_permutation_fail():
    from test_bank import test_073_permutation_fail

    test_073_permutation_fail.hypothesis.inner_test(
        lst=[0, 0, 0],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 548

# Test reproduction with exact failing values:
def test_run_failing_test_test_075_bytes_fail():
    from test_bank import test_075_bytes_fail

    test_075_bytes_fail.hypothesis.inner_test(
        b=b'',
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 563

# Test reproduction with exact failing values:
def test_run_failing_test_test_078_booleans_fail():
    from test_bank import test_078_booleans_fail

    test_078_booleans_fail.hypothesis.inner_test(
        x=False,
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 574

# Test reproduction with exact failing values:
def test_run_failing_test_test_080_list_just_one_fail():
    from test_bank import test_080_list_just_one_fail

    test_080_list_just_one_fail.hypothesis.inner_test(
        lst=[1],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 584

# Test reproduction with exact failing values:
def test_run_failing_test_test_082_unicode_fail():
    from test_bank import test_082_unicode_fail

    test_082_unicode_fail.hypothesis.inner_test(
        s='',
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 594

# Test reproduction with exact failing values:
def test_run_failing_test_test_084_floats_fail():
    from test_bank import test_084_floats_fail

    test_084_floats_fail.hypothesis.inner_test(
        lst=[1.0],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 604

# Test reproduction with exact failing values:
def test_run_failing_test_test_086_dict_keys_fail():
    from test_bank import test_086_dict_keys_fail

    test_086_dict_keys_fail.hypothesis.inner_test(
        d={1: ''},
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 615

# Test reproduction with exact failing values:
def test_run_failing_test_test_088_list_of_lists_fail():
    from test_bank import test_088_list_of_lists_fail

    test_088_list_of_lists_fail.hypothesis.inner_test(
        lst=[[0]],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 625

# Test reproduction with exact failing values:
def test_run_failing_test_test_090_tuple_fail():
    from test_bank import test_090_tuple_fail

    test_090_tuple_fail.hypothesis.inner_test(
        t=(0, '', 1.0),
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 630

# Test reproduction with exact failing values:
def test_run_failing_test_test_108_point_origin():
    from test_bank import test_108_point_origin

    test_108_point_origin.hypothesis.inner_test(
        obj=Point(0, 1),
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 766

# Test reproduction with exact failing values:
def test_run_failing_test_run_state_machine():
    from test_bank import run_state_machine

    run_state_machine.hypothesis.inner_test(
        factory=test_bank.FailingStateMachine,
        data=data(...),
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 88

# Test reproduction with exact failing values:
def test_run_failing_test_test_002_subtraction_commutative():
    from test_bank import test_002_subtraction_commutative

    test_002_subtraction_commutative.hypothesis.inner_test(
        x=0,
        y=1,
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 126

# Test reproduction with exact failing values:
def test_run_failing_test_test_030_add_one_greater():
    from test_bank import test_030_add_one_greater

    test_030_add_one_greater.hypothesis.inner_test(
        x=9007199254740992.0,
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 140

# Test reproduction with exact failing values:
def test_run_failing_test_test_005_upper_is_lower():
    from test_bank import test_005_upper_is_lower

    test_005_upper_is_lower.hypothesis.inner_test(
        s='',
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 159

# Test reproduction with exact failing values:
def test_run_failing_test_test_032_string_is_upper():
    from test_bank import test_032_string_is_upper

    test_032_string_is_upper.hypothesis.inner_test(
        s='',
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 170

# Test reproduction with exact failing values:
def test_run_failing_test_test_034_ascii_only():
    from test_bank import test_034_ascii_only

    test_034_ascii_only.hypothesis.inner_test(
        s='\x80',
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 195

# Test reproduction with exact failing values:
def test_run_failing_test_test_009_sort_is_identity():
    from test_bank import test_009_sort_is_identity

    test_009_sort_is_identity.hypothesis.inner_test(
        lst=[0, -1],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 206

# Test reproduction with exact failing values:
def test_run_failing_test_test_037_list_unique():
    from test_bank import test_037_list_unique

    test_037_list_unique.hypothesis.inner_test(
        lst=[0, 0],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 222

# Test reproduction with exact failing values:
def test_run_failing_test_test_040_list_always_empty():
    from test_bank import test_040_list_always_empty

    test_040_list_always_empty.hypothesis.inner_test(
        lst=[0],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 230

# Test reproduction with exact failing values:
def test_run_failing_test_test_010_keys_values_equal():
    from test_bank import test_010_keys_values_equal

    test_010_keys_values_equal.hypothesis.inner_test(
        d={'': 0},
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 254

# Test reproduction with exact failing values:
def test_run_failing_test_test_042_dict_values_unique():
    from test_bank import test_042_dict_values_unique

    test_042_dict_values_unique.hypothesis.inner_test(
        d={'': 0, '0': 0},
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 265

# Test reproduction with exact failing values:
def test_run_failing_test_test_044_set_difference_empty():
    from test_bank import test_044_set_difference_empty

    test_044_set_difference_empty.hypothesis.inner_test(
        a={0},
        b=set(),
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 331

# Test reproduction with exact failing values:
def test_run_failing_test_test_017_dummy_inequality():
    from test_bank import test_017_dummy_inequality

    test_017_dummy_inequality.hypothesis.inner_test(
        obj=Dummy(0),
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 356

# Test reproduction with exact failing values:
def test_run_failing_test_test_053_point_x_positive():
    from test_bank import test_053_point_x_positive

    test_053_point_x_positive.hypothesis.inner_test(
        p=Point(0, 0),
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 500

# Test reproduction with exact failing values:
def test_run_failing_test_test_068_fail_on_42():
    from test_bank import test_068_fail_on_42

    test_068_fail_on_42.hypothesis.inner_test(
        x=42,
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 506

# Test reproduction with exact failing values:
def test_run_failing_test_test_069_fail_on_drawn():
    from test_bank import test_069_fail_on_drawn

    test_069_fail_on_drawn.hypothesis.inner_test(
        data=data(...),
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 512

# Test reproduction with exact failing values:
def test_run_failing_test_test_070_fail_on_empty():
    from test_bank import test_070_fail_on_empty

    test_070_fail_on_empty.hypothesis.inner_test(
        lst=[],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 526

# Test reproduction with exact failing values:
def test_run_failing_test_test_072_permutations():
    from test_bank import test_072_permutations

    test_072_permutations.hypothesis.inner_test(
        lst=[0, 0, 0],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 534

# Test reproduction with exact failing values:
def test_run_failing_test_test_073_permutation_fail():
    from test_bank import test_073_permutation_fail

    test_073_permutation_fail.hypothesis.inner_test(
        lst=[0, 0, 0],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 548

# Test reproduction with exact failing values:
def test_run_failing_test_test_075_bytes_fail():
    from test_bank import test_075_bytes_fail

    test_075_bytes_fail.hypothesis.inner_test(
        b=b'',
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 563

# Test reproduction with exact failing values:
def test_run_failing_test_test_078_booleans_fail():
    from test_bank import test_078_booleans_fail

    test_078_booleans_fail.hypothesis.inner_test(
        x=False,
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 574

# Test reproduction with exact failing values:
def test_run_failing_test_test_080_list_just_one_fail():
    from test_bank import test_080_list_just_one_fail

    test_080_list_just_one_fail.hypothesis.inner_test(
        lst=[1],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 584

# Test reproduction with exact failing values:
def test_run_failing_test_test_082_unicode_fail():
    from test_bank import test_082_unicode_fail

    test_082_unicode_fail.hypothesis.inner_test(
        s='',
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 594

# Test reproduction with exact failing values:
def test_run_failing_test_test_084_floats_fail():
    from test_bank import test_084_floats_fail

    test_084_floats_fail.hypothesis.inner_test(
        lst=[1.0],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 604

# Test reproduction with exact failing values:
def test_run_failing_test_test_086_dict_keys_fail():
    from test_bank import test_086_dict_keys_fail

    test_086_dict_keys_fail.hypothesis.inner_test(
        d={1: ''},
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 615

# Test reproduction with exact failing values:
def test_run_failing_test_test_088_list_of_lists_fail():
    from test_bank import test_088_list_of_lists_fail

    test_088_list_of_lists_fail.hypothesis.inner_test(
        lst=[[0]],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 625

# Test reproduction with exact failing values:
def test_run_failing_test_test_090_tuple_fail():
    from test_bank import test_090_tuple_fail

    test_090_tuple_fail.hypothesis.inner_test(
        t=(0, '', 1.0),
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 630

# Test reproduction with exact failing values:
def test_run_failing_test_test_108_point_origin():
    from test_bank import test_108_point_origin

    test_108_point_origin.hypothesis.inner_test(
        obj=Point(0, 1),
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 766

# Test reproduction with exact failing values:
def test_run_failing_test_run_state_machine():
    from test_bank import run_state_machine

    run_state_machine.hypothesis.inner_test(
        factory=test_bank.FailingStateMachine,
        data=data(...),
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 88

# Test reproduction with exact failing values:
def test_run_failing_test_test_002_subtraction_commutative():
    from test_bank import test_002_subtraction_commutative

    test_002_subtraction_commutative.hypothesis.inner_test(
        x=0,
        y=1,
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 126

# Test reproduction with exact failing values:
def test_run_failing_test_test_030_add_one_greater():
    from test_bank import test_030_add_one_greater

    test_030_add_one_greater.hypothesis.inner_test(
        x=9007199254740992.0,
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 140

# Test reproduction with exact failing values:
def test_run_failing_test_test_005_upper_is_lower():
    from test_bank import test_005_upper_is_lower

    test_005_upper_is_lower.hypothesis.inner_test(
        s='',
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 159

# Test reproduction with exact failing values:
def test_run_failing_test_test_032_string_is_upper():
    from test_bank import test_032_string_is_upper

    test_032_string_is_upper.hypothesis.inner_test(
        s='',
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 170

# Test reproduction with exact failing values:
def test_run_failing_test_test_034_ascii_only():
    from test_bank import test_034_ascii_only

    test_034_ascii_only.hypothesis.inner_test(
        s='\x80',
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 195

# Test reproduction with exact failing values:
def test_run_failing_test_test_009_sort_is_identity():
    from test_bank import test_009_sort_is_identity

    test_009_sort_is_identity.hypothesis.inner_test(
        lst=[0, -1],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 206

# Test reproduction with exact failing values:
def test_run_failing_test_test_037_list_unique():
    from test_bank import test_037_list_unique

    test_037_list_unique.hypothesis.inner_test(
        lst=[0, 0],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 222

# Test reproduction with exact failing values:
def test_run_failing_test_test_040_list_always_empty():
    from test_bank import test_040_list_always_empty

    test_040_list_always_empty.hypothesis.inner_test(
        lst=[0],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 230

# Test reproduction with exact failing values:
def test_run_failing_test_test_010_keys_values_equal():
    from test_bank import test_010_keys_values_equal

    test_010_keys_values_equal.hypothesis.inner_test(
        d={'': 0},
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 254

# Test reproduction with exact failing values:
def test_run_failing_test_test_042_dict_values_unique():
    from test_bank import test_042_dict_values_unique

    test_042_dict_values_unique.hypothesis.inner_test(
        d={'': 0, '0': 0},
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 265

# Test reproduction with exact failing values:
def test_run_failing_test_test_044_set_difference_empty():
    from test_bank import test_044_set_difference_empty

    test_044_set_difference_empty.hypothesis.inner_test(
        a={0},
        b=set(),
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 331

# Test reproduction with exact failing values:
def test_run_failing_test_test_017_dummy_inequality():
    from test_bank import test_017_dummy_inequality

    test_017_dummy_inequality.hypothesis.inner_test(
        obj=Dummy(0),
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 356

# Test reproduction with exact failing values:
def test_run_failing_test_test_053_point_x_positive():
    from test_bank import test_053_point_x_positive

    test_053_point_x_positive.hypothesis.inner_test(
        p=Point(0, 0),
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 500

# Test reproduction with exact failing values:
def test_run_failing_test_test_068_fail_on_42():
    from test_bank import test_068_fail_on_42

    test_068_fail_on_42.hypothesis.inner_test(
        x=42,
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 506

# Test reproduction with exact failing values:
def test_run_failing_test_test_069_fail_on_drawn():
    from test_bank import test_069_fail_on_drawn

    test_069_fail_on_drawn.hypothesis.inner_test(
        data=data(...),
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 512

# Test reproduction with exact failing values:
def test_run_failing_test_test_070_fail_on_empty():
    from test_bank import test_070_fail_on_empty

    test_070_fail_on_empty.hypothesis.inner_test(
        lst=[],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 526

# Test reproduction with exact failing values:
def test_run_failing_test_test_072_permutations():
    from test_bank import test_072_permutations

    test_072_permutations.hypothesis.inner_test(
        lst=[0, 0, 0],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 534

# Test reproduction with exact failing values:
def test_run_failing_test_test_073_permutation_fail():
    from test_bank import test_073_permutation_fail

    test_073_permutation_fail.hypothesis.inner_test(
        lst=[0, 0, 0],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 548

# Test reproduction with exact failing values:
def test_run_failing_test_test_075_bytes_fail():
    from test_bank import test_075_bytes_fail

    test_075_bytes_fail.hypothesis.inner_test(
        b=b'',
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 563

# Test reproduction with exact failing values:
def test_run_failing_test_test_078_booleans_fail():
    from test_bank import test_078_booleans_fail

    test_078_booleans_fail.hypothesis.inner_test(
        x=False,
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 574

# Test reproduction with exact failing values:
def test_run_failing_test_test_080_list_just_one_fail():
    from test_bank import test_080_list_just_one_fail

    test_080_list_just_one_fail.hypothesis.inner_test(
        lst=[1],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 584

# Test reproduction with exact failing values:
def test_run_failing_test_test_082_unicode_fail():
    from test_bank import test_082_unicode_fail

    test_082_unicode_fail.hypothesis.inner_test(
        s='',
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 594

# Test reproduction with exact failing values:
def test_run_failing_test_test_084_floats_fail():
    from test_bank import test_084_floats_fail

    test_084_floats_fail.hypothesis.inner_test(
        lst=[1.0],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 604

# Test reproduction with exact failing values:
def test_run_failing_test_test_086_dict_keys_fail():
    from test_bank import test_086_dict_keys_fail

    test_086_dict_keys_fail.hypothesis.inner_test(
        d={1: ''},
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 615

# Test reproduction with exact failing values:
def test_run_failing_test_test_088_list_of_lists_fail():
    from test_bank import test_088_list_of_lists_fail

    test_088_list_of_lists_fail.hypothesis.inner_test(
        lst=[[0]],
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 625

# Test reproduction with exact failing values:
def test_run_failing_test_test_090_tuple_fail():
    from test_bank import test_090_tuple_fail

    test_090_tuple_fail.hypothesis.inner_test(
        t=(0, '', 1.0),
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 630

# Test reproduction with exact failing values:
def test_run_failing_test_test_108_point_origin():
    from test_bank import test_108_point_origin

    test_108_point_origin.hypothesis.inner_test(
        obj=Point(0, 1),
    )

# Failing test extracted from Hypothesis

# Failure occurred in: test_bank.py
# Line number: 766

# Test reproduction with exact failing values:
def test_run_failing_test_run_state_machine():
    from test_bank import run_state_machine

    run_state_machine.hypothesis.inner_test(
        factory=test_bank.FailingStateMachine,
        data=data(...),
    )

