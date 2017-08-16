#encoding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
driver.get('http://www.baidu.com/') #自动打开浏览器，然后访问百度。
driver.maximize_window() #设置全屏
try:
    content=driver.page_source #获取网页内容
    print content
except  UnicodeEncodeError:
    print u"当前cmd不支持打印中文,写入文件查看"
    f=open('a.txt','w')
    f.write(content)
    f.close()

elem=driver.find_element_by_name("wd")#根据名字及获取输入框
elem.send_keys("pycon") 
elem.send_keys(Keys.RETURN) #点击回车
#driver.implicitly_wait(30) #单位是秒
time.sleep(5)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2);") #下拉浏览器
time.sleep(10)
elem=driver.find_element_by_id("kw") #根据id获取输入框
elem.click() #click输入框
elem.clear() #清除输入框
elem.send_keys(u"发送文字")  #发送文字
time.sleep(10)
driver.close()

