#encoding:utf8

import requests
import threading
from bs4 import BeautifulSoup
import sys
import os

if len(sys.argv) != 2:
    print "Usage : "
    print "        python main.py [URL]"
    exit(1)

# config-start
url = sys.argv[1]
threadNumber = 20 # 设置线程数
# config-end

def getContent(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        response.encoding = response.apparent_encoding
        return response.text
    except Exception, e:
        print e
        return str(e)

def getTitle(soup):
    try:
        return soup.title.string
    except:
        return "UnTitled"

def getImageLinks(soup):
    imgs = soup.findAll("img")
    result = []
    for img in imgs:
        try:
            src = img['src']
            if src.startswith("http"):
                result.append(img['src'])
            else:
                result.append(domain + img['src'])
        except:
            continue
    return result

def makeDirectory(dicName):
    if not os.path.exists(dicName):
        os.mkdir(dicName)

def downloadImage(imgUrl,savePath):
    local_filename = imgUrl.split('/')[-1]
    local_filename = formatFileName(local_filename)
    r = requests.get(imgUrl, stream=True)
    counter = 0
    if not savePath.endswith("/"):
        savePath += "/"
    f = open(savePath + local_filename, 'wb')
    for chunk in r.iter_content(chunk_size=1024):
        if chunk:
            f.write(chunk)
            f.flush()
            counter += 1
    f.close()

def formatFileName(fileName):
    fileName = fileName.replace("/","_")
    fileName = fileName.replace("\\","_")
    fileName = fileName.replace(":","_")
    fileName = fileName.replace("*","_")
    fileName = fileName.replace("?","_")
    fileName = fileName.replace("\"","_")
    fileName = fileName.replace(">","_")
    fileName = fileName.replace("<","_")
    fileName = fileName.replace("|","_")
    fileName = fileName.replace(" ","_")
    return fileName

def threadFunction(imgSrc,directoryName):
    downloadImage(imgSrc,directoryName)

class myThread (threading.Thread):
    def __init__(self, imgSrc, directoryName):
        threading.Thread.__init__(self)
        self.imgSrc = imgSrc
        self.directoryName = directoryName

    def run(self):
        threadFunction(self.imgSrc, self.directoryName)


def getPrefix(url):
    # http://doamin/xxx.jpg
    return ''.join(i+"/" for i in url.split("/")[0:4])

def getDomain(url):
    return ''.join(i+"/" for i in url.split("/")[0:3])



content = getContent(url)
prefix = getPrefix(url)
domain = getDomain(url)
soup = BeautifulSoup(content, "html.parser")
images = getImageLinks(soup)
title = getTitle(soup)
title = formatFileName(title)
print u"页面标题 : " , title
print u"本页图片数量 :",len(images)
print u"正在创建文件夹以用来保存所有图片"
makeDirectory(title)
threads = []

for image in images:
    print u"图片地址 : " + image
    threads.append(myThread(image, title))

for t in threads:
    t.start()
    while True:
        if(len(threading.enumerate()) < threadNumber): #threading.enumerate()的使用。此方法返回当前运行中的Thread对象列表。
            break

print u"所有图片已加入下载队列 ! 正在下载..."