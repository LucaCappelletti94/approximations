"""Functions for handling greedy_sorted_balance approximation of Load Balancing."""
from typing import List, Tuple
import numpy as np

__all__ = ["greedy_sorted_balance"]

def greedy_sorted_balance(jobs: List[float], machines: int)->Tuple[List[int], List[float]]:
    r"""Return a tuple with assignment list and makespans list.

    The algorithm used is a $\frac{3}{2}$ approximation of the optimal makespan.

    Parameters
    ----------
    jobs: List[float],
        List with the required make time for each job.

    machines: int,
        Maximal number of machines.

    Returns
    -------
    Tuple of values: the list of assigned jobs and the list of makespans for each machine.

    Raises
    ------
    ValueError
        If the number of machines is not strictly positive integer.

    """
    if machines<1 or not isinstance(machines, int):
        raise ValueError("The machines' number must be a positive integer.")
    assignment = [[] for _ in range(machines)]
    makespans = [0]*machines
    for i, job in sorted(enumerate(jobs), key=lambda e: e[1], reverse=True):
        argmin = np.argmin(makespans)
        assignment[argmin].append(i)
        makespans[argmin] += job
    return assignment, makespans
