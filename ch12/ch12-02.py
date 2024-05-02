# Page 219
import asyncio


async def count(n):
    for i in range(n):
        print(i)
    return n


async def main(myValue):
    t1 = asyncio.create_task(count(10))
    print("Hello Coroutine World")
    await asyncio.sleep(5)
    return myValue

result = asyncio.run(main(42))
print(result)
