# Page 228 bottom
import asyncio


async def test(msg):
    print(msg)
    raise Exception("Test exception")


async def main():
    t1 = asyncio.create_task(test("one"))

    done, pending = await asyncio.wait([t1])
    print(repr(done.pop().exception()))

    print("Hello Coroutine World")
    await asyncio.sleep(0)

asyncio.run(main())
