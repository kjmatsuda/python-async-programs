# Page 268
import asyncio


def myFunction(value):
    print(value)


myLoop = asyncio.new_event_loop()
myLoop.call_later(3, myFunction, 43)
t = myLoop.time()+2
myLoop.call_at(t, myFunction, 44)
myLoop.call_soon(myFunction, 42)

myLoop.call_soon(myFunction, 45)
myLoop.run_forever()
