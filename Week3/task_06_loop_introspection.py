# Objective: Introspect runtime contexts and monitor open workload queues on the active loop.
import asyncio
from time import ctime

async def dynamic_job(number):
    await asyncio.sleep(1.0)

async def main():
    # check the current task's name in the active loop
    me = asyncio.current_task()
    me.set_name("Main-Coordinator")
    print(f"{ctime()} Active Execution Context Name: {me.get_name()}")
    
    # spawn multiple background jobs and label them for easier introspection
    tasks = [asyncio.create_task(dynamic_job(i), name=f"Job-{i}") for i in range(3)]
    
    # peek inside the active loop to see all running tasks
    all_active = asyncio.all_tasks()
    print(f"{ctime()} Total Active Tasks inside Loop: {len(all_active)}")
    for t in all_active:
        print(f"{ctime()}  -> Active Queue Item: {t.get_name()}")

    await asyncio.sleep(1.1) # flush the queue to let all jobs complete

asyncio.run(main())