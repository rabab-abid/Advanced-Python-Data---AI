#Normal Synchronous API call function

import time

def api_call():
    time.sleep(3)
    return "orders data"

def execute():
    print("Executing API Call")
    result = api_call()
    print(f"API Response: {result}")

execute()

#Async API call Coroutine function

import asyncio

async def api_call():
    await asyncio.sleep(3)
    return "orders data"

async def execute():
    print("Executing API Call")
    result = await api_call()
    print(f"API Response: {result}")

asyncio.run(execute())


