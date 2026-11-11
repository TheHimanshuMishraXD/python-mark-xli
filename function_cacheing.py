# Function Caching in Python: Function caching is a technique in which the result of a function is stored so that when the same function is called again with the same arguments, the previously stored result is returned instead of recalculating it.

# Simple meaning: Ek baar function ka result calculate karke store kar lena, taaki same input dobara aane par calculation repeat na karni pade.

# Benefits:
# 1. Execution time reduce karta hai.
# 2. Repeated calculations avoid karta hai.
# 3. Program ki performance improve karta hai.
from functools import lru_cache
import time
@lru_cache(maxsize=None)
def fx(n): 
    time.sleep(5)
    return n*5

print(fx(20))
print('done for 20')
print(fx(6))
print('done for 6')
print(fx(4))
print('done for 4')


print(fx(20))
print('done for 20')        
print(fx(6))    
print('done for 6')
print(fx(4))
print('done for 4')
# so basically baat ye hai ki idhr ye suruwaat ke 20,6,4 --> ka result nikalta hai ----> and jo second ki same values hai unka
# result turant compute kr deta hai q ki wo values uske cache me stored hai aur  ye chiz usko pata hai to wo isko turant caluclate
# kr leta hai
# jisse ye memoize kar leta hai calculation ko  



# form here we are doing some tasks on the basis of given exercise
# Task 1: Basic Memoization
# Ek function cube(n) banao jo:
# 1. Number ka cube return kare.
# 2. time.sleep(3) use karo.
# 3. @lru_cache(maxsize=None) lagao.
# 4. Same number ko 3 baar call karo.
# 5. Observe karo ki first call slow aur baaki instant hain ya nahi.
# Example calls:
# print(cube(4))print(cube(4))print(cube(4))

from functools import lru_cache
import time 
@lru_cache(maxsize=None)
def dx(n):
    time.sleep(3):
    return n    