#!/usr/bin/python3
"""
Basic annotations - concat:
    type-annotated function concat that takes a string str1 and a string
    str2 as arguments and returns a concatenated string
"""


def concat(str1: str, str2: str) -> str:
    """
    concat - takes a string str1 and a string str2 as arguments
    and returns a concatenated string

        Args:
            str1: The first ags, a string
            str2: The second args. of type str.

        Return: Returns a concatenated string
    """
    return str1 + str2
