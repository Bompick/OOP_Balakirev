import asyncio


async def nes():
    return print("Сопрограмма вызвана")


async def main():
    await nes()

asyncio.run(main())
