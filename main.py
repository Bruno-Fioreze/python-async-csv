import asyncio
import aiofiles
from aiocsv import AsyncReader, AsyncDictReader, AsyncWriter, AsyncDictWriter
from decorator import request_concurrency_limit_decorator


# @request_concurrency_limit_decorator(limit=1)
async def read_file(file: str):
    async with aiofiles.open(file, mode="r", encoding="utf-8", newline="") as afp:
        async for row in AsyncDictReader(afp):
            print(row)  # row is a list

async def coro():
    await asyncio.gather(read_file("./addresses.csv"), read_file("./addresses2.csv"))
    print("started coro")

asyncio.run(coro())

