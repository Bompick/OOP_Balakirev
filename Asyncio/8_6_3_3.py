import asyncio
import random


async def one(x):
    a = random.randint(1, 10)
    await asyncio.sleep(a)
    return print(x, f' спал {a} сек, one')


async def two(x):
    a = random.randint(1, 10)
    await asyncio.sleep(a)
    return print(x, f' спал {a} сек, two')


async def three(x):
    a = random.randint(1, 10)
    await asyncio.sleep(a)
    return print(x, f' спал {a} сек, three')


async def main():
    group1 = asyncio.gather(*[one(i) for i in range(5)])
    group2 = asyncio.gather(*[two(i) for i in range(5)])
    group3 = asyncio.gather(*[three(i) for i in range(5)])
    await asyncio.gather(group1, group2, group3)


asyncio.run(main())



