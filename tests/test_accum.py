import sys
import os
import pytest

# Add the directory containing the `stuff` package to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from stuff.accum import Accumulator

@pytest.fixture
def accum():
    return Accumulator()

def test_accumulator_init(accum):
    assert accum.count == 0

def test_accumulator_add_one(accum):
    accum.add(1)
    assert accum.count == 1

def test_accumulator_add_three(accum):
    #accum.add(1)
    #accum.add(2)
    accum.add(3)
    assert accum.count == 3

def test_accumulator_add_twice(accum):
    accum.add(2)
    accum.add(3)
    assert accum.count == 5

# def test_accumulator_can_not_set_count_directly():
#     accum = Accumulator()
#     with pytest.raises(AttributeError, match=r"can't set attribute") as e:
#         accum.count = 10

