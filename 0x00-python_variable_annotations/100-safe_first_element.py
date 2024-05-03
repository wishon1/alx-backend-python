#!/usr/bin/env python3
"""
This script defines a function safe_first_element that returns the first
element of a sequence safely, or None if the sequence is empty.
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence) -> Union[Any, None]:
    """
    safe_first_element: function that returns the first element of a
    sequence safely, or None if the sequence is empty.

    Args:
        lst: A sequence.

    Returns:
        The first element of the sequence if it exists, otherwise None.
    """
    if lst:
        return lst[0]
    else:
        return None
