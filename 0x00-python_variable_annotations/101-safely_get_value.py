#!/usr/bin/env python3
"""
Given the parameters and the return values, add type
annotations to the function

Hint: look into TypeVar

def safely_get_value(dct, key, default = None):
    if key in dct:
        return dct[key]
    else:
        return default
"""
from typing import Any, Mapping, Union, TypeVar

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None])\
                    -> Union[Any, T]:
    """
    safely_get_value: function that safely retrieves a value from
    a dictionary.

    Args:
        dct: A mapping (e.g., dictionary) from keys to values.
        key: The key whose value should be retrieved.
        default: An optional default value to return if the key is not found
        in the dictionary. Defaults to None.

    Returns:
        The value corresponding to the key if found in the dictionary,
        otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
