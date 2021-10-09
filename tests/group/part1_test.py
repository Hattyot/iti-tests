import pytest
import part1

def test_dummy_test_always_passes():
    assert "Hello World!!!" == \
           "Hello world!"


def test_dummy_test_always_fails():
    assert [*range(1, 1000)] == \
           [*range(1, 500), 1,2,3, *range(500, 1000)]
