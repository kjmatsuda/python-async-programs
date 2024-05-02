# Page 263
import asyncio


async def main():
    p = await asyncio.create_subprocess_exec("./myscript.sh",
                                             stdout=asyncio.subprocess.PIPE, stdin=asyncio.subprocess.PIPE)
    ans = await p.stdout.readline()
    print("message", ans)
    p.stdin.write(b"mike\n")
    ans = await p.stdout.readline()
    print("message", ans)

asyncio.run(main())
