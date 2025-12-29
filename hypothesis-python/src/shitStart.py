from hypothesis import given, strategies as st
@st.composite
def shitStuff(draw):
    return draw(st.integers(min_value=0, max_value=4))

