import multiprocessing
import requests
def downloadfile(url,name):
    response = requests.get(url)
    open(f"{name}.jpg","wb").write(response.content)
    pass
url = ["https://picsum.photos/200/300"]
for _ in range(5):
    downloadfile(url, i)