import asyncio
import random


async def two(x):
    a = random.randint(1, 10)
    await asyncio.sleep(a)
    return print(x, f'  спал {a} сек')


async def one(x):
    a = random.randint(1, 10)
    await asyncio.sleep(a)
    return print(x, f'  спал {a} сек')


async def main():
    for x in range(5):
        await asyncio.gather(one(1), two(2)) # пример функции asyncio.gather()
        # task1 = asyncio.create_task(one(1))
        # task2 = asyncio.create_task(two(2))
        # await task1
        # await task2
        print()

asyncio.run(main())



