import requests

image_url = "https://creaters-you.com/pc.png"
imgdata = requests.get(image_url)
#URLから最後のファイル名を取得
filename=image_url.split('/')[-1]
#画像データをファイルに書き出す
with open(filename, mode='wb') as f: #w:書き込み、b:画像ファイルの為、バイバリ形式
    f.write(imgdata.content)