# Page 243
import asyncio
import urllib.parse
import time
import email


def parseHeaders(headers):
    message = email.message_from_string(headers)
    return dict(message.items())


async def download(url):
    url = urllib.parse.urlsplit(url)
    reader, writer = await asyncio.open_connection(
        url.hostname, 443, ssl=True)

    request = (
        f"GET /index.html HTTP/1.1\r\n"
        f"Host: {url.hostname}\r\n"
        f"\r\n"
    )
    writer.write(request.encode('ascii'))

    headers = ""
    line = await reader.readline()

    while True:
        line = await reader.readline()
        line = line.decode('ascii')
        if line == "\r\n":
            break
        headers += line

    headers = parseHeaders(headers)
    length = int(headers["Content-Length"])

    line = await reader.read(length)
    line = line.decode('utf8')
    writer.close()
    await writer.wait_closed()
    return line


async def main():
    start = time.perf_counter()
    results = await asyncio.gather(download('http://www.example.com/'), download('http://www.example.com/'))
    end = time.perf_counter()
    print((end-start)*1000)
    print(results[0][:25])
    print(results[1][:25])


asyncio.run(main())
