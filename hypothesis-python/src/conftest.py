from hypothesis.internal.unit_tests import UnitTestGenerator

def pytest_sessionfinish(session, exitstatus):
    # TODO: maybe pass a path here
    # TODO: maybe find a better place to put this
    UnitTestGenerator().render()