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

# import multiprocessing
# import requests

# def tables(n):
#     for i in range(2,11):
#         print(f"{i} * {n} = {i*n}")

# if __name__ == "__main__":

#     p1 = multiprocessing.Process(target = tables , args = [2])
#     p2 = multiprocessing.Process(target = tables , args = [5])
#     p3 = multiprocessing.Process(target = tables , args = [10])

#     p1.start()
#     p2.start()
#     p3.start()

#     p1.join()
#     p2.join()
#     p3.join()
     

#     print("all tables printed successfully")

# Task 2: Multiprocessing File Creator
# Intermediate
# Ek function banao create_file(name).

# Requirements:
# - 5 processes create karo.
# - Har process ek alag .txt file create kare.
# - Files ke naam file1.txt se file5.txt tak hon.
# - Har file mein apna naam aur process completion message likho.
# - join() use karo.

import requests
import multiprocessing

def create_file(name):
    with open(f"{name}", "w") as f:
      f.write(f"{name} the file process is completed successfully")

      if __name__ == "__main__":
      p1 = multiprocessing.Process(target=create_file,args=["file2.txt"])
      p2 = multiprocessing.Process(target=create_file,args=["file3.txt"])
      p3 = multiprocessing.Process(target=create_file,args=["file4.txt"])
      p4 = multiprocessing.Process(target=create_file,args=["file5.txt"])
      p5 = multiprocessing.Process(target=create_file,args=["file6.txt"])


      p1.join()
      p2.join()
      p3.join()
      p4.join()
      p5.join()
  