# นักเรียนต้องเลือกใช้ asyncio.wait() พร้อมออปชัน return_when=asyncio.FIRST_COMPLETED เท่านั้น (หากใครใช้ gather หรือ wait_for จะไม่ตรงสเปกเงื่อนไขการแข่งส่งข้อมูล)
import asyncio
from time import ctime

async def fetch_stock_price(server_name, delay):
    """Simulate fetching stock price from a server with a given delay."""
    await asyncio.sleep(delay)  # Simulate network latency
    price = 150  # Mock price based on delay for demonstration
    print(f"{ctime()} [{server_name}] Price: {price} USD")
    return price

async def main():
    """Main function to run the stock price fetching tasks concurrently."""
    tasks = [
        asyncio.create_task(fetch_stock_price("Alpha", 3.0),name="Alpha"),
        asyncio.create_task(fetch_stock_price("Beta", 0.8),name="Beta"),
        asyncio.create_task(fetch_stock_price("Gamma", 1.5),name="Gamma"),
    ]

    # Wait for the first task to complete
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)

    completed_task = done.pop()

    print(f"{ctime()} Winner Result: [{completed_task.get_name()}] price: {completed_task.result()} USD")
    
    print(f"{ctime()} Canceling {len(pending)} pending task(s)...")

    for ongoing_task in pending:
        ongoing_task.cancel()
    
if __name__ == "__main__":
    asyncio.run(main())