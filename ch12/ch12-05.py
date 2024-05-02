# Page 226
import asyncio


async def test1(msg):
    print(msg)
    return msg


async def main():
    result = await asyncio.gather(test1("one"), test1("two"))
    print(result)
    print("Hello Coroutine World")

asyncio.run(main())
