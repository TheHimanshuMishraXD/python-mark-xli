# exercise 10 
# use the request module to fetch the daily  news related to diffrent topics got to the newsapi.org
# and explore the various operation to build your application
import requests
from bs4 import BeautifulSoup
url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=dea0cc03e4a94416b48d8b6f80b4e2e4'
req = requests.get(url)
