import pytest


def test_dummy_test_always_passes():
    assert True


def test_dummy_test_always_fails():
    assert False

def test_dummy_test_always_fails2():
    assert False, 'assert error message'


def test_dummy_test_always_fails3():
    raise Exception('exception message')


def test_dummy_test_always_fails4():
    raise KeyError('keyerror exception message')


def test_dummy_test_always_fails5():
    pytest.fail()


def test_dummy_test_always_fails6():
    pytest.fail("pytest fail message")

#
@pytest.mark.skip()
def test_dummy_test_always_skip():
    assert False
