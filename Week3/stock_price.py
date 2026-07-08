import asyncio
from time import ctime

# Coroutine สำหรับดึงข้อมูลราคาหุ้นจากเซิร์ฟเวอร์
async def fetch_stock_price(server_name, delay):
    await asyncio.sleep(delay)  # จำลองเวลาตอบสนองของเซิร์ฟเวอร์
    return f"[{server_name}] Price: 150 USD"

# Main Coroutine
async def main():
    # สร้าง Task ทั้ง 3 ตัวให้ทำงานพร้อมกัน
    tasks = [
        asyncio.create_task(
            fetch_stock_price("Alpha", 3.0),
            name="Alpha"
        ),
        asyncio.create_task(
            fetch_stock_price("Beta", 0.8),
            name="Beta"
        ),
        asyncio.create_task(
            fetch_stock_price("Gamma", 1.5),
            name="Gamma"
        ),
    ]

    print(f"{ctime()} Waiting for the fastest server...\n")

    # รอจนกว่าจะมี Task ตัวแรกเสร็จ
    done, pending = await asyncio.wait(
        tasks,
        return_when=asyncio.FIRST_COMPLETED
    )

    # ดึง Task ที่เสร็จแล้ว
    winner = done.pop()

    # แสดงผลลัพธ์ของเซิร์ฟเวอร์ที่ชนะ
    print(f"{ctime()} Winner Result: {winner.result()}")

    # ยกเลิก Task ที่ยังทำงานอยู่
    print(f"{ctime()} Canceling {len(pending)} pending task(s)...")

    for task in pending:
        print(f"Cancel -> {task.get_name()}")
        task.cancel()

    # รอให้การยกเลิกเสร็จสมบูรณ์
    await asyncio.gather(*pending, return_exceptions=True)

    print(f"{ctime()} All remaining tasks have been canceled.")

# เริ่มโปรแกรม
if __name__ == "__main__":
    asyncio.run(main())