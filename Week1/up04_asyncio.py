from time import sleep, ctime, time
import asyncio
import threading

async def update_cup_number(customer_name):
    print(f"{ctime()} | กำลังอัปเดตหมายเลขถ้วยสำหรับลูกค้า {customer_name} ...")
    await asyncio.sleep(1)  # จำลองเวลาในการอัปเดตหมายเลขถ้วย

async def make_coffee(customer_name):
    print(f"{ctime()} | กำลังทำกาแฟให้ลูกค้า {customer_name} ...")
    await asyncio.sleep(1)  # จำลองเวลาในการทำกาแฟ
    print(f"{ctime()} | กาแฟสำหรับลูกค้า {customer_name} พร้อมแล้ว")
    await update_cup_number(customer_name)

async def main():
    # คิวลูกค้า
    queue = ['A', 'B', 'C']
    start_time = time()

    # สร้าง Task สำหรับแต่ละลูกค้า
    tasks = [make_coffee(customer) for customer in queue]

    # รอให้ Task ทั้งหมดเสร็จสิ้น
    await asyncio.gather(*tasks)

    duration = time() - start_time
    print(f"{ctime()} | ใช้เวลารวมทั้งหมด: {duration:0.2f} วินาที")

if __name__ == "__main__":
    asyncio.run(main())