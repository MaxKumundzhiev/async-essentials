import asyncio
from time import sleep


"""Syncrounous appraoch"""
# def make_request(counter:int = 0):
#     print(f"making request to db, {counter}")
#     sleep(0.1)


# for counter in range(1, 10_001):
#     make_request(counter=counter)
"""Syncrounous appraoch"""


async def make_request():
    print(f"making request to db")
    await asyncio.sleep(0.1)

async def main():
    chunk = 200
    tasks = []
    
    for idx in range(10_000):
        tasks.append(asyncio.create_task(make_request()))
        if len(tasks) == chunk:
            await asyncio.gather(*tasks)
            tasks = []
            print(idx)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())