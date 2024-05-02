# Page 225
import asyncio


async def test1(msg):
    print(msg)
    return msg


async def main():
    t1 = asyncio.create_task(test1("one"))
    t2 = asyncio.create_task(test1("two"))
    done, pending = await asyncio.wait([t1, t2],
                                       return_when=asyncio.ALL_COMPLETED)
    for t in done:
        print(t.result())
    print("Hello Coroutine World")
asyncio.run(main())
