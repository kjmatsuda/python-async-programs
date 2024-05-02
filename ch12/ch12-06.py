# Page 227
import asyncio


async def test1(msg):
    try:
        await asyncio.sleep(0)
    except:
        pass
    print(msg)
    return msg


async def main():
    t1 = asyncio.create_task(test1("one"))
    await asyncio.sleep(0)
    t1.cancel()
    print("Hello Coroutine World")
    await asyncio.sleep(0)

asyncio.run(main())
