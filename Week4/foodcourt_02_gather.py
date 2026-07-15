# foodcourt_02_gather.py
import asyncio
from time import ctime
from food_utils import send_order_to_kitchen

async def main():
    MY_STUDENT_ID = "65010001"
    print(f"{ctime()} | --- [Task 2] Practice using gather to queue multiple orders ---")
    
    # 1. Create a list of tasks for ordering different food items.
    tasks = [
        send_order_to_kitchen(MY_STUDENT_ID, "hainanese_chicken", "Chicken Rice Mixed"),
        send_order_to_kitchen(MY_STUDENT_ID, "noodle", "noodle"),
        send_order_to_kitchen(MY_STUDENT_ID, "steak", "steak")
    ]
    
    # 2. Use asyncio.gather to run all tasks concurrently and wait for their completion.
    results = await asyncio.gather(*tasks)
    
    # 3. Print the results of all orders once they are completed.
    for result in results:
        print(f"{ctime()} | [{result['status']}] Shop: '{result['shop']}' | '{result['menu']}'")

if __name__ == "__main__":
    asyncio.run(main())