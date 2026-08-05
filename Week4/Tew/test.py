import asyncio
import time

async def bad(n):
    return n * 2
    







async def main():
    t1 = asyncio.create_task(bad(5))
    t2 = asyncio.create_task(bad(10))

    res2 = await t2
    res1 = await t1
    print(f"{res1} {res2}")




    
asyncio.run(main())