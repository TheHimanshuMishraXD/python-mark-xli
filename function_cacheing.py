# Function Caching in Python: Function caching is a technique in which the result of a function is stored so that when the same function is called again with the same arguments, the previously stored result is returned instead of recalculating it.

# Simple meaning: Ek baar function ka result calculate karke store kar lena, taaki same input dobara aane par calculation repeat na karni pade.

# Benefits:
# 1. Execution time reduce karta hai.
# 2. Repeated calculations avoid karta hai.
# 3. Program ki performance improve karta hai.
import functools
import time
@functools.lru_cache(maxsize=None)
def fx(n):
    time.sleep(5)
print(fx(20))