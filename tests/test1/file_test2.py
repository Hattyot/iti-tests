import pytest


@pytest.mark.skip_testfile()
def skip_testfile(previous_results: dict):
    return previous_results['file_test.py']['totalCount'] != previous_results['file_test.py']['passedCount']


import file


def test_dummy_test_always_passes():
    raise Exception()


def test_dummy_test_always_fails():
    a = 1 + 1
    b = a + 1
    c = b + 1
    assert c == 100

def test_dummy_test_always_fails2():
    a = 1 + 1
    b = a + 1
    c = b + 1
    assert c == 100, 'assert error message'


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