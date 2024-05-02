# Page 276
import asyncio


async def main():
    loop = asyncio.get_running_loop()
    transport, protocol = await loop.create_datagram_endpoint(
        lambda: asyncio.DatagramProtocol(),
        local_addr=("192.168.253.20", 8080))

    data = b"Hello UDP World"
    transport.sendto(data, addr=("192.168.253.14", 8080))
    transport.close()

asyncio.run(main())
