# Page 230
import asyncio
import asyncio.locks


async def count():
    global myCounter
    global myLock
    for i in range(1000):
        async with myLock:
            temp = myCounter+1
            await asyncio.sleep(0)
            myCounter = temp


async def main():
    t1 = asyncio.create_task(count())
    t2 = asyncio.create_task(count())
    await asyncio.wait([t1, t2])
    print(myCounter)

myCounter = 0
myLock = asyncio.locks.Lock()
asyncio.run(main())
