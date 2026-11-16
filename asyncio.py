# Python mein asyncio ek built-in module hai jo asynchronous programming ke liye use hota hai. Iski help se hum multiple tasks ko efficiently manage kar sakte hain,
#  bina har task ke complete hone ka wait kiye.
import time
import asyncio

async def function1():
    time.sleep(3)
    print("func 1")

async def function2():
    time.sleep(3)
    print("func 2")

async def function3():
    time.sleep(2)
    print("func 3")
async def main():
  await function1()
  await function2()
  await function3()