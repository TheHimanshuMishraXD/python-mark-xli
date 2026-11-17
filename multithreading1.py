# Python mein Multithreading ka matlab hai ek hi program ke andar multiple threads ko use karke multiple
#  tasks ko concurrently execute karna.
import threading
import time
# indicate some task being done
def func(seconds):
    print(f"sleeping for {seconds} seconds")
    time.sleep(seconds)

time1 = time.perf_counter()
# #normal code
func(4)
func(2)
func(12)  
time2 = time.perf_counter()
print(time2-time1)
#code using thread
t1 = threading.Thread(target=func , args=[4])
t2 = threading.Thread(target=func,args=[3])
t3 = threading.Thread(target=func,args=[5])
t1.start()
t2.start()
t3.start()