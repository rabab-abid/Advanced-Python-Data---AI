import asyncio
import time

#First task
async def api_call(url:str, delay:int=3):
    print(f"Fetching data from: {url}")
    await asyncio.sleep(delay)
    print(f"Data fetched from: {url}")
  
async def execution():
   time.sleep(5)
   print("Execution completed")

async def transformation():
   asyncio.sleep(4)
   print("Transformation completed")

async def main():

  tasks=await asyncio.gather(
    api_call("https://api1.example.com"),
    execution(),
    transformation())

  print("all tasks completed")

asyncio.run(main())
