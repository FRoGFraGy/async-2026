# Program 8: Task Interleaving (Context Switching)
# Concept: Watching a single thread switch back and forth between two different workflows using create_task.
import asyncio
from time import time, ctime

async def kitchen_crew():
    print(f"{ctime()} -> [Chef] puts noodle in boiling water...")
    await asyncio.sleep(1)  # Simulating a time-consuming task
    print(f"{ctime()} -> [Chef] strains the noodles!")

async def bar_crew():
    print(f"{ctime()} -> [Bar] starts grinding coffee beans...")
    await asyncio.sleep(1)  # Simulating a time-consuming task
    print(f"{ctime()} -> [Bar] pours espresso shots!")

async def main():
    # Creating tasks for kitchen and bar crews
    task_kitchen = asyncio.create_task(kitchen_crew())
    task_bar = asyncio.create_task(bar_crew())

    await task_kitchen  # Awaiting the completion of Kitchen Crew Task
    await task_bar      # Awaiting the completion of Bar Crew Task

if __name__ == "__main__":
    asyncio.run(main())  # This will execute the main coroutine and print the interleaved operations of both crews.