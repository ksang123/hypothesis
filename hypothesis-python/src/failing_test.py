# Failing tests extracted from Hypothesis

from RBTreesTest import (
    test_is_bst_functional,
)

from RBtrees import (
    RBTreeFunctional,
)

def test_is_bst_functional(tree):
    if tree:
        wrapped = RBTree()
        wrapped.root = tree
        assert is_bst(wrapped)

# Failure occurred in: RBTreesTest.py
# Line number: 75
def test_run_failing_test_test_is_bst_functional():
    test_is_bst_functional.hypothesis.inner_test(
        tree=<RBtrees.RBTreeFunctional object at 0x0000022D923ACF80>,
    )

