import asyncio
import httpx

BASE_URL = "http://127.0.0.1:8088"

async def fetch_data(endpoint):
    url = f"{BASE_URL}/{endpoint}"

    try:
        async with httpx.AsyncClient(timeout=5) as client:
            response = await client.get(url)
            response.raise_for_status()
            return response.json()

    except httpx.ConnectError:
        print("Cannot connect to server")

    except httpx.TimeoutException:
        print("Request timeout")

    except httpx.HTTPStatusError as e:
        print("HTTP Error:", e.response.status_code)

    return None

async def main():
    data = await fetch_data("price/Beta")

    if data:
        print(data)

if __name__ == "__main__":
    asyncio.run(main())