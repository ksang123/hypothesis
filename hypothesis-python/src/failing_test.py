# Failing tests extracted from Hypothesis

from test_bank import (
    Dummy,
    Point,
    Tree,
    test_002_subtraction_commutative,
    test_005_upper_is_lower,
    test_009_sort_is_identity,
    test_010_keys_values_equal,
    test_017_dummy_inequality,
    test_030_add_one_greater,
    test_032_string_is_upper,
    test_034_ascii_only,
    test_037_list_unique,
    test_040_list_always_empty,
    test_042_dict_values_unique,
    test_044_set_difference_empty,
    test_053_point_x_positive,
    test_061_tree_value_positive,
    test_068_fail_on_42,
    test_070_fail_on_empty,
    test_072_permutations,
    test_073_permutation_fail,
    test_075_bytes_fail,
    test_078_booleans_fail,
    test_080_list_just_one_fail,
    test_082_unicode_fail,
    test_084_floats_fail,
    test_086_dict_keys_fail,
    test_088_list_of_lists_fail,
    test_090_tuple_fail,
    test_092_nested_list_fail,
    test_108_point_origin,
)

# Failure occurred in: test_bank.py
# Line number: 89
def test_run_failing_test_test_002_subtraction_commutative():
    test_002_subtraction_commutative.hypothesis.inner_test(
        x=6,
        y=8,
    )

# Failure occurred in: test_bank.py
# Line number: 127
def test_run_failing_test_test_030_add_one_greater():
    test_030_add_one_greater.hypothesis.inner_test(
        x=9007199254740992.0,
    )

# Failure occurred in: test_bank.py
# Line number: 141
def test_run_failing_test_test_005_upper_is_lower():
    test_005_upper_is_lower.hypothesis.inner_test(
        s='',
    )

# Failure occurred in: test_bank.py
# Line number: 160
def test_run_failing_test_test_032_string_is_upper():
    test_032_string_is_upper.hypothesis.inner_test(
        s='',
    )

# Failure occurred in: test_bank.py
# Line number: 171
def test_run_failing_test_test_034_ascii_only():
    test_034_ascii_only.hypothesis.inner_test(
        s='\x80',
    )

# Failure occurred in: test_bank.py
# Line number: 196
def test_run_failing_test_test_009_sort_is_identity():
    test_009_sort_is_identity.hypothesis.inner_test(
        lst=[0, -1],
    )

# Failure occurred in: test_bank.py
# Line number: 207
def test_run_failing_test_test_037_list_unique():
    test_037_list_unique.hypothesis.inner_test(
        lst=[0, 0],
    )

# Failure occurred in: test_bank.py
# Line number: 223
def test_run_failing_test_test_040_list_always_empty():
    test_040_list_always_empty.hypothesis.inner_test(
        lst=[0],
    )

# Failure occurred in: test_bank.py
# Line number: 231
def test_run_failing_test_test_010_keys_values_equal():
    test_010_keys_values_equal.hypothesis.inner_test(
        d={'': 0},
    )

# Failure occurred in: test_bank.py
# Line number: 255
def test_run_failing_test_test_042_dict_values_unique():
    test_042_dict_values_unique.hypothesis.inner_test(
        d={'': 0, '0': 0},
    )

# Failure occurred in: test_bank.py
# Line number: 266
def test_run_failing_test_test_044_set_difference_empty():
    test_044_set_difference_empty.hypothesis.inner_test(
        a={0},
        b=set(),
    )

# Failure occurred in: test_bank.py
# Line number: 332
def test_run_failing_test_test_017_dummy_inequality():
    test_017_dummy_inequality.hypothesis.inner_test(
        obj=Dummy(0),
    )

# Failure occurred in: test_bank.py
# Line number: 357
def test_run_failing_test_test_053_point_x_positive():
    test_053_point_x_positive.hypothesis.inner_test(
        p=Point(0, 0),
    )

# Failure occurred in: test_bank.py
# Line number: 424
def test_run_failing_test_test_061_tree_value_positive():
    test_061_tree_value_positive.hypothesis.inner_test(
        t=Tree(-1, []),
    )

# Failure occurred in: test_bank.py
# Line number: 442
def test_run_failing_test_test_092_nested_list_fail():
    test_092_nested_list_fail.hypothesis.inner_test(
        lst=[0],
    )

# Failure occurred in: test_bank.py
# Line number: 501
def test_run_failing_test_test_068_fail_on_42():
    test_068_fail_on_42.hypothesis.inner_test(
        x=42,
    )

# Failure occurred in: test_bank.py
# Line number: 507
def test_run_failing_test_test_070_fail_on_empty():
    test_070_fail_on_empty.hypothesis.inner_test(
        lst=[],
    )

# Failure occurred in: test_bank.py
# Line number: 521
def test_run_failing_test_test_072_permutations():
    test_072_permutations.hypothesis.inner_test(
        lst=[0, 0, 0],
    )

# Failure occurred in: test_bank.py
# Line number: 529
def test_run_failing_test_test_073_permutation_fail():
    test_073_permutation_fail.hypothesis.inner_test(
        lst=[0, 0, 0],
    )

# Failure occurred in: test_bank.py
# Line number: 543
def test_run_failing_test_test_075_bytes_fail():
    test_075_bytes_fail.hypothesis.inner_test(
        b=b'',
    )

# Failure occurred in: test_bank.py
# Line number: 558
def test_run_failing_test_test_078_booleans_fail():
    test_078_booleans_fail.hypothesis.inner_test(
        x=False,
    )

# Failure occurred in: test_bank.py
# Line number: 569
def test_run_failing_test_test_080_list_just_one_fail():
    test_080_list_just_one_fail.hypothesis.inner_test(
        lst=[1],
    )

# Failure occurred in: test_bank.py
# Line number: 579
def test_run_failing_test_test_082_unicode_fail():
    test_082_unicode_fail.hypothesis.inner_test(
        s='',
    )

# Failure occurred in: test_bank.py
# Line number: 589
def test_run_failing_test_test_084_floats_fail():
    test_084_floats_fail.hypothesis.inner_test(
        lst=[1.0],
    )

# Failure occurred in: test_bank.py
# Line number: 599
def test_run_failing_test_test_086_dict_keys_fail():
    test_086_dict_keys_fail.hypothesis.inner_test(
        d={1: ''},
    )

# Failure occurred in: test_bank.py
# Line number: 610
def test_run_failing_test_test_088_list_of_lists_fail():
    test_088_list_of_lists_fail.hypothesis.inner_test(
        lst=[[0]],
    )

# Failure occurred in: test_bank.py
# Line number: 620
def test_run_failing_test_test_090_tuple_fail():
    test_090_tuple_fail.hypothesis.inner_test(
        t=(0, '', 1.0),
    )

# Failure occurred in: test_bank.py
# Line number: 625
def test_run_failing_test_test_108_point_origin():
    test_108_point_origin.hypothesis.inner_test(
        obj=Point(0, 1),
    )

