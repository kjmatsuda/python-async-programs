# Page 216
import asyncio


async def test1(msg):
    print(msg)


async def main():
    await test1("Hello Coroutine World")

asyncio.run(main())
