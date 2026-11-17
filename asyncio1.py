# Python mein asyncio ek built-in module hai jo asynchronous programming ke liye use hota hai. Iski help se hum multiple tasks ko efficiently manage kar sakte hain,
#  bina har task ke complete hone ka wait kiye.
import time
import asyncio

async def function1():
    await asyncio.sleep(1)
    print("func 1")
    return "Harry"

async def function2():
    await asyncio.sleep(1)
    print("func 2")
    

async def function3():
    await asyncio.sleep(4)
    print("func 3")
async def main():
    L = await asyncio.gather(
        function1(),
        function2(),
        function3(),
    )
 print(L)
# asyncio.run(main())