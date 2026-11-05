# # The Requests module in Python is an external library used to send HTTP requests and receive responses from web servers. 
# # It helps Python programs communicate with websites and APIs easily.
# import requests
# responses = requests.get("https://www.facebook.com")

# print(responses.text)  # This will print the HTML content of the Google homepage

import 
url = "https://jsonplaceholder.typicode.com/posts"
response = requests.post(url , headers =headers , json = data)
print(response.text) 
