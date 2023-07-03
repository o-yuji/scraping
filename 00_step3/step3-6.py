import requests
from pathlib import Path
#保存用フォルダを作成
out_folder = Path('download')
out_folder.mkdir(exist_ok=True)

image_url = "https://creaters-you.com/pc.png"
imgdata = requests.get(image_url)
#URLから最後のファイル名を取得
filename=image_url.split('/')[-1]
out_path=out_folder.joinpath(filename)
#画像データをファイルに書き出す
with open(out_path, mode='wb') as f: #w:書き込み、b:画像ファイルの為、バイナリ形式
    f.write(imgdata.content)