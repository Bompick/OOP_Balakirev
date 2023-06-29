import asyncio


async def one():
    await asyncio.sleep(6)
    print(1)


async def two():
    print('shifted')
    await asyncio.sleep(10)
    print('final')


async def main():
    await asyncio.gather(one(), two())

asyncio.run(main())
