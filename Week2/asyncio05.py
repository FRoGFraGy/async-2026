# Program 5: Sequential Execution (The Wrong Way)
# Concept: Showing that simply awaiting one after another is still sequential (Synchronous behavior).
import asyncio
from time import time, ctime

async def serve_customer(name):
    print(f"{ctime()} -> Cooking for {name}...")
    await asyncio.sleep(1)  # Simulate a delay in serving the customer.
    print(f"{ctime()} -> Served {name}!")

async def main():
    start = time()

    await serve_customer("A")  # This will block until Alice is served.
    await serve_customer("B")    # This will block until Bob is served.

    #await asyncio.gather(
    #    serve_customer("A"),  # This will run concurrently with B
    #    serve_customer("B")   # This will run concurrently with A
    #)

    print(f"Total Time: {time() - start:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())  # This will execute the main coroutine and print the total time taken to serve both customers.