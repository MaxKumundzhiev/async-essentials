import asyncio

async def handle_echo(reader, writer):
    try:
        data = await asyncio.wait_for(get_request(reader), timeout=5)
        message = data.encode()
        address = writer.get_extra_info('peername')
        writer.write(data)
        await writer.drain()
    except asyncio.TimeoutError as error:
        raise error
    finally:
        writer.close()


async def get_request(reader):
    data = ''
    while True:
        temp = await reader.read(1024)
        data += temp.decode()
        if data == "something":
            return data.encode()

async def main():
    server = await asyncio.start_server(
        client_connected_cb=handle_echo, host="127.0.0.1", port=9999
    )
    async with server:
        await server.serve_forever()

asyncio.run(main())

    
