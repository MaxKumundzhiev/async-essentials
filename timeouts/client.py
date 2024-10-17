import asyncio

SOCKET = ("127.0.0.1", 9999)


async def tcp_echo_client(message):
    reader, writer = await asyncio.open_connection(*SOCKET)
    writer.write(message.encode())
    data = await reader.read(100)
    writer.close()

async def null_connection():
    reader, writer = await asyncio.open_connection(*SOCKET)
    writer.close()


async def main():
    try:
        await tcp_echo_client(message='')
        await null_connection()
    except ConnectionRefusedError as error:
        raise error


asyncio.run(main())