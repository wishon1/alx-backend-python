#!/usr/bin/env python3
"""
type-annotated function sum_list which takes a list input_list of
floats as argument and returns their sum as a float.
"""
from typing import List


def sum_list(input_list: List[float]) ->float:
    """
    sum_list: function sum_list which takes a list input_list of floats
    as argument and returns their sum as a float.

    Args:
        input_list: A list of floating point numbers

    Returns: Returns the sum of the list as float
    """
    sum_val = 0.0
    for i in input_list:
        sum_val += i
 
    return sum_val
