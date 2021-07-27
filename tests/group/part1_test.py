import pytest
import part1

def test_dummy_test_always_passes():
    assert True


def test_dummy_test_always_fails():
    with open('part1_test.py') as f:
        raise Exception(f.read())
    assert True
