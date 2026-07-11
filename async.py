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
