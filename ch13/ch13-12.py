# Page 264
import asyncio

async def main():
    p = await asyncio.create_subprocess_exec("./myscript.sh",stdout=asyncio.subprocess.PIPE,stdin=asyncio.subprocess.PIPE)
    T=asyncio.create_task(p.stdout.read(100))
    try:
        done,pending=await asyncio.wait([T],timeout= 0.1)
    except asyncio.TimeoutError:
        pass
    print("message",T.result())
    p.stdin.write(b"mike\n")
    ans= await p.stdout.readline()
    print("message",ans)
    await p.wait()

asyncio.run(main())
