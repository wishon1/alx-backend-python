#!/usr/bin/env python3
"""
Basic annotations - floor:
    type-annotated function floor which takes a float n as argument
    and returns the floor of the float.
"""
import math


def floor(n: float) -> int:
    """
    floor: function takes a float n as argument
    and returns the floor of the float.

    Args:
        n(float): n is the argument in float

    Returns:
        Returns the floor of the float
    """
    return math.floor(n)
