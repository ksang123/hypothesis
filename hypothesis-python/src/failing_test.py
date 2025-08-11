# Failing tests extracted from Hypothesis

from simple_tests import (
    test_positive_int_negative,
)

# Failure occurred in: simple_tests.py
# Line number: 125
def test_run_failing_test_test_positive_int_negative():
    x = 1
    test_positive_int_negative.hypothesis.inner_test(
        x=x,
    )

