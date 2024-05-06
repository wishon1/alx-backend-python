#!/usr/bin/env python3
"""
Module to execute multiple coroutines at the same time with async
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Async function that returns the list of all the delays (float values).

    Args:
        n (int): Number of delays
        max_delay (int): Maximum number of delays

    Returns:
        List[float]: List of all the delays (float values). The list of
        the delays should be in ascending order without using sort() because
        of concurrency.
    """
    wait_times = []
    for _ in range(n):
        wait_times.append(await wait_random(max_delay))
    return sorted(wait_times)
