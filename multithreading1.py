# # Python mein Multithreading ka matlab hai ek hi program ke andar multiple threads ko use karke multiple
# #  tasks ko concurrently execute karna.
# import threading
# import time
# from concurrent.futures import ThreadPoolExecutor  # ye help karta hai jab aap bulk me bahut saare task execute krna chahte ho  to usme help krta hai
# # indicate some task being done
# def func(seconds):
#     print(f"sleeping for {seconds} seconds")
#     time.sleep(seconds)
# def main():
#     time1 = time.perf_counter()
#     # #normal code
#     # func(4)
#     # func(2)
#     # func(12)  
#     # time2 = time.perf_counter()
#     # print(time2-time1)
#     #code using thread
#     t1 = threading.Thread(target=func , args=[4])
#     t2 = threading.Thread(target=func,args=[3])
#     t3 = threading.Thread(target=func,args=[5])
#     t1.start()
#     t2.start()
#     t3.start()

#     t1.join()
#     t2.join()
#     t3.join()
#     #calculating time   
#     time2 = time.perf_counter()
#     print(time2-time1)

# def poolingDemo():
#     with ThreadPoolExecutor() as executor:
#     #   future = executor.submit(func , 3)
#     #   print(future.result())
#     #   future = executor.submit(func , 2)
#     #   print(future.result())
#     #   future = executor.submit(func , 5)
#     #   print(future.result())
#     # isko use karne ka ik or syntax hai using map
#      l = [3,2,4,5,6]
#      results = executor.map(func,l)
#      for result in results:
#         print(result)  #agar hame bohot saare urls se download krna hai ya iski list ho to aise krge



# poolingDemo()
# Task 1 – Basic Threading
# Easy

# Ek function banao jo kisi number ke liye 1 se 10 tak multiplication table print kare.
# - 3 threads create karo.
# - Tables of 2, 5 and 10 execute karo.
# - start() aur join() use karo.
import threading
import time
# def table(n):
#     for i in range (2,11):
#         print(f"{n}*{i} = {n*i}")
# t1 =  threading.Thread(target=table, args=[2])
# t1.start()
# t1.join()
# print("for 2 is done")
# ##for 5
# def forfive(n):
#     for i in range (2,11):
#         print(f"{n}*{i} = {n*i}")
# t1 = threading.Thread(target=forfive,args=[5])
# t1.start()
# t1.join()
# print("for  five it it totally done")

# def forten(n):
#     for i in range(2,11):
#         print(f"{i} * {n} = {i*n}")

# tq = threading.Thread(target=forten,args=[10])
# tq.start()
# tq.join()
# print("for ten it is done")

def table(n):
    for i in range(2,11):
        print(f"{i} * {n} = {i*n}")

t1 = threading.Thread(target=table,args=[2])
t2 = threading.Thread(target=table,args=[5])