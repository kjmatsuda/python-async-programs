# Page 280
import asyncio
import socket


async def main():
    loop = asyncio.get_running_loop()

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    data = b"Hello UDP World"
    await loop.sock_connect(sock, ("192.168.253.255", 8080))
    await loop.sock_sendall(sock, data)

asyncio.run(main())
