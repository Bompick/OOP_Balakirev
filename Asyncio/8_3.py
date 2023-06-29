import asyncio
import aiohttp
from codetiming import Timer

urls = ['http://google.com',
        'http://apple.com',
        'https://stepik.org',
        'https://habr.com']


async def main(url):
    with Timer(text=f'Затраченное время: {{:.3f}} сек'):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                print(resp.url)


if __name__ == "__main__":
    task = [main(link) for link in urls]
    # asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(asyncio.wait(task))

