"""
https://www.youtube.com/watch?v=-CzqsgaXUM8&list=PLhNSoGM2ik6SIkVGXWBwerucXjgP1rHmB&index=3
"""

"""
method asyncio.wait_for(aw)
    wait for aw awaitable to complete with time out
    if aw is coroutine it is automatically scheduled a task


high levels structure if objects in asyncio
        AWAITAIBLE (any objected which can be awaited on)
            |
       _____|_____
      |          |
  COROUTINE    FUTURE
                 |
                TASK                 
"""


import asyncio
from datetime import datetime


def print_now():
    print(datetime.now())


async def keep_printing(name: str = "") -> None:
    while True:
        print(name, end=" ")
        print_now()
        await asyncio.sleep(0.5)


async def main() -> None:
    try:
        await asyncio.wait_for(keep_printing(name="hey"), 10)
    except TimeoutError:
        print("oops, timeout")


if __name__ == "__main__":
    # asyncio.run(keep_printing())
    # add time exception
    # asyncio.run(asyncio.wait_for(keep_printing(), 10))
    asyncio.run(main())