# Program 9: Dynamically Tracking Tasks in a List
# Concept: Managing multiple generated tasks dynamically by appending them into a standard Python list.
import asyncio
from time import time, ctime

async def serve_customer(name):
    print(f"{ctime()} -> Handling Customer {name}...")
    await asyncio.sleep(1)  # Simulating a time-consuming task
    print(f"{ctime()} -> Done Customer {name}!")

async def main():
    start_time = time()
    customers = ["A", "B", "C", "D"]  # List of customers to serve
    task_list = []  # List to hold the tasks

    for name in customers:
        t = asyncio.create_task(serve_customer(name))  # Create a task for each customer
        task_list.append(t)  # Append the task to the list

    for t in task_list:
        await t  # Await each task to ensure they complete

    print(f"Served all {len(customers)} customers in {time() - start_time:.2f} seconds.")

if __name__ == "__main__":
    asyncio.run(main())  # This will execute the main coroutine and print the total time taken to serve all customers.