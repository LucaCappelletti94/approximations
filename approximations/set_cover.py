"""Functions for handling greedy approximation of Set Cover."""
from typing import List, Set
import numpy as np

__all__ = ["set_cover"]

def coverage_weights(subsets: List[Set], weights: List[float], uncovered: Set) -> List[float]:
    r"""Return weights updated with the coverage score for each set.

    The coverage score for each $i$-th set is:

    .. math::

       \frac{w_{i}}{S_{i} \cap \text{Uncovered}}
       
    """
    for w, subset in zip(weights, subsets):
        intersection = len(subset.intersection(uncovered))
        yield (w/intersection if intersection else np.inf)


def set_cover(full_set: Set, subsets: List[Set], weights: List[float])->List[int]:
    r"""Return the an approximated minimum set cover for given sets.
        
    Considering the Harmonic function:

    .. math::

        H(n)=\sum_{i=1}^{n} \frac{1}{i}

    The approximation achieved by the greedt set cover is equal to:

    .. math::

        \sum_{k=1}^n H\left(\left|S_{k}\right|\right) \cdot w_{k}

    Parameters
    ----------
    full_set:Set
        Complete set of elements of the subsets. 

    subsets:List[Set]
        List of subsets.
    
    weights:List[float]
        Weights of the subsets in problem instance.

    Returns
    -------
    List of selected subsets indices.

    Raises
    ------
    ValueError
        If given subsets list is empty.

    ValueError
        If given subsets list contain only one set.
    
    ValueError
        If given lengths of subsets and weights lists do not match.

    """

    if not subsets:
        raise ValueError("Given subsets list is empty.")
    if len(subsets)<2:
        raise ValueError("Given subsets list contains only one set.")
    if len(subsets) != len(weights):
        raise ValueError("Lengths of subsets and weights lists do not match.")
    uncovered, min_set_cover = full_set.copy(), []
    while uncovered:
        argmin = np.argmin(list(coverage_weights(subsets, weights, uncovered)))
        uncovered -= subsets[argmin]
        min_set_cover.append(argmin)
    return min_set_cover
