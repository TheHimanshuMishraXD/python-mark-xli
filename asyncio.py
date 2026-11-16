# Python mein asyncio ek built-in module hai jo asynchronous programming ke liye use hota hai. Iski help se hum multiple tasks ko efficiently manage kar sakte hain,
#  bina har task ke complete hone ka wait kiye.
import time

def function1():
    time.sleep(3)
    print("func 1")

def function2():
    time.sleep(3)
    print("func 2")

def function3():
    time.sleep(3)
    print("func 3")

function1()
function2()