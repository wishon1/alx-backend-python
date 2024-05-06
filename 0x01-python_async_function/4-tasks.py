#!/usr/bin/env python3
"""
task 4
"""
import asyncio
from typing import List

# Import the task_wait_random function using __import__
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''
    Executes task_wait_random n times and returns sorted delay times.

    Args:
        n (int): Number of times to execute the task.
        max_delay (int): Maximum delay for each task.

    Returns:
        List[float]: List of sorted delay times.
    '''
    # List to store the delay times
    wait_times = []

    # Loop 'n' times and call task_wait_random each time
    for _ in range(n):
        # Await the result of task_wait_random and append it to wait_times
        wait_times.append(await task_wait_random(max_delay))

    # Sort the list of delay times in ascending order
    return sorted(wait_times)
