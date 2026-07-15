# foodcourt_03_wait_first.py
import asyncio
from asyncio import tasks
from time import ctime
from food_utils import send_order_to_kitchen

async def main():
    MY_STUDENT_ID = "65010001"
    print(f"{ctime()} | --- [Task 3] Practice using wait to queue multiple orders ---")
    
    # 1. Create a list of tasks for ordering different food items.
    tasks = [
    asyncio.create_task(send_order_to_kitchen(MY_STUDENT_ID, "hainanese_chicken", "Chicken Rice Mixed")),
    asyncio.create_task(send_order_to_kitchen(MY_STUDENT_ID, "pad_thai", "Pad Thai")),
    asyncio.create_task(send_order_to_kitchen(MY_STUDENT_ID, "sushi", "Sushi Platter"))
    ]
    
    # 2. Use asyncio.wait to run all tasks concurrently and wait for their completion.
    done, pending = await asyncio.wait(
        tasks,
        return_when=asyncio.FIRST_COMPLETED
    )    
    # 3. Print the results of the completed orders.
    print(f"{ctime()} | Canceling {len(pending)} pending order(s)...")
    for task in pending:
        task.cancel()

    await asyncio.gather(*pending, return_exceptions=True)

if __name__ == "__main__":
    asyncio.run(main())