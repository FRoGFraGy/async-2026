# Objective: Implement complex processing workflows based on task fulfillment conditions.
import asyncio
from time import ctime

async def network_probe(server_name, delay):
    await asyncio.sleep(delay)
    return f"Ping successful: {server_name}"

async def main():
    # asyncio.wait() allows us to wait for a set of tasks to complete based on specific conditions
    tasks = {
        asyncio.create_task(network_probe("Primary-Server", 2.0)),
        asyncio.create_task(network_probe("Backup-Server-1", 0.5)),
        asyncio.create_task(network_probe("Backup-Server-2", 1.0))
    }
    
    # break execution when the first task completes, returning two sets: done and pending
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    
    print(f"{ctime()} Count of Tasks Done: {len(done)}")       # expect 1
    print(f"{ctime()} Count of Tasks Pending: {len(pending)}") # expect 2
    
    for finished_task in done:
        print(f"{ctime()} Fastest Task Result: {finished_task.result()}")
        
    # clean up remaining pending tasks to avoid memory leaks or dangling operations
    for ongoing_task in pending:
        ongoing_task.cancel()

asyncio.run(main())