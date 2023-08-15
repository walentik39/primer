#!/usr/bin/python3

import asyncio
import time
import random

async def task1():

    wait = random.randint(0, 3)
    await asyncio.sleep(wait)
    print("task 1 finished")


async def task2():

    wait = random.randint(0, 3)
    await asyncio.sleep(wait)
    print("task 2 finished")


async def task3():

    wait = random.randint(0, 3)
    await asyncio.sleep(wait)
    print("task 3 finished")


async def main():

    for x in range(2):
        await asyncio.gather(task1(), task2(), task3())
        time.sleep(1)
        print('----------------------------')

t1 = time.perf_counter()
asyncio.run(main())
t2 = time.perf_counter()

print(f'Total time elapsed: {t2-t1:0.2f} seconds')
