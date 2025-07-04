# Failing tests extracted from Hypothesis

from simple_tests import (
    MyPair,
    test_dict_value_not_mod3,
    test_integer_is_even,
    test_my_pair,
    test_no_true_flags,
    test_pair_elements_differ,
    test_pair_unsorted,
    test_palindrome_not_pal,
    test_positive_int_negative,
)

# Failure occurred in: simple_tests.py
# Line number: 52
def test_run_failing_test_test_my_pair():
    test_my_pair.hypothesis.inner_test(
        pair=<simple_tests.MyPair object at 0x000002A3FB6BD910>,
    )

# Failure occurred in: simple_tests.py
# Line number: 57
def test_run_failing_test_test_pair_elements_differ():
    test_pair_elements_differ.hypothesis.inner_test(
        pair=(0, 0),
    )

# Failure occurred in: simple_tests.py
# Line number: 61
def test_run_failing_test_test_no_true_flags():
    test_no_true_flags.hypothesis.inner_test(
        flags=(False, False, True),
    )

# Failure occurred in: simple_tests.py
# Line number: 65
def test_run_failing_test_test_palindrome_not_pal():
    test_palindrome_not_pal.hypothesis.inner_test(
        s='00',
    )

# Failure occurred in: simple_tests.py
# Line number: 69
def test_run_failing_test_test_dict_value_not_mod3():
    test_dict_value_not_mod3.hypothesis.inner_test(
        d={0: 0},
    )

# Failure occurred in: simple_tests.py
# Line number: 73
def test_run_failing_test_test_pair_unsorted():
    test_pair_unsorted.hypothesis.inner_test(
        p=(0.0, 0.0),
    )

# Failure occurred in: simple_tests.py
# Line number: 82
def test_run_failing_test_test_integer_is_even():
    test_integer_is_even.hypothesis.inner_test(
        n=1,
    )

# Failure occurred in: simple_tests.py
# Line number: 86
def test_run_failing_test_test_positive_int_negative():
    test_positive_int_negative.hypothesis.inner_test(
        x=1,
    )

