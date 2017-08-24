# -*- coding: UTF-8 -*- 
import sys,os,re,urllib,uuid
import threading
import requests
import shutil
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf-8')
''' 
#首先定义云端的网页,以及本地保存的文件夹地址 
urlPath='http://gamebar.com/'
localPath='pythonPath'

 
#从一个网页url中获取图片的地址，保存在 
#一个list中返回 
def getUrlList(urlParam): 
    urlStream=urllib.urlopen(urlParam) 
    htmlString=urlStream.read() 
    if(len(htmlString)!=0 ): 
        patternString=r'http://.{0,50}\.jpg'
        searchPattern=re.compile(patternString) 
        imgUrlList=searchPattern.findall(htmlString) 
        return imgUrlList 

   
      
#生成一个文件名字符串  
def generateFileName(imgUrl):
    nam=os.path.split(imgUrl)
    print nam[1]
    return  nam[1]
  
    
#根据文件名创建文件  
def createFileWithFileName(localPathParam,fileName):
    os.removedirs(localPathParam)
    os.makedirs(localPathParam)
    totalPath=localPathParam+'\\'+fileName
    if not os.path.exists(totalPath): 
        file=open(totalPath,'wb') 
        file.close() 
        return totalPath 
    
  
#根据图片的地址，下载图片并保存在本地  
def getAndSaveImg(imgUrl):
    if(len(imgUrl)!= 0 ):
        fileName=generateFileName(imgUrl)+'.jpg'
        urllib.urlretrieve(imgUrl,createFileWithFileName(localPath,fileName)) 
  
  
#下载函数 
def downloadImg(url):
    urlList=getUrlList(url) 
    for urlString in urlList: 
        getAndSaveImg(urlString)
    
downloadImg(urlPath) 
'''

#定义线程功能
def threadFunction(fileUrl,directoryName):
    downloadFile(fileUrl,directoryName)

#定义线程类
class myThread (threading.Thread):
    def __init__(self, fileUrl, directoryName):
        threading.Thread.__init__(self)
        self.fileUrl = fileUrl
        self.directoryName = directoryName

    def run(self):
        threadFunction(self.fileUrl, self.directoryName)

        #下载文件
def downloadFile(fileUrl,savePath):
    imageName=os.path.split(fileUrl)
    local_filename = imageName[1]
    r = requests.get(fileUrl, stream=True)
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

def getPrefix(url):
    return ''.join(i+"/" for i in url.split("/")[0:4])

def getDomain(url):
    return ''.join(i+"/" for i in url.split("/")[0:3])

def getContent(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        response.encoding = response.apparent_encoding
        return response.text
    except Exception, e:
        print e
        return str(e)

        
#从一个网页url中获取图片的地址，保存在 
#一个list中返回 
def getImageLinks(soup,imagePath):
    imgs = soup.findAll("img")
    result = []
    for img in imgs:
        try:
            src = img['src']
            if not src.startswith("http"):
                src ="http:"+src
            result.append(img['src'])
            imageName=os.path.split(src)
            #图片路径改成相对路径
            imPath=imagePath+"/"+imageName[1]
            img['src']=imPath
            #print img.prettify() 
        except:
            continue
        #finally: #对网页中地址进行替换，生成相对路径
             
        
    
    return result

def getJsLinks(soup,jsPath):
    scripts = soup.findAll("script")
    result = []
    for script in scripts:
        try:
            src = script['src']
            if not src.startswith("http"):
                src ="http:"+src
            if os.path.splitext(src)[-1]=='.js':
                result.append(src)
            jsName=os.path.split(src)
            #图片路径改成相对路径
            jPath=jsPath+"/"+jsName[1]
            script['src']=jPath
            #print img.prettify()  
                
        except:
            continue
 
    return result

def getCssLinks(soup,cssPath):
    links = soup.findAll("link")
    result = []
    for link in links:
        try:
            src = link['href']
            if not src.startswith("http"):
                src ="http:"+src
            if os.path.splitext(src)[-1]=='.css':
                result.append(src)
            cssName=os.path.split(src)
            #图片路径改成相对路径
            csPath=cssPath+"/"+cssName[1]
            link['href']=csPath
            #print img.prettify()  
        except:
            continue
    return result
 
def creatJsFile(pPath,jsPath):
    js_Path=os.path.join(pPath,jsPath)
    if os.path.exists(js_Path):
        #os.removedirs(js_Path)
        shutil.rmtree(js_Path) 
    os.makedirs(js_Path)
    return js_Path

def creatCssFile(pPath,cssPath):
    css_Path=os.path.join(pPath,cssPath)
    if os.path.exists(css_Path):
        #os.removedirs(css_Path)
        shutil.rmtree(css_Path) 
    os.makedirs(css_Path)
    return css_Path

    
def creatImageFile(pPath,imagePath):
    image_Path=os.path.join(pPath,imagePath)
    if os.path.exists(image_Path):
        #os.removedirs(image_Path)
        shutil.rmtree(image_Path) 
    os.makedirs(image_Path)
    return image_Path
    
def creatFile(urlPath):
    if urlPath[-1]=='/':
        file=urlPath[7:-1]
    else:
        file=urlPath[7:]
    print file
    if os.path.exists(file):
        #os.removedirs(file)
        shutil.rmtree(file) 
    os.makedirs(file)
    return file
    
def saveContent(fPath,text):
    hPath=os.path.join(fPath,fPath+'.html') #连接一个路径
    if os.path.exists(hPath):
        os.remove(hPath)
    f=open(hPath,'wb')
    f.write(text)
    f.close()

threadNumber = 20 # 设置线程数    
imagePath='images'
jsPath='js'
cssPath='css'  
urlPath='http://gamebar.com/'

hfile=creatFile(urlPath)#创建网页文件夹
image_Path=creatImageFile(hfile,imagePath)#创建图片文件夹
js_Path=creatJsFile(hfile,jsPath)#创建js文件夹
css_Path=creatCssFile(hfile,cssPath)#创建css文件夹

content = getContent(urlPath)
soup = BeautifulSoup(content, "html.parser")


images = getImageLinks(soup,imagePath)
print u"本页图片数量 :%d" %len(images)
imageThreads = []
for image in images:
    imageThreads.append(myThread(image, image_Path))
print u'开始下载图片'
for t in imageThreads:
    t.start()
    while True:
        if(len(threading.enumerate()) < threadNumber): #threading.enumerate()的使用。此方法返回当前运行中的Thread对象列表。
            break


while True:
    if((threading.activeCount()-1)==0):  #threading.activeCount()的使用，此方法返回当前进程中线程的个数。返回的个数中包含主线程。
        print u'所有图片下载完毕！'
        break


jss=getJsLinks(soup,jsPath)
jsThreads = []
for js in jss:
    jsThreads.append(myThread(js, js_Path))
print u'开始下载js'
for t in jsThreads:
    t.start()
    while True:
        if(len(threading.enumerate()) < threadNumber): #threading.enumerate()的使用。此方法返回当前运行中的Thread对象列表。
            break


while True:
    if((threading.activeCount()-1)==0):  #threading.activeCount()的使用，此方法返回当前进程中线程的个数。返回的个数中包含主线程。
        print u'所有js文件下载完毕！'
        break


csss=getCssLinks(soup,cssPath)
cssThreads = []
for css in csss:
    cssThreads.append(myThread(css, css_Path))
print u'开始下载css'
for c in cssThreads:
    c.start()
    while True:
        if(len(threading.enumerate()) < threadNumber): #threading.enumerate()的使用。此方法返回当前运行中的Thread对象列表。
            break


while True:
    if((threading.activeCount()-1)==0):  #threading.activeCount()的使用，此方法返回当前进程中线程的个数。返回的个数中包含主线程。
        print u'所有css文件下载完毕！'
        break
#分析css文件是否包含背景图，如果存在就下载

f = open (ss, "r")
data = f.read()
print data

#生成html文件
content=soup.prettify()  
saveContent(hfile,content)

