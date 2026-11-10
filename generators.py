# A Generator in Python is a special type of function that returns values one at a time using 
# the yield keyword instead of returning all values at once using return.

def my_generator():
    for i in range(5):
        yield i

gen = my_generator()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
