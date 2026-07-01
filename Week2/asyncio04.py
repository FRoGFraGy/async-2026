# Program 4: The await Keyword
# Concept: Pausing a coroutine to let another operation finish using await.
import asyncio
from time import ctime

async def main():
    print(f"{ctime()} -> Task Started!")

    await asyncio.sleep(1)  # This will pause the coroutine for 1 second.

    print(f"{ctime()} -> Task Finished!")

if __name__ == "__main__":
    asyncio.run(main())  # This will execute the main coroutine and print the start and finish times.
