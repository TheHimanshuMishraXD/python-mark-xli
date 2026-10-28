import time
def usingwhile():
    i = 0
    while i < 5:
        i = i+1
        print(i)

def usingfor():
    for i in range(5):
      print(i)
init = time.time()

usingwhile()
print(time.time()-init)
usingfor()