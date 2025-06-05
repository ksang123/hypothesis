# Failing test extracted from Hypothesis

# Failure occurred in: C:\Users\danir\PycharmProjects\hypothesis\hypothesis-python\src\test_bank.py
# Line number: 88

# Original test function implementation:
def test_002_subtraction_commutative(x, y):
    assert x - y == y - x

# Test reproduction with exact failing values:
def test_run_failing_test():
    test_002_subtraction_commutative(
        x=0,
        y=1,
    )

