# Page 221
import asyncio


async def test1(msg):
    print(msg)


async def main():
    asyncio.create_task(test1("one"))
    asyncio.create_task(test1("two"))

    await test1("three")
    print("Hello Coroutine World")
    await asyncio.sleep(0)

asyncio.run(main())
