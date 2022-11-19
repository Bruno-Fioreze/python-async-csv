import asyncio
import aiofiles
from aiocsv import AsyncReader, AsyncDictReader, AsyncWriter, AsyncDictWriter


async def read_file(file: str):
    print("========== start ============")
    async with aiofiles.open(file, mode="r", encoding="utf-8", newline="") as afp:
        async for row in AsyncDictReader(afp):
            print(row)  # row is a list
    print("========== finish ============")

async def coro():
    await asyncio.gather(read_file("./addresses.csv"), read_file("./addresses2.csv"))
    print("started coro")

asyncio.run(coro())


import asyncio
from functools import wraps
def request_concurrency_limit_decorator(limit=3):
    # Bind the default event loop 
    sem = asyncio.Semaphore(limit)

    def executor(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            async with sem:
                return await func(*args, **kwargs)

        return wrapper

    return executor

@request_concurrency_limit_decorator(limit=...)
async def download():
    ...