import asyncio
import random


async def one(x):
    a = random.randint(1, 10)
    await asyncio.sleep(a)
    return print(x, f' спал {a} сек')


async def main():
    # lst = [x for x in range(10)]
    lst_tasks = []
    for x in range(15):
        task = asyncio.create_task(one(x))
        lst_tasks.append(task)
    await asyncio.gather(*lst_tasks)

asyncio.run(main())



