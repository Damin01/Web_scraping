#IMPORT LIBRARIES
from bs4 import BeautifulSoup
import requests

def get_source(url):
    return BeautifulSoup(requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, verify=False).text, 'html.parser')

soup = get_source('https://www.youtube.com/@AtriocClips/videos')

for entry in soup.find_all("entry"):
   for title in entry.find_all("title"):
      print(title.text)
   for link in entry.find_all("link"):
      print(link["href"])
   for name in entry.find_all("name"):
      print(name.text)
   for pub in entry.find_all("published"):
      print(pub.text)

