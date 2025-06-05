import hypothesis
from hypothesis import given, strategies as st, settings, example
from hypothesis.stateful import RuleBasedStateMachine, rule, precondition, run_state_machine_as_test
from hypothesis import statistics
# from hypothesis import settings, Verbosity

i = 0
@given(st.integers(), st.integers())
@example(1, 1)
@settings(verbosity=hypothesis.Verbosity.debug)
def test_addition_commutativity(x, y):
    global i
    i = i + 1
    # print(i)
    assert x + y == y + x

class test:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        print(x, y)

@given(st.builds(test, st.integers()))
def test1(obj):
    assert 1==1

j = 0
class StatefulMachine(RuleBasedStateMachine):
    def __init__(self):
        super().__init__()
        global j
        j = j + 1
        # print(j)
        self.x = 0
        self.add_c = 0
        self.mult_c = 0

    @rule(x=st.integers())
    def add(self, x):
        old = self.x
        self.x += x
        self.add_c += 1
        assert self.x - x == old
        # print(f"Add: {self.add_c}")

    @rule(y=st.integers().filter(lambda x: x != 0))
    @precondition(lambda self: True)  # Some precondition
    def mult(self, y):
        old = self.x
        self.x *= y
        self.mult_c += 1
        assert self.x // y == old
        # print(f"Mult: {self.mult_c}")

def test_stateful_machine():
    run_state_machine_as_test(
        StatefulMachine,
        settings=settings(verbosity=hypothesis.Verbosity.debug)
    )
# import hypothesis
# from hypothesis import given, strategies as st, settings
# from hypothesis.stateful import RuleBasedStateMachine, rule, precondition
#
#
# class Tester:
#     def __init__(self):
#         self.counter = 0
#
#     @settings(verbosity=hypothesis.Verbosity.verbose)
#     @given(st.integers(), st.integers())
#     def test_addition_commutativity(self, x, y):
#         self.counter += 1
#         print(self.counter)
#         assert x + y == y + x
#
#     @given(st.integers())
#     def test_fail(self, x):
#         assert x == 1
#
#
#
# t = Tester()
# t.test_addition_commutativity()
#
# class StatefulMachine(RuleBasedStateMachine):
#     def __init__(self):
#         self.x = 0
#         super().__init__()
#         self.add_c = 0
#         self.mult_c = 0
#
#
#
#     @rule(x = st.integers()) # Can hold params we want generated
#     def add(self, x):
#         old = self.x
#         self.x += x
#         self.add_c += 1
#         assert self.x - x == old
#         print(f"Add: {self.add_c}")
#
#
#     # @settings()
#     @rule(y = st.integers().filter(lambda x: x != 0))
#     @precondition(lambda x: True) # Some precondition
#     def mult(self, y):
#         old = self.x
#         self.x *= y
#         self.mult_c += 1
#         assert self.x // y == old
#         print(f"Mult: {self.mult_c}")
#
# test = settings(verbosity=hypothesis.Verbosity.verbose)(hypothesis.stateful.run_state_machine_as_test)
# test(StatefulMachine)
