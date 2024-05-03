#!/usr/bin/env python3
"""
module containing a type-annotated function sum_mixed_list - which
takes a list mxd_lst of integers and floats and returns their sum as a float.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    sum_mixed_list: type-annotated function sum_mixed_list which takes a
    list mxd_lst of integers and floats and returns their sum as a float.

    Args:
        mxd_lst: list of integers and floats

    Returns: sum of the mxd_lst list as a float
    """

    return float(sum(mxd_lst))
