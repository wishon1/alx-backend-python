#!/usr/bin/env python3
"""
Module containing a type-annotated function to_kv that takes a string k and
an int OR float v as arguments and returns a tuple. The first element of the
tuple is the string k. The second element is the square of the int/float v and
should be annotated as a float.
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    to_kv: Type-annotated function that takes a string k and an int OR float v
    as arguments and returns a tuple. The first element of the tuple is the
    string k. The second element is the square of the int/float v and should be
    annotated as a float.

    Args:
        k (str): The string key.
        v (Union[int, float]): The value, which can be either an integer or a
        float.

    Returns:
        Tuple[str, float]: A tuple containing the string key k and the square
        of v as a float.
    """
    return (k, float(v**2))
