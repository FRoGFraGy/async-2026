import asyncio
import httpx

BASE_URL = "http://172.16.2.117:8088"
STUDENT_ID = "6710301049"

LIGHT_ORDER = ["light_1", "light_2", "light_3", "light_4"]

async def turn_on(client: httpx.AsyncClient, light_id: str):
    print(f"Turning ON {light_id} ...")
    resp = await client.post(
        f"{BASE_URL}/api/{STUDENT_ID}/lights/{light_id}",
        json={"status": "ON"},
    )
    resp.raise_for_status()
    print(f"  -> {light_id} is now ON")

async def turn_oFF(client: httpx.AsyncClient, light_id: str):
    print(f"Turning OFF {light_id} ...")
    resp = await client.post(
        f"{BASE_URL}/api/{STUDENT_ID}/lights/{light_id}",
        json={"status": "OFF"},
    )
    resp.raise_for_status()
    print(f"  -> {light_id} is now OFF")

async def main():
    async with httpx.AsyncClient(timeout=30.0) as client:

        for light_id in LIGHT_ORDER:
            await turn_on(client, light_id)

        #for light_id in LIGHT_ORDER:
        #    await turn_oFF(client, light_id)

if __name__ == "__main__":
    asyncio.run(main())