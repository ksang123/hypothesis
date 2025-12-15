# Failing tests extracted from Hypothesis

from RBTreesTest import (
    test_is_bst_functional,
)

from RBtrees import (
    RBTreeFunctional,
)

# Failure occurred in: RBTreesTest.py
# Line number: 67
def test_run_failing_test_test_is_bst_functional():
    if depth >= max_depth or False:
        return None
    tree_value = 0
    tree_left = <RBtrees.RBTreeFunctional object at 0x00000158C7511430>
    tree_right = None
    tree_node = RBTreeFunctional(tree_value, Color.BLACK, tree_left, tree_right)
    tree = tree_node
    test_is_bst_functional.hypothesis.inner_test(
        tree=tree,
    )

