"""
Test Bank: 100 +  stateful & advanced Hypothesis-powered tests.
Each group contains both passing and failing tests.
Features used: @given, @example, @settings, assume, filter, composite, data(),
builds, recursive, sampled_from, just, one_of, shared, etc.
"""
from typing import Optional, List, Tuple

from hypothesis import (
    given, example, assume, settings, seed, note,
    strategies as st, Verbosity,
)
from hypothesis.stateful import (
    RuleBasedStateMachine, rule, invariant, Bundle,
    run_state_machine_as_test,
)
import math
import unicodedata
import string

# ---------------------------------------------------------------------------
# 0.  Tiny helper classes used throughout
# ---------------------------------------------------------------------------
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return isinstance(other, Point) and self.x == other.x and self.y == other.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


class Dummy:
    def __init__(self, value):
        self.value = value


class Box:
    def __init__(self, point):
        self.point = point

    def __eq__(self, other):
        return isinstance(other, Box) and self.point == other.point


class Counter:
    def __init__(self):
        self.count = 0

    def inc(self):
        self.count += 1


class Tree:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children or []

    def __eq__(self, other):
        return (
            isinstance(other, Tree)
            and self.value == other.value
            and self.children == other.children
        )


class Greeter:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}!"


# ---------------------------------------------------------------------------
# 1.  Math Tests
# ---------------------------------------------------------------------------
@example(x=0, y=0)
@given(st.integers(), st.integers())
def test_001_addition_commutative(x, y):
    assert x + y == y + x

@example(x=6, y=8)
@given(st.integers(), st.integers())
def test_002_subtraction_commutative(x, y):
    assert x - y == y - x


@given(x=st.integers(), y=st.integers(), z=st.integers())
def test_003_multiplication_associative(x, y, z):
    assert (x * y) * z == x * (y * z)


@given(st.integers(min_value=1, max_value=100), st.integers(min_value=1, max_value=100))
def test_025_division_not_commutative(x, y):
    assume(x != y)
    assert (x / y) != (y / x)


@given(st.integers())
def test_026_sqrt_square(x):
    assert math.isclose(math.sqrt(x * x), abs(x))


@given(st.floats(min_value=0.1, max_value=1000), st.floats(min_value=0.1, max_value=1000))
def test_027_log_product(x, y):
    assert math.isclose(math.log(x * y), math.log(x) + math.log(y))


@given(st.integers())
def test_028_divide_self(x):
    assume(x != 0)
    assert x / x == 1


@given(st.integers(), st.integers())
def test_029_gcd_positive(x, y):
    assert math.gcd(x, y) >= 0


@given(st.floats(allow_infinity=True, allow_nan=False))
def test_030_add_one_greater(x):
    assume(not math.isinf(x))
    assert x + 1 > x


# ---------------------------------------------------------------------------
# 2.  String Tests
# ---------------------------------------------------------------------------
@example(s="ΑβΓδ")                             # Greek unicode
@given(st.text())
def test_004_reverse_twice_identity(s):
    assert s[::-1][::-1] == s


@given(st.text())
def test_005_upper_is_lower(s):
    assert s.upper().islower()


@given(st.text())
def test_006_string_contains_itself(s):
    assume(s)
    assert s in s


@given(st.text().filter(lambda s: len(s) > 0))
def test_031_palindrome_reverse(s):
    if s == s[::-1]:
        assert s == s[::-1]
    else:
        assert s != s[::-1]


@given(st.text())
def test_032_string_is_upper(s):
    assert s.isupper()


@example(s1="foo", s2="バー")                     # Latin + Japanese
@given(st.text(), st.text())
def test_033_concat_length(s1, s2):
    assert len(s1 + s2) == len(s1) + len(s2)


@given(st.text())
def test_034_ascii_only(s):
    assert all(ord(c) < 128 for c in s)


@given(st.text())
def test_035_normalize_nfc(s):
    assert unicodedata.normalize("NFC", s) == unicodedata.normalize("NFC", s)


# ---------------------------------------------------------------------------
# 3.  List / Sequence Tests
# ---------------------------------------------------------------------------
@example(lst=[3, 1, 2])
@given(st.lists(st.integers()))
def test_007_sort_idempotent(lst):
    assert sorted(sorted(lst)) == sorted(lst)


@example(lst=[5, 4, 3, 2, 1])
@given(st.lists(st.integers()))
def test_008_sort_preserves_length(lst):
    assert len(sorted(lst)) == len(lst)


@given(st.lists(st.integers()))
def test_009_sort_is_identity(lst):
    assert sorted(lst) == lst


@example(lst=[1, 2, 3])
@given(st.lists(st.integers()))
def test_036_reverse_twice(lst):
    assert lst[::-1][::-1] == lst


@given(st.lists(st.integers()))
def test_037_list_unique(lst):
    assert len(lst) == len(set(lst))


@example(lst=[-1, 0, 1])
@given(st.lists(st.integers(), min_size=3, max_size=3))
def test_038_sum_repeated(lst):
    assert sum(lst) == lst[0] + lst[1] + lst[2]


@given(st.lists(st.integers()))
def test_039_sorted(lst):
    assert all(sorted(lst)[i] <= sorted(lst)[i + 1] for i in range(len(sorted(lst)) - 1))


@given(st.lists(st.integers(), min_size=1))
def test_040_list_always_empty(lst):
    assert len(lst) == 0


# ---------------------------------------------------------------------------
# 4.  Dict / Set Tests
# ---------------------------------------------------------------------------
@given(st.dictionaries(st.text(), st.integers()))
def test_010_keys_values_equal(d):
    assert set(d.keys()) == set(d.values())


@given(st.sets(st.integers()))
def test_011_set_idempotent(s):
    assert set(set(s)) == set(s)


@given(a=st.sets(st.integers()), b=st.sets(st.integers()))
def test_012_set_union_contains_both(a, b):
    for x in a:
        assert x in a | b
    for y in b:
        assert y in a | b


@example(d={"a": 1, "b": 2})
@given(st.dictionaries(st.text(), st.integers()))
def test_041_dict_keys_unique(d):
    assert len(d.keys()) == len(set(d.keys()))


@given(st.dictionaries(st.text(), st.integers()))
def test_042_dict_values_unique(d):
    assert len(d.values()) == len(set(d.values()))


@example(a={1, 2, 3}, b={3, 4})
@given(st.sets(st.integers()), st.sets(st.integers()))
def test_043_set_intersection_subset(a, b):
    assert a & b <= a and a & b <= b


@given(st.sets(st.integers()), st.sets(st.integers()))
def test_044_set_difference_empty(a, b):
    assert a - b == set()


@example(keys=["a", "a", "b"])
@given(st.lists(st.sampled_from(["a", "b", "c"])))
def test_045_dict_from_keys(keys):
    d = dict.fromkeys(keys, 1)
    assert all(k in d for k in keys)


# ---------------------------------------------------------------------------
# 5.  Edge-case Tests
# ---------------------------------------------------------------------------
@given(st.integers())
def test_013_division_by_zero(x):
    assume(x != 0)
    assert 1 / x != 0


@given(st.lists(st.integers(), min_size=0, max_size=0))
def test_014_empty_list_sum(lst):
    assert sum(lst) == 0


@given(st.lists(st.integers().filter(lambda x: x > 0)))
def test_015_all_positive(lst):
    assert all(x > 0 for x in lst)


@given(st.just(float("nan")))
def test_046_nan_not_equal(x):
    assert x != x


@given(st.just(float("inf")))
def test_047_inf_plus_one(x):
    assert x + 1 == x


@given(st.just(-0.0))
def test_048_negative_zero(x):
    assert x == 0.0


@given(st.just(""))
def test_049_empty_string_palindrome(s):
    assert s == s[::-1]


@settings(max_examples=5)
@given(st.lists(st.integers(), min_size=1000, max_size=1000))
def test_050_large_list_sum(lst):
    assert isinstance(sum(lst), int)


# ---------------------------------------------------------------------------
# 6.  Custom Classes / Objects
# ---------------------------------------------------------------------------
@example(obj=Dummy(123))
@given(st.builds(Dummy, st.integers()))
def test_016_dummy_equality(obj):
    assert obj == obj


@given(st.builds(Dummy, st.integers()))
def test_017_dummy_inequality(obj):
    assert obj != obj


@given(st.builds(Dummy, st.integers()))
def test_018_dummy_value_is_int(obj):
    assume(isinstance(obj.value, int))
    assert isinstance(obj.value, int)


@example(a=Point(1, 2), b=Point(3, 4))
@given(
    st.builds(Point, st.integers(), st.integers()),
    st.builds(Point, st.integers(), st.integers()),
)
def test_051_point_add_commutative(a, b):
    assert a + b == b + a


@given(st.builds(Point, st.integers(), st.integers()))
def test_052_point_reflexive(p):
    assert p == p


@given(st.builds(Point, st.integers(), st.integers()))
def test_053_point_x_positive(p):
    assert p.x > 0


@given(st.builds(Box, st.builds(Point, st.integers(), st.integers())))
def test_054_box_point_equality(box):
    assert box == box


@given(st.builds(Counter))
def test_055_counter_always_zero(c):
    assert c.count == 0


# ---------------------------------------------------------------------------
# 7.  Composite / Data / Shared etc.
# ---------------------------------------------------------------------------
@st.composite
def palindromes(draw):
    half = draw(st.text())
    return half + half[::-1]


@given(palindromes())
def test_056_palindrome_property(s):
    assert s == s[::-1]


@given(st.data())
def test_057_data_dependent(data):
    n = data.draw(st.integers(min_value=1, max_value=10))
    lst = data.draw(st.lists(st.integers(), min_size=n, max_size=n))
    assert len(lst) == n


@given(st.shared(st.integers(), key="k"), st.shared(st.integers(), key="k"))
def test_058_shared_value(x, y):
    assert x == y


@given(
    st.one_of(
        st.builds(Dummy, st.integers()),
        st.builds(Point, st.integers(), st.integers()),
    )
)
def test_059_one_of_custom(obj):
    assert hasattr(obj, "__eq__")


# ---------------------------------------------------------------------------
# 8.  Recursive Structures
# ---------------------------------------------------------------------------
tree_strategy = st.recursive(
    st.builds(Tree, st.integers()),
    lambda children: st.builds(Tree, st.integers(), st.lists(children, max_size=2)),
    max_leaves=5,
)

@example(t=Tree(1, [Tree(2), Tree(3)]))
@given(tree_strategy)
def test_060_tree_structure(t):
    assert isinstance(t, Tree)


@example(t=Tree(-1, []))
@given(tree_strategy)
def test_061_tree_value_positive(t):
    assert t.value > 0


nested_list = st.recursive(
    st.integers(),
    lambda children: st.lists(children),
    max_leaves=5,
)

@example(lst=[1, [2, [3]]])
@given(nested_list)
def test_091_nested_list_type(lst):
    assert isinstance(lst, (int, list))


@example(lst=[0])
@given(nested_list)
def test_092_nested_list_fail(lst):
    assert lst == 0


custom_tree = st.recursive(
    st.builds(Tree, st.integers()),
    lambda children: st.builds(Tree, st.integers(), st.lists(children, max_size=2)),
    max_leaves=3,
)

@example(t=Tree(10, [Tree(11)]))
@given(custom_tree)
def test_105_recursive_custom_tree(t):
    assert isinstance(t, Tree)


# ---------------------------------------------------------------------------
# 9.  Register-type strategy examples
# ---------------------------------------------------------------------------
from hypothesis.strategies import register_type_strategy

register_type_strategy(Dummy, st.builds(Dummy, st.integers()))
register_type_strategy(Point, st.builds(Point, st.integers(), st.integers()))


@given(st.from_type(Dummy))
def test_062_from_type_dummy(obj):
    assert isinstance(obj, Dummy)


@given(st.sampled_from([True, False]))
def test_063_sampled_from_bool(b):
    assert b in [True, False]


@given(st.just(None))
def test_064_just_none(x):
    assert x is None


@settings(suppress_health_check=[])  # No-op
@given(st.integers())
def test_065_settings_noop(x):
    assert isinstance(x, int)


@seed(1234)
@given(st.integers())
def test_066_seeded(x):
    assert isinstance(x, int)


@given(st.integers())
def test_067_note(x):
    note(f"Value: {x}")
    assert isinstance(x, int)


@given(st.integers())
def test_068_fail_on_42(x):
    assert x != 42


@given(st.lists(st.integers()))
def test_070_fail_on_empty(lst):
    assume(len(lst) == 0)
    assert False


@given(st.tuples(st.integers(), st.text()))
def test_071_tuple_unpack(t):
    x, s = t
    assert isinstance(x, int) and isinstance(s, str)


@given(st.lists(st.integers(), min_size=3, max_size=3))
def test_072_permutations(lst):
    from itertools import permutations

    perms = list(permutations(lst))
    assert lst in perms


@given(st.lists(st.integers(), min_size=3, max_size=3))
def test_073_permutation_fail(lst):
    from itertools import permutations

    perms = list(permutations(lst))
    assert [0, 0, 0] in perms


@given(st.binary())
def test_074_bytes_decode_encode(b):
    try:
        s = b.decode("utf-8", errors="ignore")
        assert isinstance(s, str)
    except Exception:
        assert True


@given(st.binary())
def test_075_bytes_fail(b):
    assert b == b"abc"


@given(st.none())
def test_076_none_not_true(x):
    assert not x


@given(st.booleans())
def test_077_booleans(x):
    assert x in [True, False]


@given(st.booleans())
def test_078_booleans_fail(x):
    assert x is True


@example(lst=[1, 1, 1])
@given(st.lists(st.just(1)))
def test_079_list_just_one(lst):
    assert all(x == 1 for x in lst)


@given(st.lists(st.just(1)))
def test_080_list_just_one_fail(lst):
    assert all(x == 2 for x in lst)


@given(st.text())
def test_081_unicode_normalization(s):
    assert unicodedata.normalize("NFC", s) == unicodedata.normalize("NFC", s)


@given(st.text())
def test_082_unicode_fail(s):
    assert s == "abc"


@given(st.lists(st.floats(allow_nan=False, allow_infinity=False)))
def test_083_floats_finite(lst):
    assert all(math.isfinite(x) for x in lst)


@given(st.lists(st.floats()))
def test_084_floats_fail(lst):
    assert all(x == 0.0 for x in lst)


@given(st.dictionaries(st.integers(), st.text()))
def test_085_dict_int_keys(d):
    assert all(isinstance(k, int) for k in d.keys())


@given(st.dictionaries(st.integers(), st.text()))
def test_086_dict_keys_fail(d):
    assert all(k == 0 for k in d.keys())


@example(lst=[[1], [], [2, 3]])
@given(st.lists(st.lists(st.integers())))
def test_087_list_of_lists(lst):
    assert all(isinstance(x, list) for x in lst)


@given(st.lists(st.lists(st.integers())))
def test_088_list_of_lists_fail(lst):
    assert all(x == [] for x in lst)


@given(st.tuples(st.integers(), st.text(), st.floats()))
def test_089_tuple_types(t):
    assert isinstance(t[0], int) and isinstance(t[1], str) and isinstance(t[2], float)


@given(st.tuples(st.integers(), st.text(), st.floats()))
def test_090_tuple_fail(t):
    assert t == (0, "", 0.0)


@given(st.builds(Point, st.integers(), st.integers()))
def test_108_point_origin(obj):
    assert obj.x == 0 and obj.y == 0


@st.composite
def custom_point(draw):
    x = draw(st.integers())
    y = draw(st.integers())
    return Point(x, y)


@given(custom_point())
def test_101_custom_point(obj):
    assert isinstance(obj, Point)


@st.composite
def custom_box(draw):
    pt = draw(custom_point())
    return Box(pt)


@given(custom_box())
def test_102_custom_box(obj):
    assert isinstance(obj, Box)


@given(st.data())
def test_103_data_custom_class(data):
    x = data.draw(st.integers())
    y = data.draw(st.integers())
    obj = Point(x, y)
    assert obj.x == x and obj.y == y


@given(
    st.shared(st.builds(Point, st.integers(), st.integers()), key="pt"),
    st.shared(st.builds(Point, st.integers(), st.integers()), key="pt"),
)
def test_104_shared_custom_class(a, b):
    assert a == b


@st.composite
def positive_point(draw):
    x = draw(st.integers().filter(lambda x: x > 0))
    y = draw(st.integers().filter(lambda y: y > 0))
    return Point(x, y)


@given(positive_point())
def test_107_positive_point(obj):
    assert obj.x > 0 and obj.y > 0


@st.composite
def greeter_with_name(draw):
    name = draw(st.text())
    return Greeter(name)


@given(greeter_with_name())
def test_109_greeter_with_name(obj):
    assert obj.greet().startswith("Hello, ")


# ---------------------------------------------------------------------------
# 10.  Stateful Specifications
# ---------------------------------------------------------------------------
class CounterStateMachine(RuleBasedStateMachine):
    def __init__(self):
        super().__init__()
        self.counter = 0

    @rule()
    def increment(self):
        self.counter += 1

    @rule()
    def decrement(self):
        self.counter -= 1

    @invariant()
    def counter_is_int(self):
        assert isinstance(self.counter, int)


class Stack:
    def __init__(self):
        self._data = []

    def push(self, x):
        self._data.append(x)

    def pop(self):
        if self._data:
            return self._data.pop()
        return None

    def top(self):
        if self._data:
            return self._data[-1]
        return None

    def __len__(self):
        return len(self._data)


class StackStateMachine(RuleBasedStateMachine):
    def __init__(self):
        super().__init__()
        self.stack = Stack()

    @rule(x=st.integers())
    def push(self, x):
        self.stack.push(x)

    @rule()
    def pop(self):
        self.stack.pop()

    @invariant()
    def length_nonnegative(self):
        assert len(self.stack) >= 0


class FailingStateMachine(RuleBasedStateMachine):
    def __init__(self):
        super().__init__()
        self.value = 0

    @rule()
    def inc(self):
        self.value += 1

    @invariant()
    def always_zero(self):
        assert self.value == 0


class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        return False


class BankAccountStateMachine(RuleBasedStateMachine):
    def __init__(self):
        super().__init__()
        self.account = BankAccount()

    @rule(amount=st.integers(min_value=1, max_value=1000))
    def deposit(self, amount):
        self.account.deposit(amount)

    @rule(amount=st.integers(min_value=1, max_value=1000))
    def withdraw(self, amount):
        self.account.withdraw(amount)

    @invariant()
    def balance_nonnegative(self):
        assert self.account.balance >= 0


class ListStateMachine(RuleBasedStateMachine):
    Items = Bundle("items")

    def __init__(self):
        super().__init__()
        self.lst = []

    @rule(target=Items, x=st.integers())
    def add(self, x):
        self.lst.append(x)
        return x

    @rule(x=Items)
    def remove(self, x):
        if x in self.lst:
            self.lst.remove(x)

    @invariant()
    def all_ints(self):
        assert all(isinstance(x, int) for x in self.lst)


class FailingBankStateMachine(RuleBasedStateMachine):
    def __init__(self):
        super().__init__()
        self.account = BankAccount()

    @rule(amount=st.integers(min_value=1, max_value=1000))
    def deposit(self, amount):
        self.account.deposit(amount)

    @rule(amount=st.integers(min_value=1, max_value=1000))
    def withdraw(self, amount):
        self.account.withdraw(amount)

    @invariant()
    def always_zero_balance(self):
        assert self.account.balance == 0


# Manual wrappers to guarantee collection in any pytest configuration
# def test__run_counter_state_machine():
#     run_state_machine_as_test(CounterStateMachine)
#
#
# def test__run_stack_state_machine():
#     run_state_machine_as_test(StackStateMachine)
#
#
# def test__run_failing_state_machine():
#     run_state_machine_as_test(FailingStateMachine)
#
#
# def test__run_bank_account_state_machine():
#     run_state_machine_as_test(BankAccountStateMachine)
#
#
# def test__run_list_state_machine():
#     run_state_machine_as_test(ListStateMachine)
#
#
# def test__run_failing_bank_state_machine():
#     run_state_machine_as_test(FailingBankStateMachine)

# ====================== more complex tests that is hard to do with @example! ====================

# =======================================================================
# 111 – 115 : “ridiculously-manual” examples
# =======================================================================

# ---------------------------------------------------------------------------
# 111.  Balanced-BST check with gigantic, hand-wired trees
# ---------------------------------------------------------------------------

class BSTNode:
    __slots__ = ("val", "left", "right")

    def __init__(self, val: int):
        self.val = val
        self.left: Optional["BSTNode"] = None
        self.right: Optional["BSTNode"] = None

    def __repr__(self):
        return f"Node({self.val})"


def is_balanced(node: Optional[BSTNode]) -> bool:
    def h(n):
        return 0 if n is None else 1 + max(h(n.left), h(n.right))

    if node is None:
        return True
    return (
        abs(h(node.left) - h(node.right)) <= 1
        and is_balanced(node.left)
        and is_balanced(node.right)
    )


# ----- five brutally explicit balanced trees --------------------------------
BST_EX1 = BSTNode(8)
BST_EX1.left = BSTNode(4)
BST_EX1.right = BSTNode(12)
BST_EX1.left.left = BSTNode(2)
BST_EX1.left.right = BSTNode(6)
BST_EX1.right.left = BSTNode(10)
BST_EX1.right.right = BSTNode(14)

BST_EX2 = BSTNode(16)
BST_EX2.left = BSTNode(8)
BST_EX2.right = BSTNode(24)
BST_EX2.left.left = BSTNode(4)
BST_EX2.left.right = BSTNode(12)
BST_EX2.right.left = BSTNode(20)
BST_EX2.right.right = BSTNode(28)
BST_EX2.left.left.left = BSTNode(2)
BST_EX2.left.left.right = BSTNode(6)
BST_EX2.left.right.left = BSTNode(10)
BST_EX2.left.right.right = BSTNode(14)
BST_EX2.right.left.left = BSTNode(18)
BST_EX2.right.left.right = BSTNode(22)
BST_EX2.right.right.left = BSTNode(26)
BST_EX2.right.right.right = BSTNode(30)

# a complete tree, depth-5
BST_EX3 = BSTNode(32)
BST_EX3.left = BSTNode(16)
BST_EX3.right = BSTNode(48)
BST_EX3.left.left = BSTNode(8)
BST_EX3.left.right = BSTNode(24)
BST_EX3.right.left = BSTNode(40)
BST_EX3.right.right = BSTNode(56)
BST_EX3.left.left.left = BSTNode(4)
BST_EX3.left.left.right = BSTNode(12)
BST_EX3.left.right.left = BSTNode(20)
BST_EX3.left.right.right = BSTNode(28)
BST_EX3.right.left.left = BSTNode(36)
BST_EX3.right.left.right = BSTNode(44)
BST_EX3.right.right.left = BSTNode(52)
BST_EX3.right.right.right = BSTNode(60)

# depth-6 left-biased but balanced
BST_EX4 = BSTNode(100)
BST_EX4.left = BSTNode(50)
BST_EX4.right = BSTNode(150)
BST_EX4.left.left = BSTNode(25)
BST_EX4.left.right = BSTNode(75)
BST_EX4.left.left.left = BSTNode(12)
BST_EX4.left.left.right = BSTNode(37)
BST_EX4.left.right.left = BSTNode(62)
BST_EX4.left.right.right = BSTNode(87)
BST_EX4.right.left = BSTNode(125)
BST_EX4.right.right = BSTNode(175)
BST_EX4.right.left.left = BSTNode(112)
BST_EX4.right.left.right = BSTNode(137)
BST_EX4.right.right.left = BSTNode(162)
BST_EX4.right.right.right = BSTNode(187)

# depth-7 symmetric monster
BST_EX5 = BSTNode(256)
BST_EX5.left = BSTNode(128)
BST_EX5.right = BSTNode(384)
BST_EX5.left.left = BSTNode(64)
BST_EX5.left.right = BSTNode(192)
BST_EX5.right.left = BSTNode(320)
BST_EX5.right.right = BSTNode(448)
BST_EX5.left.left.left = BSTNode(32)
BST_EX5.left.left.right = BSTNode(96)
BST_EX5.left.right.left = BSTNode(160)
BST_EX5.left.right.right = BSTNode(224)
BST_EX5.right.left.left = BSTNode(288)
BST_EX5.right.left.right = BSTNode(352)
BST_EX5.right.right.left = BSTNode(416)
BST_EX5.right.right.right = BSTNode(480)

@example(root=BST_EX1)
@example(root=BST_EX2)
@example(root=BST_EX3)
@example(root=BST_EX4)
@example(root=BST_EX5)
@given(
    root=st.builds(
        lambda sorted_vals: (
            (lambda sv: (
                (lambda mid: (lambda node: node)(BSTNode(sv[mid])))
                (len(sv) // 2)
            ))(sorted_vals)
        ),
        st.lists(
            st.integers(min_value=0, max_value=500),
            unique=True,
            min_size=1,
            max_size=31,
        ).map(sorted),
    )
)
def test_111_balanced_bst(root):
    assert is_balanced(root)


# ---------------------------------------------------------------------------
# 112.  DAG topological order —  handwritten edge sets
# ---------------------------------------------------------------------------

def is_valid_topology(order: List[int], edges: List[Tuple[int, int]]) -> bool:
    pos = {v: i for i, v in enumerate(order)}
    return all(pos[u] < pos[v] for u, v in edges)

def trivial_tsort(n: int) -> List[int]:
    return list(range(n))

_edges_full_5  = [(i, j) for i in range(5)  for j in range(i + 1, 5)]
_edges_full_10 = [(i, j) for i in range(10) for j in range(i + 1, 10)]

@example(n=4,  edges=[(0,1),(1,2),(2,3),(0,3)])
@example(n=5,  edges=_edges_full_5)
@example(n=6,  edges=[(0,2),(0,3),(1,3),(2,4),(3,4),(4,5)])
@example(n=10, edges=[(0,9)] + [(i,i+1) for i in range(9)])
@example(n=13, edges=[(0,6),(0,7),(1,8),(2,9),(3,10),(4,11),(5,12)])
@given(
    n     = st.integers(min_value=2, max_value=8),
    edges = st.lists(
        st.tuples(
            st.integers(min_value=0, max_value=7),
            st.integers(min_value=0, max_value=7),
        ).filter(lambda e: e[0] < e[1]),
        min_size=1,
        max_size=15,
        unique=True,
    ),
)
def test_112_manual_dag(n, edges):
    assume(all(0 <= u < n and 0 <= v < n for u, v in edges))
    order = trivial_tsort(n)
    assert is_valid_topology(order, edges)



# ---------------------------------------------------------------------------
# 113.  Explicit 9×9 solved Sudoku boards
# ---------------------------------------------------------------------------

def is_valid_sudoku(board: List[List[int]]) -> bool:
    rows_ok = all(sorted(row) == list(range(1, 10)) for row in board)
    cols_ok = all(
        sorted(board[r][c] for r in range(9)) == list(range(1, 10)) for c in range(9)
    )
    blocks_ok = True
    for br in range(0, 9, 3):
        for bc in range(0, 9, 3):
            block = [
                board[r][c] for r in range(br, br + 3) for c in range(bc, bc + 3)
            ]
            if sorted(block) != list(range(1, 10)):
                blocks_ok = False
    return rows_ok and cols_ok and blocks_ok


S1 = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [4, 5, 6, 7, 8, 9, 1, 2, 3],
    [7, 8, 9, 1, 2, 3, 4, 5, 6],
    [2, 3, 4, 5, 6, 7, 8, 9, 1],
    [5, 6, 7, 8, 9, 1, 2, 3, 4],
    [8, 9, 1, 2, 3, 4, 5, 6, 7],
    [3, 4, 5, 6, 7, 8, 9, 1, 2],
    [6, 7, 8, 9, 1, 2, 3, 4, 5],
    [9, 1, 2, 3, 4, 5, 6, 7, 8],
]
S2 = [row[::-1] for row in S1]
S3 = [[(cell % 9) + 1 for cell in row] for row in S1]
S4 = [row[3:] + row[:3] for row in S1]
S5 = S3[::-1]

@example(board=S1)
@example(board=S2)
@example(board=S3)
@example(board=S4)
@example(board=S5)
@given(st.just(S1))  # strategy is pointless – the agony is the @examples
def test_113_manual_sudoku(board):
    assert is_valid_sudoku(board)


# ---------------------------------------------------------------------------
# 114.  Hand-typed, huge balanced-parentheses strings
# ---------------------------------------------------------------------------

def is_balanced_parens(s: str) -> bool:
    bal = 0
    for ch in s:
        if ch == "(":
            bal += 1
        elif ch == ")":
            bal -= 1
            if bal < 0:
                return False
    return bal == 0


P1 = "((()))((()))((()))((()))((()))"
P2 = "(" * 50 + ")" * 50
P3 = "(()())" * 34
P4 = "(((((())))))" * 20
P5 = ""  # edge case

@example(s=P1)
@example(s=P2)
@example(s=P3)
@example(s=P4)
@example(s=P5)
@given(st.just(P2))
def test_114_manual_parens(s):
    assert is_balanced_parens(s)


# ---------------------------------------------------------------------------
# 115.  Expression-tree evaluation vs. Python eval – giant literal trees
# ---------------------------------------------------------------------------

class ExprNode:
    __slots__ = ("op", "left", "right", "value")

    def __init__(
        self,
        op: Optional[str] = None,
        left: Optional["ExprNode"] = None,
        right: Optional["ExprNode"] = None,
        value: Optional[int] = None,
    ):
        self.op, self.left, self.right, self.value = op, left, right, value

    def __repr__(self):
        return (
            str(self.value)
            if self.op is None
            else f"({self.left!r}{self.op}{self.right!r})"
        )


def eval_tree(node: ExprNode) -> int:
    if node.op is None:
        return node.value
    l, r = eval_tree(node.left), eval_tree(node.right)
    return {"+" : l + r, "-" : l - r, "*" : l * r}[node.op]


def tree_to_infix(node: ExprNode) -> str:
    return str(node.value) if node.op is None else f"({tree_to_infix(node.left)}{node.op}{tree_to_infix(node.right)})"


# ----- five monstrous literal trees ----------------------------------------
T1 = ExprNode(
    "+",
    ExprNode("+", ExprNode(value=1), ExprNode(value=1)),
    ExprNode("+", ExprNode(value=1), ExprNode(value=1)),
)

T2 = ExprNode(
    "*",
    ExprNode(
        "+",
        ExprNode("+", ExprNode(value=2), ExprNode(value=3)),
        ExprNode(value=4),
    ),
    ExprNode(value=5),
)

T3 = ExprNode(
    "-",
    ExprNode(
        "*",
        ExprNode(
            "+",
            ExprNode(value=6),
            ExprNode(value=7),
        ),
        ExprNode(value=8),
    ),
    ExprNode(value=9),
)

# ridiculously deep, right-leaning chain of pluses (10 nodes)
T4 = (
    ExprNode(
        "+",
        ExprNode(value=1),
        ExprNode(
            "+",
            ExprNode(value=1),
            ExprNode(
                "+",
                ExprNode(value=1),
                ExprNode(
                    "+",
                    ExprNode(value=1),
                    ExprNode(
                        "+",
                        ExprNode(value=1),
                        ExprNode(
                            "+",
                            ExprNode(value=1),
                            ExprNode(
                                "+",
                                ExprNode(value=1),
                                ExprNode(
                                    "+",
                                    ExprNode(value=1),
                                    ExprNode(value=1),
                                ),
                            ),
                        ),
                    ),
                ),
            ),
        ),
    )
)

# symmetric multiplication tree
T5 = ExprNode(
    "*",
    ExprNode("*", ExprNode(value=2), ExprNode(value=2)),
    ExprNode("*", ExprNode(value=3), ExprNode(value=3)),
)

@example(tree=T1)
@example(tree=T2)
@example(tree=T3)
@example(tree=T4)
@example(tree=T5)
@given(st.just(T4))
def test_115_manual_expr_eval(tree: ExprNode):
    assert eval(tree_to_infix(tree)) == eval_tree(tree)
