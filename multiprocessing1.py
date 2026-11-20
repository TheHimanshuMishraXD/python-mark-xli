import multiprocessing
import concurrent.futures   
import requests
def downloadfile(url,name):
    print(f"started downloading {name}")
    response = requests.get(url)
    open(f"{name}.jpg","wb").write(response.content)
    print(f"finished downloading {name}")


 if __name__ == "__main__": 
url = "https://picsum.photos/200/300"
  pros = []
  for i in range(5):
    # downloadfile(url, i)
    p =  multiprocessing.Process(target=downloadfile, args = [url, i])
    p.start()
    pros.append(p)


  
  for p in pros:  
    p.join() 

with concurrent.futures.ProcessPoolExecutor() as executor:
    l1 = [url for i in range(5)]
    l2 =  [i for i in range(6)]
    results = executor.map(downloadfile,l1,l2)
    for r in results:
        print(r)
