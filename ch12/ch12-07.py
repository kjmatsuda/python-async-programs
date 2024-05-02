# Page 228 top
import asyncio


async def test(msg):
    print(msg)
    raise Exception("Test exception")


async def main():
    t1 = asyncio.create_task(test("one"))
    try:
        await t1
    except:
        print("an exception has occurred")
    print("Hello Coroutine World")
    await asyncio.sleep(0)

asyncio.run(main())
