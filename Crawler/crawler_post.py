#encoding:utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import MySQLdb
import time
import sys
reload(sys)
sys.setdefaultencoding('utf8')





driver = webdriver.PhantomJS(executable_path="D:\Python27\Scripts\phantomjs.exe")
driver.get('http://www.ip138.com/post')
father_handle=driver.current_window_handle
driver.maximize_window()  #设置全屏
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
provinces=driver.find_elements_by_css_selector("body>center>div#newAlexa>table.t4>tbody>tr>td>a")
post=[]
for province in provinces:
    #print province.get_attribute('href')
    p_name=province.text
    print u"%s各县市邮政编码如下:" %p_name
    total=0
    province.click()
    #ActionChains(province).click(next_button).perform()
    time.sleep(5)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    handles = driver.window_handles # 获取当前窗口句柄集合（列表类型）
    for handle in handles:
        if handle != father_handle:
            driver.switch_to_window(handle) 
            break
    citys=driver.find_elements_by_css_selector("body>table.t12>tbody>tr")
    citys=citys[1:]
    for city in citys:
        tds=city.find_elements_by_css_selector('td')
        i=0
        while len(tds)>4:
            c_name=tds[i].text
            c_post_code=tds[i+1].text
            if c_post_code == "":  
                print "empty-------------"  
            c_zone_code=tds[i+2].text
            total+=1
            print "%s：邮政编码:%s--长途区号:%s" %(c_name,c_post_code,c_zone_code)
            data=(c_name,c_post_code,c_zone_code,p_name)
            post.append(data)
            if i==3:
                break
            i+=3
    
    print u"%s各县市邮政编码信息一共%d个" %(p_name,total)    
    driver.close() #关闭切换的窗口
    driver.switch_to_window(father_handle) #切换回原来窗口
    break
    
'''
i=1
while True:
    time.sleep(5)
    if i>11:
        break
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight/3);") #下拉浏览器
    #查询商品
    goods=driver.find_elements_by_css_selector("body >div.main_new >div#rmfgBox.siteBox >div.prolistBox >ul#rmfg_ul.clear> li")
    print u'第%d页商品信息如下:共有%d件商品' %(i,len(goods))
    for good in goods:
        name = good.find_element_by_css_selector('div.m3_sellername>a').text;  
        price= good.find_element_by_css_selector('div.m3_info.mt10 >span.m3_price.fl').text;
        pub_time = good.find_element_by_css_selector('a >div.m3_reltime>span').text;  
        print u"商品名称:%s-----价格:%s----发布时间:%s" %(name,price[4:],pub_time)
    i+=1
    try:
        next_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "body> div.main_new > div#rmfgBox > div.prolistBox >div.tcdPageCode>a.nextPage")))
        ActionChains(driver).click(next_button).perform()
        print u'当前第%d页' %i
        driver.execute_script("var q=document.documentElement.scrollTop=0") 
    except  Exception as e:
        print e
   
    
'''  
db = MySQLdb.connect(host='192.168.190.129', port=3306, user='root', passwd='root', db='test', charset='utf8')
# 使用cursor()方法获取操作游标 
cursor = db.cursor()
# 如果数据表已经存在使用 execute() 方法删除表。
cursor.execute("DROP TABLE IF EXISTS POST")

# 创建数据表SQL语句
sql = """CREATE TABLE POST (
         `ID` int(11) primary key  AUTO_INCREMENT,   
         CITY_NAME  CHAR(50) NOT NULL,
         POST_CODE  CHAR(50),
         ZONE_CODE  CHAR(50),
         PROVINCE_NAME  CHAR(50) NOT NULL
         )"""

cursor.execute(sql)
# 使用cursor()方法获取操作游标 
cursor = db.cursor()

# SQL 插入语句
sql = "INSERT INTO POST(CITY_NAME,POST_CODE, ZONE_CODE, PROVINCE_NAME) VALUES ('%s', '%s', '%s', '%s')" 
print post     
try:
   # 执行sql语句
   cursor.executemany(sql,post)
   cursor.execute(sql)
   # 提交到数据库执行
   db.commit()
except Exception as e:
   print e
   # 发生错误时回滚
   db.rollback()
# 关闭数据库连接
db.close()    
print u"操作结束"
time.sleep(5) 
driver.close()