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
# Line number: 63
def test_run_failing_test_test_is_bst_imperative():
	max_depth=6
	current_depth=0
	low=0
	high=100
	parent=None
	if current_depth >= max_depth or high - low <= 1 or False:
		tree = None
	tree_value = 1
	tree_left = None
#++++++++++++++++++++++++++++++++++++++++++++++++++
	if current_depth >= max_depth or high - low <= 1 or True:
		tree_composite_strat3 = None
#The next thing is null because it is out of bounds
	tree_composite_strat3_value = None
#The next thing is null because it is out of bounds
	tree_composite_strat3_left = None
#The next thing is null because it is out of bounds
	tree_composite_strat3_right = None
	tree_composite_strat3_node = RBTreeImperative(tree_composite_strat3_value, Color.BLACK, parent)
	tree_composite_strat3_node.left = tree_composite_strat3_left
	tree_composite_strat3_node.right = tree_composite_strat3_right
	if tree_composite_strat3_left:
		tree_composite_strat3_left.parent = tree_composite_strat3_node
	if tree_composite_strat3_right:
		tree_composite_strat3_right.parent = tree_composite_strat3_node
	if parent is None and current_depth == 0:
		tree_composite_strat3_tree = RBTree()
		tree_composite_strat3_tree.root = tree_composite_strat3_node
		tree_composite_strat3 = tree_composite_strat3_tree
	else:
		tree_composite_strat3 = tree_composite_strat3_node
#--------------------------------------------------
	tree_right = tree_composite_strat3
	tree_node = RBTreeImperative(tree_value, Color.BLACK, parent)
	tree_node.left = tree_left
	tree_node.right = tree_right
	if tree_left:
		tree_left.parent = tree_node
	if tree_right:
		tree_right.parent = tree_node
	if parent is None and current_depth == 0:
		tree_tree = RBTree()
		tree_tree.root = tree_node
		tree = tree_tree
	else:
		tree = tree_node
	test_is_bst_imperative.hypothesis.inner_test(
		tree=tree,
	)

# Failure occurred in: RBTreesTest.py
# Line number: 70
def test_run_failing_test_test_is_bst_functional():
	depth=0
	max_depth=6
	if depth >= max_depth or False:
		tree = None
	tree_value = 0
#++++++++++++++++++++++++++++++++++++++++++++++++++
	if depth >= max_depth or False:
		tree_composite_strat2 = None
	tree_composite_strat2_value = 0
#++++++++++++++++++++++++++++++++++++++++++++++++++
	if depth >= max_depth or True:
		tree_composite_strat2_composite_strat2 = None
#The next thing is null because it is out of bounds
	tree_composite_strat2_composite_strat2_value = None
#The next thing is null because it is out of bounds
	tree_composite_strat2_composite_strat2_left = None
#The next thing is null because it is out of bounds
	tree_composite_strat2_composite_strat2_right = None
	tree_composite_strat2_composite_strat2_node = RBTreeFunctional(tree_composite_strat2_composite_strat2_value, Color.BLACK, tree_composite_strat2_composite_strat2_left, tree_composite_strat2_composite_strat2_right)
	tree_composite_strat2_composite_strat2 = tree_composite_strat2_composite_strat2_node
#--------------------------------------------------
	tree_composite_strat2_left = tree_composite_strat2_composite_strat2
#++++++++++++++++++++++++++++++++++++++++++++++++++
	if depth >= max_depth or True:
		tree_composite_strat2_composite_strat3 = None
#The next thing is null because it is out of bounds
	tree_composite_strat2_composite_strat3_value = None
#The next thing is null because it is out of bounds
	tree_composite_strat2_composite_strat3_left = None
#The next thing is null because it is out of bounds
	tree_composite_strat2_composite_strat3_right = None
	tree_composite_strat2_composite_strat3_node = RBTreeFunctional(tree_composite_strat2_composite_strat3_value, Color.BLACK, tree_composite_strat2_composite_strat3_left, tree_composite_strat2_composite_strat3_right)
	tree_composite_strat2_composite_strat3 = tree_composite_strat2_composite_strat3_node
#--------------------------------------------------
	tree_composite_strat2_right = tree_composite_strat2_composite_strat3
	tree_composite_strat2_node = RBTreeFunctional(tree_composite_strat2_value, Color.BLACK, tree_composite_strat2_left, tree_composite_strat2_right)
	tree_composite_strat2 = tree_composite_strat2_node
#--------------------------------------------------
	tree_left = tree_composite_strat2
#++++++++++++++++++++++++++++++++++++++++++++++++++
	if depth >= max_depth or True:
		tree_composite_strat3 = None
#The next thing is null because it is out of bounds
	tree_composite_strat3_value = None
#The next thing is null because it is out of bounds
	tree_composite_strat3_left = None
#The next thing is null because it is out of bounds
	tree_composite_strat3_right = None
	tree_composite_strat3_node = RBTreeFunctional(tree_composite_strat3_value, Color.BLACK, tree_composite_strat3_left, tree_composite_strat3_right)
	tree_composite_strat3 = tree_composite_strat3_node
#--------------------------------------------------
	tree_right = tree_composite_strat3
	tree_node = RBTreeFunctional(tree_value, Color.BLACK, tree_left, tree_right)
	tree = tree_node
	test_is_bst_functional.hypothesis.inner_test(
		tree=tree,
	)

