
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

@request_concurrency_limit_decorator(limit=3)
async def download():
    await asyncio.sleep(3)
    print("chegou aqui")
    ...

async def coro():
    await asyncio.gather( *[ download() for number in range(0, 10)])

asyncio.run(coro())

