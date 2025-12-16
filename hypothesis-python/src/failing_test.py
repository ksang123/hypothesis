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
	depth=0
	max_depth=6
	if depth >= max_depth or False:
	    return None
	tree_value = 0
	tree_left = inner_rb_functional_tree(depth=depth + 1, max_depth=max_depth)
	tree_right = inner_rb_functional_tree(depth=depth + 1, max_depth=max_depth)
	tree_node = RBTreeFunctional(tree_value, Color.BLACK, tree_left, tree_right)
	tree = tree_node
	test_is_bst_functional.hypothesis.inner_test(
		tree=tree,
	)

