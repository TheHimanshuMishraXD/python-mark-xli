import time
def usingwhile():
    i = 0
    while i < 5:
        i = i+1
        print(i)

def usingfor():
    for i in range(18):
      print(i)
init = time.time()

usingwhile()
print(time.time()-init)  
usingfor()
print(time.time()-init)  # ye batata hai ki apka program kitne time me run kia hai