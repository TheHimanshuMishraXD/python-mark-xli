# Python mein Multithreading ka matlab hai ek hi program ke andar multiple threads ko use karke multiple
#  tasks ko concurrently execute karna.
import threading
import time
# indicate some task being done
def func():
    print(f"sleeping")
    time.sleep(seconds)