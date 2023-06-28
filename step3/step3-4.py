import requests
from bs4 import BeautifulSoup
import urllib

load_url = 'https://creaters-you.com/'
html = requests.get(load_url)
soup = BeautifulSoup(html.content,'html.parser')

filename='linklist.text'

with open(filename,'w') as f:
    linkContent = soup.find_all('a')
    for el in linkContent:
        f.write(el.text+"\n")
        url = el.get('href')
        link_url = urllib.parse.urljoin(load_url,url)
        f.write(link_url+"\n")