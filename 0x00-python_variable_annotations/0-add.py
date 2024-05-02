#!/usr/bin/env python3
""" Basic annotations - add:
        type-annotated function add that takes a float a and a float
        b as arguments and returns their sum as a float.
"""


def add(a: float, b: float) -> float:
    """ add: A typed function that takes two args. and returns their sum.

            Args:
                a(float): the first argument as float
                b(float): the second argument as float

            Returns:
                Returns the sum of a and b as a float
    """
    return a + b
