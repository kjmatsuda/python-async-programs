# Page 271
import asyncio
import threading
import time


def myMakeTask(loop, cor, value):
    loop.call_soon_threadsafe(lambda: loop.create_task(cor(value)))


async def myFunction1(value):
    await asyncio.sleep(0)
    print(value)


async def myFunction2(value):
    print(value)
    await asyncio.sleep(0)

myLoop = None


def myThreadLoop():
    global myLoop
    myLoop = asyncio.new_event_loop()
    T1 = myLoop.create_task(myFunction1(42))
    T2 = myLoop.create_task(myFunction2(43))
    myLoop.run_forever()


t = threading.Thread(target=myThreadLoop)
t.start()
time.sleep(0)
while not myLoop:
    pass
myMakeTask(myLoop, myFunction1, 44)
t.join()
