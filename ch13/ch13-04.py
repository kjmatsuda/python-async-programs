# Page 251
import urllib.request
import asyncio
import time


def _download():
    with urllib.request.urlopen('http://www.example.com/') as f:
        html = f.read().decode('utf-8')
        return html


async def download():
    return await asyncio.to_thread(_download)


async def main():
    n = 1000
    t1 = time.perf_counter()
    results = await asyncio.gather(*[download() for i in range(n)])
    t2 = time.perf_counter()
    print((t2-t1)*1000)
    print(results[0][:25])

asyncio.run(main())
