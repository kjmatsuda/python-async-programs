# Page 272
import asyncio
import concurrent.futures


def myFunction1(value):
    print(value)
    return value


if __name__ == '__main__':
    pool = concurrent.futures.ProcessPoolExecutor()
    myLoop = asyncio.new_event_loop()

    T1 = myLoop.run_in_executor(pool, myFunction1, 42)
    T2 = myLoop.run_in_executor(pool, myFunction1, 43)

    myLoop.run_until_complete(asyncio.wait([T1, T2]))
    print(T1.result())
    print(T2.result())
    pool.shutdown()
