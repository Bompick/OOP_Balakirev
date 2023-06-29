import asyncio


async def main():
    await asyncio.sleep(1)
    print(asyncio.get_running_loop())


asyncio.run(main())