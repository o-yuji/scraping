import requests

url = "https://creaters-you.com/"
res = requests.get(url)
res.encoding = res.apparent_encoding
filename="download.txt"
with open(filename,mode="w") as f:
  f.write(res.text)