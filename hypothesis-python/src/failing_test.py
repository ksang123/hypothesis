# Failing tests extracted from Hypothesis

from simple_tests import (
    MyPair,
    test_dict_value_not_mod3,
    test_float_square_negative,
    test_integer_is_even,
    test_keys_match_values,
    test_list_palindromic,
    test_my_pair,
    test_no_true_flags,
    test_non_empty_string_empty,
    test_pair_elements_differ,
    test_pair_unsorted,
    test_palindrome_not_pal,
    test_positive_int_negative,
)

# Failure occurred in: simple_tests.py
# Line number: 52
def test_run_failing_test_test_my_pair():
    pair_i = 0
    pair_j = 1
    pair = MyPair(pair_i, pair_j)
    test_my_pair.hypothesis.inner_test(
        pair=pair,
    )

# Failure occurred in: simple_tests.py
# Line number: 57
def test_run_failing_test_test_pair_elements_differ():
    pair_i = 0
    pair = (pair_i, pair_i)
    test_pair_elements_differ.hypothesis.inner_test(
        pair=pair,
    )

# Failure occurred in: simple_tests.py
# Line number: 61
def test_run_failing_test_test_no_true_flags():
    flags = (False, False, True)
    test_no_true_flags.hypothesis.inner_test(
        flags=flags,
    )

# Failure occurred in: simple_tests.py
# Line number: 65
def test_run_failing_test_test_palindrome_not_pal():
    s_half = '0'
    s = s_half + s_half[::-1]
    test_palindrome_not_pal.hypothesis.inner_test(
        s=s,
    )

# Failure occurred in: simple_tests.py
# Line number: 69
def test_run_failing_test_test_dict_value_not_mod3():
    d_keys = [0]
    d = {k: k % 3 for k in d_keys}
    test_dict_value_not_mod3.hypothesis.inner_test(
        d=d,
    )

# Failure occurred in: simple_tests.py
# Line number: 73
def test_run_failing_test_test_pair_unsorted():
    p_a = 0.0
    p_b = 0.0
    p = tuple(sorted((p_a, p_b)))
    test_pair_unsorted.hypothesis.inner_test(
        p=p,
    )

# Failure occurred in: simple_tests.py
# Line number: 82
def test_run_failing_test_test_integer_is_even():
    n = 0
    m = 0
    test_integer_is_even.hypothesis.inner_test(
        n=n,
        m=m,
    )

# Failure occurred in: simple_tests.py
# Line number: 86
def test_run_failing_test_test_positive_int_negative():
    x = 1
    test_positive_int_negative.hypothesis.inner_test(
        x=x,
    )

# Failure occurred in: simple_tests.py
# Line number: 90
def test_run_failing_test_test_non_empty_string_empty():
    s = '0'
    test_non_empty_string_empty.hypothesis.inner_test(
        s=s,
    )

# Failure occurred in: simple_tests.py
# Line number: 94
def test_run_failing_test_test_float_square_negative():
    f = 0.0
    test_float_square_negative.hypothesis.inner_test(
        f=f,
    )

# Failure occurred in: simple_tests.py
# Line number: 98
def test_run_failing_test_test_list_palindromic():
    lst = [0, 1]
    test_list_palindromic.hypothesis.inner_test(
        lst=lst,
    )

# Failure occurred in: simple_tests.py
# Line number: 102
def test_run_failing_test_test_keys_match_values():
    d = {'1': 0}
    test_keys_match_values.hypothesis.inner_test(
        d=d,
    )

