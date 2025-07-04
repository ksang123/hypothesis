from hypothesis import given, strategies as st

class MyPair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

@st.composite
def complex_pair(draw):
    x = draw(st.integers(min_value=-10, max_value=10))
    y = draw(st.integers(min_value=-10, max_value=10))
    z = draw(st.integers(min_value=-10, max_value=10))
    i = draw(st.integers(min_value=-10, max_value=10))
    j = draw(st.integers(min_value=-10, max_value=10))
    k = MyPair(x, y)
    k = MyPair(k, z)
    k = MyPair(k, i)
    k = MyPair(k, j)
    return k

@st.composite
def my_pair(draw):
    i = draw(st.integers(min_value=0, max_value=10))
    j = draw(st.integers(min_value=0, max_value=10))
    return MyPair(i, j)

@st.composite
def pair_same_ints(draw):
    i = draw(st.integers(min_value=-5, max_value=5))
    return i, i

@st.composite
def triple_boolean_flags(draw):
    return (
        draw(st.booleans()),
        draw(st.booleans()),
        draw(st.booleans()),
    )

@st.composite
def ascii_pal_string(draw):
    half = draw(
        st.text(
            min_size=1,
            max_size=3,
            alphabet=st.characters(blacklist_categories=("Cs", "Cc", "Zs", "Zl", "Zp")),
        )
    )
    return half + half[::-1]

@st.composite
def dict_int_to_mod3(draw):
    keys = draw(st.lists(st.integers(min_value=0, max_value=3), min_size=1, max_size=3))
    return {k: k % 3 for k in keys}

@st.composite
def sorted_float_pair(draw):
    a = draw(st.floats(min_value=-10, max_value=10, allow_nan=False, allow_infinity=False))
    b = draw(st.floats(min_value=-10, max_value=10, allow_nan=False, allow_infinity=False))
    return tuple(sorted((a, b)))

@given(complex_pair())
def test_my_complex_pair(pair):
    a, b = pair.x, pair.y
    assert a == b

@given(my_pair())
def test_my_pair(pair):
    a, b = pair.x, pair.y
    assert a == b

@given(pair_same_ints())
def test_pair_elements_differ(pair):
    a, b = pair
    assert a != b

@given(triple_boolean_flags())
def test_no_true_flags(flags):
    assert not any(flags)

@given(ascii_pal_string())
def test_palindrome_not_pal(s):
    assert s[::-1] != s

@given(dict_int_to_mod3())
def test_dict_value_not_mod3(d):
    assert any(v == k % 3 + 1 for k, v in d.items())

@given(sorted_float_pair())
def test_pair_unsorted(p):
    assert p[0] > p[1]


"""
im putting here tests without a custom strategy
to understand how it will work with default strategies
"""
@given(st.integers(), st.integers())
def test_integer_is_even(n, m):
    assert m + n % 10 != 0

@given(st.integers(min_value=1, max_value=10))
def test_positive_int_negative(x):
    assert x < 0

@given(st.text(min_size=1, max_size=5))
def test_non_empty_string_empty(s):
    assert s == ""

@given(st.floats(min_value=-3, max_value=3, allow_nan=False, allow_infinity=False))
def test_float_square_negative(f):
    assert f * f < 0

@given(st.lists(st.integers(), min_size=2, max_size=4))
def test_list_palindromic(lst):
    assert lst == lst[::-1]

@given(st.dictionaries(st.text(min_size=1, max_size=2), st.integers(), min_size=1, max_size=3))
def test_keys_match_values(d):
    assert all(str(v) == k for k, v in d.items())
