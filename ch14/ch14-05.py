# Page 273
import asyncio
import concurrent.futures
import time


def myPi(m, n):
    pi = 0
    for k in range(m, n+1):
        s = 1 if k % 2 else -1
        pi += s / (2 * k - 1)
    return pi*4


if __name__ == '__main__':
    pool = concurrent.futures.ProcessPoolExecutor()

    myLoop = asyncio.new_event_loop()

    N = 10000000
    with concurrent.futures.ProcessPoolExecutor() as pool:
        t1 = time.perf_counter()
        T1 = myLoop.run_in_executor(pool, myPi, 1, N//2)
        T2 = myLoop.run_in_executor(pool, myPi, N//2+1, N)
        myLoop.run_until_complete(asyncio.wait([T1, T2]))
        t2 = time.perf_counter()

    PI = T1.result()
    PI += T2.result()
    print((t2-t1)*1000)
    print(PI)
