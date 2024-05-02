# Page 279
import asyncio


async def main():
    loop = asyncio.get_running_loop()
    transport, protocol = await loop.create_datagram_endpoint(
        lambda: asyncio.DatagramProtocol(),
        local_addr=("192.168.253.20", 8080), allow_broadcast=True)
    sock = transport.get_extra_info('socket')
    print(sock)
    data = b"Hello UDP World"
    await loop.sock_connect(sock, ("192.168.253.255", 8080))
    await loop.sock_sendall(sock, data)
    transport.close()

asyncio.run(main())
