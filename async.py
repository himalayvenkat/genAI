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


# SYNC + ASYNC with multi threading 
import asyncio
import time
import concurrent.futures

def s1(item):
    print(f"checing the {item}")
    time.sleep(4)
    return f'{item} in stock: 42'

async def main():
    loop = asyncio.get_running_loop()
    with concurrent.futures.ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(pool,s1,"Masala Chai")
        print(result)
asyncio.run(main())


import asyncio
import time
import concurrent.futures

def s11(a,b):
    print(f'the Values of a and b are {a},{b}')
    time.sleep(5)
    return a+b

async def main():
    loop = asyncio.get_running_loop()
    with concurrent.futures.ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(pool,s11,10,20)
        print(result)

asyncio.run(main())

# SYNC + ASYNC with multi processing 

import asyncio
import time
import concurrent.futures

def x121(x):
    return x[::-1]

async def main():
    loop = asyncio.get_running_loop()
    with concurrent.futures.ProcessPoolExecutor() as pool:
        result = await loop.run_in_executor(pool,x121,'HIMALAY')
        print(result)

if __name__ == '__main__':
    asyncio.run(main())


#### Daemon Thread 

import threading


def x1():
    while True:
        print("Hi Ra Mama")

t = threading.Thread(target=x1,daemon=True)
t.start()
print("Main Thread End")

import threading

# This Program will executes restlessly

def x1():
    while True:
        print("Hi Ra Mama")

t = threading.Thread(target=x1,daemon=False)
t.start()
print("Main Thread End")

import multiprocessing
import time


def x1():
    while True:
        print("Hi Ra Mama")

if __name__ == '__main__':
    x = multiprocessing.Process(target=x1,daemon=True)
    x.start()
    time.sleep(5) 
print("Main Thread End")