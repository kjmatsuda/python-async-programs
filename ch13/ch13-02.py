# Page 247
import asyncio
import email
import email.utils


async def handleRequest(reader, writer):
    headers = ""
    while True:
        line = await reader.readline()
        line = line.decode('ascii')
        if line == "\r\n":
            break
        headers += line
    print(headers)
    html = ("<html><head><title>Test Page</title></head><body>"
            "page content"
            "</p></body></html>\r\n")
    headers = ("HTTP/1.1 200 OK\r\n"
               "Content-Type: text/html; charset=UTF-8\r\n"
               "Server:PythonAcyncio\r\n"
               f"Date: {email.utils.formatdate(timeval=None,localtime=False, usegmt=True)}\r\n"
               f"Content-Length:{len(html)}\r\n\r\n"
               )
    data = headers.encode("ascii")+html.encode("utf8")
    writer.write(data)
    await writer.drain()
    await writer.wait_closed()


async def main():
    server = await asyncio.start_server(handleRequest, "", 8080)
    async with server:
        await server.serve_forever()


asyncio.run(main())
