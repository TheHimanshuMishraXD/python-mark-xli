# # The Requests module in Python is an external library used to send HTTP requests and receive responses from web servers. 
# # It helps Python programs communicate with websites and APIs easily.
# import requests
# responses = requests.get("https://www.facebook.com")

# print(responses.text)  # This will print the HTML content of the Google homepage

import requests

# data = {
#     "title": "himanshu bhai",
#     "body": "bar",
#     "userId": 12
# } 
# headers = {
#     "Content-Type": "application/json; charset=UTF-8"
# }

# url = "https://jsonplaceholder.typicode.com/posts"
# response = requests.post(url , headers =headers , json = data)
# print(response.text)                  
            

# scraping ke liye use hone wala like :-

url =  "https://www.codewithharry.com/blog"
r = requests.get(url)
print(r.text)



# bs4 ---> BeautifulSoup (bs4) Python ki third-party library hai,
#  jiska use Web Scraping mein website ke HTML data se required information extract karne ke liye hota hai.

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_dov , 'html.parser')
print(soup.prettify  )