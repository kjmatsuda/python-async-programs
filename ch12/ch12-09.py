# Page 229
import asyncio


async def count():
    global myCounter
    for i in range(1000):
        temp = myCounter+1
        myCounter = temp


async def main():
    t1 = asyncio.create_task(count())
    t2 = asyncio.create_task(count())
    await asyncio.wait([t1, t2])
    print(myCounter)

myCounter = 0
asyncio.run(main())
