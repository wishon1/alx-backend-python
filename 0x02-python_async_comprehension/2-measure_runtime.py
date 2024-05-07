#!/usr/bin/env python3
"""
Run time for four parallel comprehensions: Import async_comprehension
from the previous file and write a measure_runtime coroutine that will
execute async_comprehension four times in parallel using asyncio.gather.

Notice that the total runtime is roughly 10 seconds, explain it to yourself.
"""
import asyncio
import time

async_comp = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    coroutine that will execute async_comprehension four times in parallel
    using asyncio.gather.

    Args:
        None

    Returns: return a float
    """
    startTime = time.time()

    await asyncio.gather(*(async_comp() for n_time in range(4)))

    end_time = time.time()
