"""Functions for handling fptas approximation of Knapsack."""
from knapsack import knapsack
from typing import List, Tuple
from math import ceil

__all__ = ["fptas"]

def rounding_factor(values:List[float], approximation:float)->float:
    """Return the rounding factor for the given approximation.
        values:List[float], values of the items in problem instance.
        approximation:float, expected score approximation.
    """
    return approximation * max(values) / (2*len(values))

def round_values(values:List[float], approximation:float)->List[float]:
    """Return the rounded values for the given approximation.
        values:List[float], values of the items in problem instance.
        approximation:float, expected score approximation.
    """
    b = rounding_factor(values, approximation)
    return [
        ceil(v/b)*b
        for v in values
    ]

def fptas(weights:List[float], values:List[float], capacity:float, approximation:float)->Tuple[float, float, List[int]]:
    r"""Return a triple containing the total weights, values and indices of used objects.

    The knapsack problem or rucksack problem is a problem in combinatorial optimization:
    given a set of $n$ items, each with a weight and a value, determine the number of each item
    to include in a collection so that the total weight is less than or equal to a given
    limit and the total value is as large as possible. It derives its name from the
    problem faced by someone who is constrained by a fixed-size knapsack and must fill it
    with the most valuable items.

    In this FPTAS approximation, a rounding factor $b$ is determined based on the given
    approximation $\varepislon$ factor and is aferwards used to determine the rounded values.

    .. math::

        b = \frac{\varepsilon}{2n}\cdot\max w

    .. math::

        \tilde{v}_i = \left \lceil \frac{v_i}{b} \right \rceil \cdot b

    Parameters
    ----------
    weights:List[float]
        weights of the items in problem instance.

    values:List[float]
        values of the items in problem instance.
    
    capacity:float,
        maximum capacity of the knapsack.

    approximation:float,
        expected score approximation.

    Returns
    -------
    Triple of values, containing total weight and values of selected items
    and the indices of the selected items.

    Raises
    ------
    ValueError
        If values and weights lists have different sizes.
    ValueError
        If values list is empty.
    ValueError
        If the approximation factor is not strictly positive.
    ValueError
        If the capacity is not strictly positive.

    References
    ----------
    .. [1] Vazirani, Vijay V. Approximation algorithms.
        Springer Science & Business Media, 2013.
    """
    if len(weights) != len(values):
        raise ValueError("The values and weights lists have different sizes.")

    if not len(weights):
        raise ValueError("Provide at least one object.")

    if capacity < 1:
        raise ValueError("The capacity is not strictly positive.")

    if approximation <= 0:
        raise ValueError("The approximation factor is not strictly positive.")
    
    _, objects = knapsack(
        weight=round_values(values, approximation),
        size=weights
    ).solve(capacity)
    total_weight = sum([
        weights[i] for i in objects
    ])
    total_value = sum([
        values[i] for i in objects
    ])
    return total_weight, total_value, objects