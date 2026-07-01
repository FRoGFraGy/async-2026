# Program 2: The Coroutine Object
# Concept: Seeing that calling an async def function creates an "Object" but does not execute it yet.
import asyncio

async def great():
    print("Hello!")

coro_object = great()  # This creates a coroutine object but does not execute it yet.

print(type(coro_object))  #output <class 'coroutine'>

coro_object  # This will execute the coroutine and print "Hello!"