# Basic Program
import asyncio

async def brew(name):
    print(f'brewing {name}...')
    await asyncio.sleep(2) # to sleep for 2 sec
    print(f'{name} is ready')

asyncio.run(brew("Masala chai"))

# Program 2
import asyncio

async def b1(name):
    print(f"Brewing {name}...")
    await asyncio.sleep(2)
    print(f"{name} is Ready , Enjoy the Chai")

async def main():
    chais = ["Masala Chai","Green Chai","Ginger Chai"]
    tasks = [b1(c) for c in chais]
    await asyncio.gather(*tasks)

asyncio.run(main())

# Fetch Urls

import asyncio
import aiohttp

async def x1(session,url):
    async with session.get(url) as response:
        print(f'fetched {url} with status {response.status}')

async def main():
    urls = ['https://httpbin.org/#/Images/get_image','https://httpbin.org/#/Images/get_image_jpeg','https://httpbin.org/#/Images/get_image_png']
    async with aiohttp.ClientSession() as session:
        z = [x1(session,url) for url in urls]
        await asyncio.gather(*z)

asyncio.run(main())
