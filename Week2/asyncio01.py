# Program 1: The First Coroutine Function
# Concept: Understanding async def and how it differs from a normal function.
import asyncio

#A regular function uses def An async function uses async def.
#This defines a coroutine function.

async def great():
    print("Hello from Coroutine!")

print(type(great))  #output <class 'function'>