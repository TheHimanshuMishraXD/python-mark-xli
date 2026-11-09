# exercise 10 
# use the request module to fetch the daily  news related to diffrent topics got to the newsapi.org
# and explore the various operation to build your application
# ===== DAILY NEWS APP =====

# 1. Technology
# 2. Sports
# 3. Business
# 4. Entertainment
# 5. Science

# Enter your choice: 1

# ===== TECHNOLOGY NEWS =====

# News 1:
# Title: ................
# Description: ...........
# Published At: ..........
# URL: ...................

# News 2:
# Title: ................
# ...
import requests
from bs4 import BeautifulSoup
url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=dea0cc03e4a94416b48d8b6f80b4e2e4'
req = requests.get(url)
print(req.text)
user_input = input("enter your choice of news category: ")
