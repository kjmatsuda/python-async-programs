# Page 277
import asyncio


class ClientDatagramProtocol(asyncio.DatagramProtocol):
    def datagram_received(self, data, addr):
        message = data.decode("utf8")
        print("Received", message, "from", addr)


async def main():
    loop = asyncio.get_running_loop()
    transport, protocol = await loop.create_datagram_endpoint(
        lambda: ClientDatagramProtocol(),
        local_addr=('192.168.253.14', 8080))
    await asyncio.sleep(1000)
    transport.close()

asyncio.run(main())
