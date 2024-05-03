#!/usr/bin/env python3
"""
A module containing a type-annotated function make_multiplier that
takes a float multiplier as argument and returns a function that multiplies
a float by multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    make_multiplier:  type-annotated function

    Args:
        multiplier: A float multiplier.

    Returns: function that takes a float as input and returns the product
    of that float and the multiplier
    """
    def multiplier_function(x: float) -> float:
        return x * multiplier

    return multiplier_function
