# foodcourt_03_wait_first.py
import asyncio
from asyncio import tasks
from time import time, ctime
from food_utils import send_order_to_kitchen

async def main():
    MY_STUDENT_ID = "6710301049"
    print(f"{ctime()} | --- [Task 3] Practice using wait (FIRST_COMPLETED)")
    start_time = time()
    # 1. Create a list of tasks for ordering different food items.
    tasks = [
    asyncio.create_task(send_order_to_kitchen(MY_STUDENT_ID, "hainanese_chicken", "Chicken Rice Thigh")),
    asyncio.create_task(send_order_to_kitchen(MY_STUDENT_ID, "noodle", "Wonton Noodles")),
    asyncio.create_task(send_order_to_kitchen(MY_STUDENT_ID, "steak", "Sizzling Steak"))
    ]
    
    # 2. Use asyncio.wait to run all tasks concurrently and wait for their completion.
    done, pending = await asyncio.wait(
        tasks,
        return_when=asyncio.FIRST_COMPLETED
    )    

    fastest_task = done.pop()

    print(f"{ctime()} | winner served dish: Shop: {fastest_task.result()['shop']} | Menu: {fastest_task.result()['menu']}")

    # 3. Print the results of the completed orders.
    print(f"{ctime()} | Cleaning up: Canceling {len(pending)} remaining pending orders...")
    for task in pending:
        task.cancel()

    await asyncio.gather(*pending, return_exceptions=True)
    print(f"{ctime()} | Total waiting time for the first dish: {time() - start_time:.2f} seconds.")

if __name__ == "__main__":
    asyncio.run(main())