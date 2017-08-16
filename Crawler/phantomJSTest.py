#encoding:utf-8
from selenium import webdriver
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
obj = webdriver.PhantomJS(executable_path="D:\Python27\Scripts\phantomjs.exe")
obj.set_page_load_timeout(30)
obj.maximize_window()  #设置全屏
try:
    obj.get('http://leige.lolabc.cn')
    #time.sleep(15) #等待页面渲染完成
    #obj.save_screenshot('11.png')  # 截取全屏，并保存
    data = obj.page_source.encode('GBK', 'ignore');  
    title=obj.title.encode('GBK', 'ignore');  
    print data
except UnicodeEncodeError:
    print u"当前cmd不支持打印中文,写入文件查看"
    f=open('b.txt','w')
    f.write(data)
    f.close()

