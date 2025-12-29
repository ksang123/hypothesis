# Failing tests extracted from Hypothesis

from RBTreesTest import (
    test_is_bst_functional,
)

from RBtrees import (
    RBTreeFunctional,
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

