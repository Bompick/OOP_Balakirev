import asyncio


async def two():
    print("my ")


async def three():
    a = input("ВВедите число")
    print(a)


async def main():
    print('Hello, ')
    await three()
    await two()
    print('world')

asyncio.run(main())



