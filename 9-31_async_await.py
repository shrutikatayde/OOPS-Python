import asyncio
import time
import requests


async def f1():

    # await asyncio.sleep(1)
    # return 5

    URL = "https://instagram.com/favicon.ico"
    response = requests.get(URL)
    open("instagram.jpg", "wb").write(response.content)
    print("1st function")


async def f2():
    # await asyncio.sleep(1)

    URL = "https://instagram.com/favicon.ico"
    response = requests.get(URL)
    open("instagram1.jpg", "wb").write(response.content)
    print("2nd function")


async def f3():
    # await asyncio.sleep(4)
    URL = "https://instagram.com/favicon.ico"
    response = requests.get(URL)
    open("instagram2.jpg", "wb").write(response.content)
    print("3rd function")


async def main():
    # asyncio.create_task(f1())
    # await f1()
    # await f2()
    # await f3()
    g = await asyncio.gather(f1(), f2(), f3())
    print(g)


asyncio.run(main())
