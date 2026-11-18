# Python mein Multithreading ka matlab hai ek hi program ke andar multiple threads ko use karke multiple
#  tasks ko concurrently execute karna.
import threading
import time
from concurrent.futures import ThreadPoolExecutor  # ye help karta hai jab aap bulk me bahut saare task execute krna chahte ho  to usme help krta hai
# indicate some task being done
def func(seconds):
    print(f"sleeping for {seconds} seconds")
    time.sleep(seconds)
def main():
    time1 = time.perf_counter()
    # #normal code
    # func(4)
    # func(2)
    # func(12)  
    # time2 = time.perf_counter()
    # print(time2-time1)
    #code using thread
    t1 = threading.Thread(target=func , args=[4])
    t2 = threading.Thread(target=func,args=[3])
    t3 = threading.Thread(target=func,args=[5])
    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()
    #calculating time   
    time2 = time.perf_counter()
    print(time2-time1)

def poolingDemo():
    with ThreadPoolExecutor() as executor:
    #   future = executor.submit(func , 3)
    #   print(future.result())
    #   future = executor.submit(func , 2)
    #   print(future.result())
    #   future = executor.submit(func , 5)
    #   print(future.result())
    # isko use karne ka ik or syntax hai using map
        l = [3,2,4,5,6]
        results = executor.map(func,1)
        for result in results:
            print(result)



poolingDemo()