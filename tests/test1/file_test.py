import pytest


def test_dummy_test_always_passes():
    assert True


def test_dummy_test_always_fails():
    assert False

#
@pytest.mark.skip()
def test_dummy_test_always_skip():
    assert False
