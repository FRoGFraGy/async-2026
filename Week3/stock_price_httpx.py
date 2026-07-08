# stock_price_httpx.py (เวอร์ชันสำหรับแจกเป็นโจทย์หรือแนวทางให้นักเรียนเขียน)
import asyncio
import httpx
from time import ctime

async def fetch_stock_price(server_name: str):
    """
    TODO: Assignment 3 - เขียนฟังก์ชันเชื่อมต่อ Mock Server ผ่านระบบเครือข่าย
    1. กำหนดเป้าหมายไปที่พอร์ต 8088 ตามสเปกเซิร์ฟเวอร์ของอาจารย์
    2. ใช้ httpx.AsyncClient() ดึงข้อมูลเพื่อไม่ให้เกิดการ Block สัญญาณ Event Loop
    3. นำข้อมูล JSON (server และ price_usd) มาจัดฟอร์แมตแสดงผล
    """
    url = f"http://127.0.0.1:8088/price/{server_name}"
    
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()
        return f"[{data['server']}] Price: {data['price_usd']} USD"

async def main():
    """
    TODO: จัดการส่งกลุ่ม Tasks ทำ Concurrency Racing บนเซิร์ฟเวอร์ย่อย Alpha, Beta, Gamma
    และปิดกั้นทรัพยากรตัวที่ค้างคา (pending) ทิ้งทันทีเมื่อมีผู้ชนะ
    """
    tasks = [
        asyncio.create_task(fetch_stock_price("Alpha"), name="Alpha"),
        asyncio.create_task(fetch_stock_price("Beta"), name="Beta"),
        asyncio.create_task(fetch_stock_price("Gamma"), name="Gamma"),
    ]

    print(f"{ctime()} Racing started...")

    done, pending = await asyncio.wait(
        tasks,
        return_when=asyncio.FIRST_COMPLETED
    )

    winner = done.pop()

    print(f"{ctime()} Winner: {winner.result()}")

    print(f"{ctime()} Canceling {len(pending)} pending task(s)...")

    for task in pending:
        print(f"Cancel -> {task.get_name()}")
        task.cancel()

    await asyncio.gather(*pending, return_exceptions=True)
    

if __name__ == "__main__":
    asyncio.run(main())