from hypothesis import given, strategies as st
# from shitStart import shitStuff
import shitStart
import random
from RBtrees import *

@st.composite
def rb_functional_tree(draw, depth=0, max_depth=6):
    if depth >= max_depth or draw(st.booleans()):
        return None

    value = draw(st.integers(min_value=0, max_value=100))
    # shit = draw(shitStart.shitStuff())
    left = draw(rb_functional_tree(depth=depth + 1, max_depth=max_depth))
    right = draw(rb_functional_tree(depth=depth + 1, max_depth=max_depth))

    node = RBTreeFunctional(value, Color.BLACK, left, right)
    return node


@st.composite
def rb_imperative_tree(draw, max_depth=6, current_depth=0, low=0, high=100, parent=None):
    if current_depth >= max_depth or high - low <= 1 or draw(st.booleans()):
        return None

    value = draw(st.integers(min_value=low + 1, max_value=high - 1))

    left = draw(rb_imperative_tree(
        max_depth=max_depth,
        current_depth=current_depth + 1,
        low=low,
        high=value,
        parent=None
    ))

    right = draw(rb_imperative_tree(
        max_depth=max_depth,
        current_depth=current_depth + 1,
        low=value,
        high=high,
        parent=None
    ))

    node = RBTreeImperative(value, Color.BLACK, parent)
    node.left = left
    node.right = right

    if left:
        left.parent = node
    if right:
        right.parent = node

    if parent is None and current_depth == 0:
        tree = RBTree()
        tree.root = node
        return tree
    else:
        return node

@given(rb_imperative_tree())
def test_is_bst_imperative(tree):
    if tree is not None:
        assert not is_bst(tree)

@given(rb_functional_tree())
def test_is_bst_functional(tree):
    if tree:
        wrapped = RBTree()
        wrapped.root = tree
        assert is_bst(wrapped)
