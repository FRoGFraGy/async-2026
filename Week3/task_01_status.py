# Objective: Learn how to query the lifecycle status of a task object. ตรวจ lift cycle ของ task
import asyncio
from time import ctime

async def short_job():
    await asyncio.sleep(1)
    return "Success"

async def main():
    task = asyncio.create_task(short_job())
    
    # Check the task's status while still running
    print(f"{ctime()} Is task done? {task.done()}")          # expect False
    print(f"{ctime()} Is task canceled? {task.cancelled()}")  # expect False
    
    await task #wait for complete
    
    # Inspect status again after it finishes
    print(f"{ctime()} Is task done now? {task.done()}")      # expect True
    print(f"{ctime()} Is task canceled now? {task.cancelled()}") # expect False

asyncio.run(main())