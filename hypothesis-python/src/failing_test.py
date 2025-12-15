# Failing tests extracted from Hypothesis

from RBTreesTest import (
    test_is_bst_imperative,
)

from RBtrees import (
    RBTree,
)

# Failure occurred in: RBTreesTest.py
# Line number: 60
def test_run_failing_test_test_is_bst_imperative():
    if current_depth >= max_depth or high - low <= 1 or False:
        return None
    tree_value = 1
    tree_left = None
    tree_right = None
    tree_node = RBTreeImperative(tree_value, Color.BLACK, parent)
    tree_node.left = tree_left
    tree_node.right = tree_right
    if tree_left:
        tree_left.parent = tree_node
    if tree_right:
        tree_right.parent = tree_node
    if parent is None and current_depth == 0:
        tree = RBTree()
        tree.root = tree_node
        return tree
    else:
        return tree_node
    test_is_bst_imperative.hypothesis.inner_test(
        tree=tree,
    )

