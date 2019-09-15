from approximations import knapsack
import pytest

def test_knapsack_exceptions():
    with pytest.raises(ValueError):
        knapsack([], [], 0, 0)
    
    with pytest.raises(ValueError):
        knapsack([0], [], 0, 0)

    with pytest.raises(ValueError):
        knapsack([0], [0], 0, 0)

    with pytest.raises(ValueError):
        knapsack([0], [0], 1, 0)

def test_knapsack():
    v = 4
    w = 4
    w1, v1, o = knapsack([w], [v], w, 1)
    assert v1 == v
    assert w1 == v
    assert o[0] == 0
