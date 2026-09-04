import asyncio

async def api_call(url:str, delay:int):
    print(f"Fetching data from: {url}")
    await asyncio.sleep(delay)
    print(f"Data fetched from: {url}")
    return f"{url} data"

async def main():
#Creating tasks with gather to run multiple API calls/coroutines concurrently
 
  tasks=await asyncio.gather(
    api_call("https://api1.example.com",2),
    api_call("https://api2.example.com",3),
    api_call("https://api3.example.com",1))

  print("all API CALL completed")

asyncio.run(main())

#Another way of creating tasks with gather
#async def main():
    #urls = ["https://api1.example.com", "https://api2.example.com", "https://api3.example.com"]
    #tasks = [api_call(url) for url in urls]
    #results = await asyncio.gather(*tasks)
   