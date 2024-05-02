# Page 250
import urllib.request
import asyncio
import time

async def download():
    with urllib.request.urlopen('http://www.example.com/') as f:
        html = f.read().decode('utf-8')
        return html

async def main():
    t1=time.perf_counter()
    results=await asyncio.gather(download(),download())
    t2=time.perf_counter()
    print((t2-t1)*1000)
    print(results[0][:25])

asyncio.run(main())
