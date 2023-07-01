import requests
from bs4 import BeautifulSoup
import urllib
from pathlib import Path
import time

#Webページを取得して解析
load_url = "https://creaters-you.com/"
html = requests.get(load_url)
soup = BeautifulSoup(html.content,"html.parser")
#保存用フォルダを作成
out_folder = Path("download")
out_folder.mkdir(exist_ok=True)

#全てのimgタグを検索して、リンクを取得
for el in soup.find_all("img"):
    src = el.get("src")
    #絶対パスと、画像データを取得する
    image_url = urllib.parse.urljoin(load_url,src)
    imgdata = requests.get(image_url)
    #URlから最後のファイル名を取り出し、保存フォルダ名と接続
    filename = image_url.split('/')[-1]
    out_path = out_folder.joinpath(filename)
    with open(out_path,mode="wb") as f:
        f.write(imgdata.content)
    #1回アクセスしたので、1秒待つ
    time.sleep(1)