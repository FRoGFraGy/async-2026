import asyncio

# Coroutine สำหรับดึงราคาหุ้น
async def fetch_stock_price(server_name, delay):
    await asyncio.sleep(delay)
    return f"[{server_name}] Price: 150 USD"

# ฟังก์ชันหลัก
async def main():

    # สร้าง Task ทั้ง 3 ตัว
    task_alpha = asyncio.create_task(fetch_stock_price("Alpha", 3.0))
    task_beta = asyncio.create_task(fetch_stock_price("Beta", 0.8))
    task_gamma = asyncio.create_task(fetch_stock_price("Gamma", 1.5))

    tasks = [task_alpha, task_beta, task_gamma]

    # รอจนกว่าจะมี Task แรกทำงานเสร็จ
    done, pending = await asyncio.wait(
        tasks,
        return_when=asyncio.FIRST_COMPLETED
    )

    # แสดงผลเซิร์ฟเวอร์ที่ตอบเร็วที่สุด
    for task in done:
        print(f"Winner Result: {task.result()}")

    # ยกเลิก Task ที่เหลือ
    print(f"Cleaning up {len(pending)} tasks...")
    for task in pending:
        task.cancel()

    # รอให้การยกเลิกเสร็จสมบูรณ์
    await asyncio.gather(*pending, return_exceptions=True)

# เริ่มโปรแกรม
asyncio.run(main())