from approximations import load_balancing
import pytest

def test_load_balancing_exceptions():
    with pytest.raises(ValueError):
        load_balancing([], 0)

    with pytest.raises(ValueError):
        load_balancing([], 1.5)

def test_load_balancing():
    v = [1,2,3,4,5,6]
    w = 3
    assignment, makespans = load_balancing(v, w)
    assert assignment == [[5, 0], [4, 1], [3, 2]]
    assert makespans == [7, 7, 7]