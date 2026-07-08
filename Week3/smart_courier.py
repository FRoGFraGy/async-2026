# Delivery System): นักศึกษาต้องเขียน try...except CancelledError ได้ถูกต้อง 
# และใช้ .get_name(), .cancel(), และ .cancelled() ได้
import asyncio
from time import ctime
async def delivery_task(package_id, duration):
    """Simulate a delivery task with a given package ID and duration."""
    try:
        print(f"{ctime()} Courier Started delivering {package_id}...")
        # Simulate a long-running task
        await asyncio.sleep(duration)
        print(f"{ctime()} Courier: Package {package_id} Delivered!")
    except asyncio.CancelledError:
        print(f"{ctime()} Delivery Canceled! Returning package to warehouse.")
        raise  # Re-raise the exception to propagate cancellation

async def main():
    """Main function to run the delivery tasks concurrently."""

    task = asyncio.create_task(delivery_task("P001", 5), name="Express-Courier")
    
    await asyncio.sleep(2)  # Let the task run for a while
    print(f"{ctime()} Check task '{task.get_name()}'. It is done? {task.done()}")
    task.cancel()
    print(f"{ctime()} Taking too long! Canceling task...")
    # Wait for the first task to complete
    done, pending = await asyncio.wait([task], return_when=asyncio.FIRST_COMPLETED)
    
    print(f"{ctime()} Final verify: Is task officially canceled? {task.cancelled()}")
    
    # Wait for all tasks to finish
    await asyncio.gather(*pending, return_exceptions=True)

if __name__ == "__main__":
    asyncio.run(main())