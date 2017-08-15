#encoding:utf-8
from selenium import webdriver
import time
import urllib 
import sys
import io
import chardet 
reload(sys)
sys.setdefaultencoding('utf-8')
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
path = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
browser = webdriver.Chrome(executable_path=path)
#browser = webdriver.Chrome()
browser.set_page_load_timeout(30)
browser.get('http://www.17huo.com/search.html?sq=2&keyword=%E7%BE%8A%E6%AF%9B')
page_info = browser.find_element_by_css_selector('body > div.wrap > div.pagem.product_list_pager > div')
print page_info.text
la=page_info.text.split('，')
print la
pages = int((page_info.text.split('，')[0]).split(' ')[1])
for page in range(pages):
    if page > 2:
        break
    url = 'http://www.17huo.com/?mod=search&sq=2&keyword=%E7%BE%8A%E6%AF%9B&page=' + str(page + 1)
    browser.get(url)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)   # 不然会load不完整
    goods = browser.find_element_by_css_selector('body > div.wrap > div:nth-child(2) > div.p_main > ul').find_elements_by_tag_name('li')
    print  u'%d页有%d件商品' %((page + 1), len(goods))
    for good in goods:
        try:
            title = good.find_element_by_css_selector('a:nth-child(1) > p:nth-child(2)').text.decode('gb2312')
            price = good.find_element_by_css_selector('div > a > span').text.decode('gb2312')
            print title,price
        except:
            print good.text
