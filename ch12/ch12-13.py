# Page 234
import asyncio
import asyncio.queues


async def addCount(q):
    for i in range(1000):
        await q.put(i)


async def getCount(q, id):
    while True:
        i = await q.get()
        print(id, i)
        await asyncio.sleep(0)


async def main():
    q = asyncio.queues.Queue()
    t1 = asyncio.create_task(addCount(q))
    t2 = asyncio.create_task(getCount(q, "t2"))
    t3 = asyncio.create_task(getCount(q, "t3"))
    await asyncio.wait([t1, t2, t3])

asyncio.run(main())
