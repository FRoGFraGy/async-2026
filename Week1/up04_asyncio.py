from time import sleep, ctime, time
import asyncio

async def update_cup_number(customer_name):
    print(f"{ctime()} | LCD: Processing for customer {customer_name}...")
    await asyncio.sleep(1)  # จำลองเวลาในการอัปเดตหมายเลขถ้วย
    print(f"{ctime()} | LCD: Done for customer {customer_name}.")

async def make_coffee(customer_name):
    print(f"{ctime()} | Making coffee for {customer_name}...")
    await asyncio.sleep(1)  # จำลองเวลาในการทำกาแฟ
    print(f"{ctime()} | Coffee ready for {customer_name}!")
    await update_cup_number(customer_name)

async def main():
    # คิวลูกค้า
    queue = ['A', 'B', 'C']
    start_time = time()
    print(f"{ctime()} | === Asyncio Coffee Machine ===")

    # สร้าง Task สำหรับแต่ละลูกค้า
    tasks = [make_coffee(customer) for customer in queue]

    # รอให้ Task ทั้งหมดเสร็จสิ้น
    await asyncio.gather(*tasks)

    duration = time() - start_time
    print(f"{ctime()} | Total time: {duration:0.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())