# # import multiprocessing
# # import concurrent.futures   
# # import requests
# # def downloadfile(url,name):
# #     print(f"started downloading {name}")
# #     response = requests.get(url)
# #     open(f"{name}.jpg","wb").write(response.content)
# #     print(f"finished downloading {name}")


# #  if __name__ == "__main__": 
# # url = "https://picsum.photos/200/300"
# #   pros = []
# #   for i in range(5):
# #     # downloadfile(url, i)
# #     p =  multiprocessing.Process(target=downloadfile, args = [url, i])
# #     p.start()
# #     pros.append(p)


  
# #   for p in pros:  
# #     p.join() 

# # with concurrent.futures.ProcessPoolExecutor() as executor:
# #     l1 = [url for i in range(5)]
# #     l2 =  [i for i in range(6)]
# #     results = executor.map(downloadfile,l1,l2)
# #     for r in results:
# #         print(r)



# Task 1: Multiprocessing Tables
# Easy
# Ek program banao jo 3 alag-alag processes mein tables print kare.

# Requirements:
# 1. table(n) naam ka function banao.
# 2. 3 processes create karo.
# 3. First process table of 2 print kare.
# 4. Second process table of 5 print kare.
# 5. Third process table of 10 print kare.
# 6. join() se sabhi processes complete hone ka wait karo.
# Expected output concept:

import multiprocessing
import requests

def tables(n):
    for i in range(2,11):
        print(f"{i} * {n} = {i*n}")

if __name__ == "__main__":
    
    p1 = multiprocessing.process(target = tables , args = [2])
    p2 = multiprocessing.process(target = tables , args = [5])
    p3 = multiprocessing.process(target = tables , args = [10])

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()
     

    print("all tables printed successfully")