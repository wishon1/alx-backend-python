#!/usr/bin/env python3
"""
module containing an Async Comprehensions: import async_generator from
the previous task and then write a coroutine called async_comprehension
that takes no arguments. The coroutine will collect 10 random numbers
using an async comprehensing over async_generator, then return the 10
random numbers.
"""
import asyncio
from typing import List

async_gen = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    The coroutine will collect 10 random numbers using an async
    comprehension over async_generator, then return the 10 random
    numbers.

    Args:
        NULL

    Returns: List of random numbers (float).
    """
    new_list_of_nums = [num async for num in async_gen()]
    return new_list_of_nums
