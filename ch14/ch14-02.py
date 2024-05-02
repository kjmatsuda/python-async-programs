# Page 269
import asyncio


async def myFunction1(value):
    await asyncio.sleep(0)
    print(value)


async def myFunction2(value):
    print(value)
    await asyncio.sleep(0)

myLoop = asyncio.new_event_loop()
T1 = myLoop.create_task(myFunction1(42))
T2 = myLoop.create_task(myFunction2(43))

myLoop.run_forever()
