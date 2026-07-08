# Objective: Stop an ongoing execution prematurely by triggering a cancellation exception.
import asyncio
from time import ctime

async def background_loop():
    try:
        print(f"{ctime()} Worker: Starting long infinite process...")
        while True:#วนตลอดเวลา
            await asyncio.sleep(1)
            print(f"{ctime()} Worker: Still ticking...")
    except asyncio.CancelledError:
        # inject when the task.cancel() is expected to be called, we can handle the cancellation gracefully
        print(f"{ctime()} Worker: Interrupted! Executing clean-up logic before exit...")

async def main():
    task = asyncio.create_task(background_loop())
    await asyncio.sleep(2.5) # let the worker run for a while
    
    print(f"{ctime()} Main: Changing plans, canceling the worker task now!")
    task.cancel() # cancel the task, which will raise a CancelledError in the background_loop
    await asyncio.sleep(0.1) # wait a moment to let the cancellation propagate

asyncio.run(main())