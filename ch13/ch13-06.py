# Page 255
import aiohttp
import asyncio


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get("http://www.example.com") as response:

            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])

            html = await response.text()
            print("Body:", html[:25], "...")

asyncio.run(main())
