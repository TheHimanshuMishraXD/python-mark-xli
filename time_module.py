import time
# def usingwhile():
#     i = 0
#     while i < 5:
#         i = i+1
#         print(i)

# def usingfor():
#     for i in range(8):
#       print(i)
# init = time.time()

# usingwhile()
# print(time.time()-init)  
# usingfor()
# print(time.time()-init)  # ye batata hai ki apka program kitne time me run kia hai

# print(4)
# time.sleep(5)
# print("this is printed after 3 seconds")  #iska use ye hai ki ye program itne time baad chlega


t = time.localtime()

formatted_time = time.strftime("%y-%m-%d %H %M %S",t)
print(formatted_time)