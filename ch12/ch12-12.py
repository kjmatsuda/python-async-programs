# Page 233
import asyncio
import random
import contextvars

idGlobalCtx = contextvars.ContextVar("id")


async def inner(idparam):
    await asyncio.sleep(0)
    print(idparam, idGlobalCtx.get(), end=" ")
    if idparam != idGlobalCtx.get():
        print("error", end="")
    print()


async def outer():
    global idGlobal
    id = random.randint(0, 10000)
    idGlobalCtx.set(id)
    await inner(id)


async def main():
    await asyncio.gather(outer(), outer())

asyncio.run(main())
