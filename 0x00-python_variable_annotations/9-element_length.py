#!/usr/bin/env python3
"""
this module contains a task to Annotate the below function’s parameters
and return values with the appropriate types
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    element_length: function that accepts an iterable containing sequences
    and returns a list of tuples where each tuple contains a sequence and
    its length.

    Args:
        lst: An iterable containing sequences.

    Returns:
        A list of tuples where each tuple contains a sequence and its length.
    """
    return [(i, len(i)) for i in lst]
