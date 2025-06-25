# Failing tests extracted from Hypothesis

from RBTreesTest import (
    test_is_bst_functional,
    test_is_bst_imperative,
)

from RBtrees import (
    RBTree,
    RBTreeFunctional,
)

# Failure occurred in: RBTreesTest.py
# Line number: 60
def test_run_failing_test_test_is_bst_imperative():
    test_is_bst_imperative.hypothesis.inner_test(
        tree=<RBtrees.RBTree object at 0x000001C0CDAC4E90>,
    )

# Failure occurred in: RBTreesTest.py
# Line number: 67
def test_run_failing_test_test_is_bst_functional():
    test_is_bst_functional.hypothesis.inner_test(
        tree=<RBtrees.RBTreeFunctional object at 0x000001C0CD9CEE70>,
    )

