#!/usr/bin/env python3
"""
Module to measure the runtime of wait_n coroutine.
"""
import asyncio
import time


def measure_time(n: int, max_delay: int) -> float:
    """
    Function to measure the runtime of wait_n coroutine.

    Args:
        n (int): Number of iterations.
        max_delay (int): Maximum delay.

    Returns:
        float: Average execution time.
    """
    wait_n = __import__('1-concurrent_coroutines').wait_n
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))

    return (time.time() - start_time) / n
