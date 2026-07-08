import asyncio
import httpx


async def fetch_stock_price(server_name: str):
    url = f"http://127.0.0.1:8088/price/{server_name}"

    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()
        return f"[{data['server']}] Price: {data['price_usd']} USD"


async def main():

    tasks = [
        asyncio.create_task(fetch_stock_price("Alpha"), name="alpha"),
        asyncio.create_task(fetch_stock_price("Beta"), name="beta"),
        asyncio.create_task(fetch_stock_price("Gamma"), name="gamma"),
    ]

    done, pending = await asyncio.wait(
        tasks,
        return_when=asyncio.FIRST_COMPLETED
    )

    winner = done.pop()

    print(f"Winner: {winner.result()}")

    # ยกเลิก Task ที่เหลือ
    print(f"Canceled {len(pending)} pending task(s)")
    for task in pending:
        task.cancel()

    await asyncio.gather(*pending, return_exceptions=True)


if __name__ == "__main__":
    asyncio.run(main())