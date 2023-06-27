import requests

url = "https://creaters-you.com/"
res = requests.get(url)
res.encoding = res.apparent_encoding

print(res.text)