import multiprocessing
import threading
import asyncio
from time import sleep, time, ctime

async def greet_diners(customer):
    print(f"{ctime()} Greeting for Customer-{customer}...")
    await asyncio.sleep(1)  # Simulating a time-consuming task
    print(f"{ctime()} Greeting for Customer-{customer}...Done!")

async def customer_private_workflow(customer):
    #take_order(customer)
    print(f"{ctime()} [Thread-{customer}] Taking Order ...")
    await asyncio.sleep(1)  # Simulating a time-consuming task
    print(f"{ctime()} [Thread-{customer}] Taking Order ...Done!")


    print(f"{ctime()} [Thread-{customer}] Cooking Spaghetti ...")
    await asyncio.sleep(1)  # Simulating a time-consuming task
    print(f"{ctime()} [Thread-{customer}] Cooking Spaghetti ...Done!")

    print(f"{ctime()} [Thread-{customer}] Manage Bar for Drink  ...")
    await asyncio.sleep(1)  # Simulating a time-consuming task
    print(f"{ctime()} [Thread-{customer}] Manage Bar for Drink  ...Done!")
    print(f"{ctime()} [Thread-{customer}] All served!")

async def main():
    customers = ["A", "B", "C"]  # List of customers to serve
    start_time = time()

    for customer in customers:
        await greet_diners(customer)
        
    print(f"\n{ctime()} -> All customers greeted. Splitting into individual tasks for private workflows...\n")

    tasks = []
    for customer in customers:
        task = asyncio.create_task(customer_private_workflow(customer))
        tasks.append(task)

    await asyncio.gather(*tasks)  # Wait for all tasks to complete

    duration = time() - start_time
    print(f"\n{ctime()} Finished Entire Restaurant Operation in {duration:.2f} seconds.")

if __name__ == "__main__":
    asyncio.run(main())  # This will execute the main coroutine and print the total time taken to serve all customers.