# Page 262
import asyncio


async def main():
    p = await asyncio.create_subprocess_exec("dir", "/",
                                             stdout=asyncio.subprocess.PIPE)
    stdout_data, stderr_data = await p.communicate()
    print(stdout_data)
    print("finished")

asyncio.run(main())
