# Failing tests extracted from Hypothesis

from simple_tests import (
    MyPair,
    test_dict_value_not_mod3,
    test_float_square_negative,
    test_imperative_pair,
    test_integer_is_even,
    test_keys_match_values,
    test_list_palindromic,
    test_my_complex_pair,
    test_my_complex_pair_prefixer_test,
    test_my_pair,
    test_no_true_flags,
    test_non_empty_string_empty,
    test_pair_elements_differ,
    test_pair_unsorted,
    test_palindrome_not_pal,
    test_positive_int_negative,
)

# Failure occurred in: simple_tests.py
# Line number: 76
def test_run_failing_test_test_my_complex_pair_prefixer_test():
    pair1_x = 0
    pair1_y = 0
    pair1_z = 0
    pair1_i = 0
    pair1_j = 0
    pair1_k = MyPair(pair1_x, pair1_y)
    pair1_k = MyPair(pair1_k, pair1_z)
    pair1_k = MyPair(pair1_k, pair1_i)
    pair1_k = MyPair(pair1_k, pair1_j)
    pair1 = pair1_k
    pair2_x = 0
    pair2_y = 0
    pair2_z = 0
    pair2_i = 0
    pair2_j = 0
    pair2_k = MyPair(pair2_x, pair2_y)
    pair2_k = MyPair(pair2_k, pair2_z)
    pair2_k = MyPair(pair2_k, pair2_i)
    pair2_k = MyPair(pair2_k, pair2_j)
    pair2 = pair2_k
    test_my_complex_pair_prefixer_test.hypothesis.inner_test(
        pair1=pair1,
        pair2=pair2,
    )

# Failure occurred in: simple_tests.py
# Line number: 81
def test_run_failing_test_test_imperative_pair():
    pair_p = MyPair()
    pair_p2 = MyPair()
    pair_p.x = 0
    pair_p.y = pair_p2
    pair_p.y.x = 0
    pair_p.y.y = 0
    pair = pair_p
    test_imperative_pair.hypothesis.inner_test(
        pair=pair,
    )

# Failure occurred in: simple_tests.py
# Line number: 86
def test_run_failing_test_test_my_complex_pair():
    pair_x = 0
    pair_y = 0
    pair_z = 0
    pair_i = 0
    pair_j = 0
    pair_k = MyPair(pair_x, pair_y)
    pair_k = MyPair(pair_k, pair_z)
    pair_k = MyPair(pair_k, pair_i)
    pair_k = MyPair(pair_k, pair_j)
    pair = pair_k
    test_my_complex_pair.hypothesis.inner_test(
        pair=pair,
    )

# Failure occurred in: simple_tests.py
# Line number: 91
def test_run_failing_test_test_my_pair():
    pair_i = 0
    pair_j = 1
    pair = MyPair(pair_i, pair_j)
    test_my_pair.hypothesis.inner_test(
        pair=pair,
    )

# Failure occurred in: simple_tests.py
# Line number: 96
def test_run_failing_test_test_pair_elements_differ():
    pair_i = 0
    pair = (pair_i, pair_i)
    test_pair_elements_differ.hypothesis.inner_test(
        pair=pair,
    )

# Failure occurred in: simple_tests.py
# Line number: 100
def test_run_failing_test_test_no_true_flags():
    flags = (False, False, True)
    test_no_true_flags.hypothesis.inner_test(
        flags=flags,
    )

# Failure occurred in: simple_tests.py
# Line number: 104
def test_run_failing_test_test_palindrome_not_pal():
    s_half = '0'
    s = s_half + s_half[::-1]
    test_palindrome_not_pal.hypothesis.inner_test(
        s=s,
    )

# Failure occurred in: simple_tests.py
# Line number: 108
def test_run_failing_test_test_dict_value_not_mod3():
    d_keys = [0]
    d = {k: k % 3 for k in d_keys}
    test_dict_value_not_mod3.hypothesis.inner_test(
        d=d,
    )

# Failure occurred in: simple_tests.py
# Line number: 112
def test_run_failing_test_test_pair_unsorted():
    p_a = 0.0
    p_b = 0.0
    p = tuple(sorted((p_a, p_b)))
    test_pair_unsorted.hypothesis.inner_test(
        p=p,
    )

# Failure occurred in: simple_tests.py
# Line number: 121
def test_run_failing_test_test_integer_is_even():
    n = 0
    m = 0
    test_integer_is_even.hypothesis.inner_test(
        n=n,
        m=m,
    )

# Failure occurred in: simple_tests.py
# Line number: 125
def test_run_failing_test_test_positive_int_negative():
    x = 1
    test_positive_int_negative.hypothesis.inner_test(
        x=x,
    )

# Failure occurred in: simple_tests.py
# Line number: 129
def test_run_failing_test_test_non_empty_string_empty():
    s = '0'
    test_non_empty_string_empty.hypothesis.inner_test(
        s=s,
    )

# Failure occurred in: simple_tests.py
# Line number: 133
def test_run_failing_test_test_float_square_negative():
    f = 0.0
    test_float_square_negative.hypothesis.inner_test(
        f=f,
    )

# Failure occurred in: simple_tests.py
# Line number: 137
def test_run_failing_test_test_list_palindromic():
    lst = [0, 1]
    test_list_palindromic.hypothesis.inner_test(
        lst=lst,
    )

# Failure occurred in: simple_tests.py
# Line number: 141
def test_run_failing_test_test_keys_match_values():
    d = {'1': 0}
    test_keys_match_values.hypothesis.inner_test(
        d=d,
    )

