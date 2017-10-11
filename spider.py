import os
import urllib
from urllib.request import urlretrieve
from urllib.request import urlopen
from PIL import Image
import time


global count
counts = 0
def download(url):
    global counts
    counts += 1
    name = str(counts) + '.jpg'
    file_path = os.path.join("F:\\modern-family", name)  # 拼接这个图片的路径，我是放在F盘的pics文件夹下
    urllib.request.urlretrieve(url, file_path)  # 接收文件路径和需要保存的路径，会自动去文件路径下载并保存到我们指定的本地路径

def buildUrl(n):
    pages = []
    num = int(n)
    for i in range(1, num):
        url = 'http://221.122.117.73/index.jsp?file=741551717&width=1000&pageno=%s' % i
        pages.append(url)
    return pages


urls = buildUrl(326)
for url in urls:
    time.sleep(5)
    print(url)
    download(url)