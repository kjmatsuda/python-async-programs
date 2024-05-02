# Page 232
import asyncio
import random

idGlobal = 0


async def inner(idparam):
    global idGlobal
    await asyncio.sleep(0)
    if idparam != idGlobal:
        print("error")


async def outer():
    global idGlobal
    id = random.randint(0, 10000)
    idGlobal = id
    await inner(id)


async def main():
    await asyncio.gather(outer(), outer())

asyncio.run(main())
