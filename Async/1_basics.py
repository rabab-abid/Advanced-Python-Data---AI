import asyncio
import time

#Coroutine function
async def main():
    print("Hello")  #First task is executed by thread
    await asyncio.sleep(3) #Thread is idle here
    print("World") #Event Manager will not let the thread sit idle & this task is executed right after thread is idle

#Run Coroutine function
asyncio.run(main())