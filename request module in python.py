# # The Requests module in Python is an external library used to send HTTP requests and receive responses from web servers. 
# # It helps Python programs communicate with websites and APIs easily.
# import requests
# responses = requests.get("https://www.facebook.com")

# print(responses.text)  # This will print the HTML content of the Google homepage

import requests
from bs4 import BeautifulSoup


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
# print(r.text) 


# bs4 ---> BeautifulSoup (bs4) Python ki third-party library hai,
#  jiska use Web Scraping mein website ke HTML data se required information extract karne ke liye hota hai.

# soup = BeautifulSoup(r.text , 'html.parser')
# for heading in soup.find_all('h2'): 
# # print(soup.prettify )
#     print(heading.text)     

# Your progress

# 0/6



# [ ] Website ka HTML fetch karo using requests.get().
# [ ] HTML content print karo using r.text.
# [ ] BeautifulSoup se HTML parse karo.
# [ ] Saare h2 headings find karo.
# [ ] Saari book titles print karo.
# [ ] Saari book prices print karo.



url = "https://books.toscrape.com/"
r = requests.get(url)
print(r.text) # so this is the html content of the website bro


soup = BeautifulSoup(r.text , 'html,parser')
p = price
for heading in soup.find_all('h2'):
    print(heading.text)
    print(p.text)
    