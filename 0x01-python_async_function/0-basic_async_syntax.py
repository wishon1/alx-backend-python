#!/usr/bin/env python3
"""
Module containing an asynchronous coroutine that takes in an integer
argument (max_delay, with a default value of 10) named wait_random that
waits for a random delay between 0 and max_delay (included and
float value) seconds and eventually returns it.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    asynchronous coroutine that takes in an integer argument (max_delay,
    with a default value of 10) named wait_random that waits for a random
    delay between 0 and max_delay (included and float value) seconds and
    eventually returns it.

    Args:
        max_delay(int): this is the maximum delay in seconds, the default
        value is 10

    Returns:
        float: Random delay between 0 and max_delay seconds.
    """
    # generate a random floatingpoint number between 0-10
    delay_time = random.random() * max_delay
    await asyncio.sleep(delay_time)

    return delay_time
