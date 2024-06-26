#!/usr/bin/env python3
"""
module containing an async coroutine called async_generator
that takes no arguments.
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    coroutine that will loop 10 times, each time asynchronously wait 1
    second, then yield a random number between 0 and 10. Use the random
    module.

    Args:
        NUll

    Return:
        Yield a random number(float) between 0 and 10.
    """
    for _ in range(10):
        # asynchronously wait for 1 sec
        await asyncio.sleep(1)

        # generate a random number between 0 and 10
        random_num = random.random() * 10

        yield random_num
