# Page 253
import asyncio
import time


async def tick():
    i = 0
    while True:
        i += 1
        print("TICK", i)
        await asyncio.sleep(0.5)


def _myPi(m, n):
    pi = 0
    for k in range(m, n+1):
        s = 1 if k % 2 else -1
        pi += s / (2 * k - 1)
    return 4*pi


async def myPi(m, n):
    return await asyncio.to_thread(_myPi, m, n)


async def main():
    n = 100
    t1 = time.perf_counter()
    T1 = asyncio.create_task(myPi(1, 10000000))
    T2 = asyncio.create_task(tick())
    done, pending = await asyncio.wait([T1, T2],
                                       return_when=asyncio.FIRST_COMPLETED)
    t2 = time.perf_counter()
    print((t2-t1)*1000)
    print(done.pop().result())

asyncio.run(main())
