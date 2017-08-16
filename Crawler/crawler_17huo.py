#encoding:utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
driver.get('http://www.17huo.com/')
driver.maximize_window()  #设置全屏
m_w_closeButton=driver.find_element_by_id("bomb_close")# 关闭弹窗
ActionChains(driver).click(m_w_closeButton).perform()
b_w_closeButton=driver.find_element_by_css_selector("body > div.fix-bottom > div.fb-context-box  >div.fb-context > a.fb-close")
ActionChains(driver).click(b_w_closeButton).perform()
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
   
    
   
    
print u"操作结束"
  
driver.close()