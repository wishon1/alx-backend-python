#!/usr/bin/env python3
"""
module containing task_wait_random that takes an integer max_delay
and returns a asyncio.Task.
"""
import asyncio
from typing import Any

# import wait_andom coroutine from 0-basic_async_syntax
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Function to create and return an asyncio.Task for the wait_random
    coroutine.

    Args:
        max_delay (int): Maximum delay.

    Returns:
        asyncio.Task: Task object representing the execution of wait_random.
    """
    return asyncio.create_task(wait_random(max_delay))
