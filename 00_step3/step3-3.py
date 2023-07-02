import requests
from bs4 import BeautifulSoup

load_url = "https://creaters-you.com/"

html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

chap1 = soup.find(id="chap1").find_all('li')

for el in chap1:
    print(el.text)