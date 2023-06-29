import asyncio


async def sleep():
    await asyncio.sleep(5)
    print("Hello")

asyncio.run(sleep())


