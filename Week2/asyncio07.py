# Program 7: Dual Tasks Concurrency
# Concept: Scheduling two distinct tasks concurrently and awaiting them individually without gather.
import asyncio
from time import time, ctime
from tracemalloc import start

async def cook_spaghetti(customer):
    print(f"{ctime()} -> Starting cooking for Customer {customer}...")
    await asyncio.sleep(1)  # Simulating a time-consuming task
    print(f"{ctime()} -> Finished cooking for Customer {customer}!")

async def main():
    start_time = time()

    # Creating tasks for each customer
    task_a = asyncio.create_task(cook_spaghetti("A"))
    task_b = asyncio.create_task(cook_spaghetti("B"))

    print(f"{ctime()} -> Main program can do other things while Tasks A and B run in the background.")

    await task_a  # Awaiting the completion of Task A
    await task_b  # Awaiting the completion of Task B

    print(f"Total Operation Time: {time() - start_time:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())  # This will execute the main coroutine and print the total time taken to serve the customers.