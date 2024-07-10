import asyncio

async def get_text():
    return "foobuzz"

async def say_text():
    text = await get_text()
    await asyncio.sleep(1)
    return text

result = asyncio.run(say_text())
print(result)