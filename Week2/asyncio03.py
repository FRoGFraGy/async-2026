# Program 3: The Event Loop (asyncio.run)
# Concept: Using the Event Loop to actually execute a Coroutine Object.
import asyncio

async def great():
    print("Hello from the Event Loop!")

if __name__ == "__main__":
    coro_object = great()  # This creates a coroutine object but does not execute it yet.

    asyncio.run(coro_object)  # This will execute the coroutine and print "Hello from the Event Loop!"