# Objective: Extract returned data safely and inspect crashed tasks without breaking the main loop. เช็คว่า fail ไหม ได้ค่าอะไรมา
import asyncio
from time import ctime

async def division_worker(a, b):
    await asyncio.sleep(0.5)
    return a / b # This will raise a ZeroDivisionError if b = 0

async def main():
    task_success = asyncio.create_task(division_worker(10, 2))
    task_fail = asyncio.create_task(division_worker(10, 0))

    # wait for a moment to let tasks complete
    await asyncio.sleep(1)
    
    # retrieve the result of the successful task safely
    if task_success.done() and not task_success.exception():
        print(f"{ctime()} Task Success Result: {task_success.result()}") # expect 5.0
        
    # extract the exception from the failed task safely
    if task_fail.done():
        print(f"{ctime()} Task Fail Exception: {type(task_fail.exception()).__name__}") # expect ZeroDivisionError

asyncio.run(main())