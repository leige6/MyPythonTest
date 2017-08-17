#encoding:utf-8
from PIL import Image,ImageEnhance
import pytesseract
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

pytesseract.pytesseract.tesseract_cmd = 'D:\\Tesseract-OCR\\tesseract' #设置tesseract_cmd地址
tessdata_dir = '--tessdata-dir "D:\\Tesseract-OCR\\tessdata"'  #设置eng.traineddata地址
driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
driver.maximize_window()  #设置全屏

driver.get('https://www.vjinke.com/login')
father_handle=driver.current_window_handle
#driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

elem_user = driver.find_element_by_xpath('//input[@id="userName"]')
elem_psw = driver.find_element_by_xpath('//input[@id="password"]')
elem_code = driver.find_element_by_xpath('//input[@id="validateCode"]')
imgelement = driver.find_element_by_xpath('//img[@id="verifyCodeImage"]')  #定位验证码
location = imgelement.location  #获取验证码x,y轴坐标
size=imgelement.size  #获取验证码的长宽
total=0
while True:
    total+=1
    driver.save_screenshot('vjinke_login.png')  #截取当前网页，该网页有我们需要的验证码
    rangle=(int(location['x']),int(location['y']),int(location['x']+size['width']),int(location['y']+size['height'])) #写成我们需要截取的位置坐标
    i=Image.open("vjinke_login.png") #打开截图
    frame4=i.crop(rangle)  #使用Image的crop函数，从截图中再次截取我们需要的区域
    frame4.save('verifyCodeImage.jpg')
    '''
    time.sleep(1) 
    im=Image.open('verifyCodeImage.jpg')
    imgry = im.convert('L')#图像加强，二值化
    sharpness =ImageEnhance.Contrast(imgry)#对比度增强
    sharp_img = sharpness.enhance(2.0)
    sharp_img.save('verifyCodeImage.jpg')
    '''
    time.sleep(1) 
    qq=Image.open('verifyCodeImage.jpg')
    time.sleep(1) 
    code=pytesseract.image_to_string(qq,lang='eng',config=tessdata_dir).strip() #使用image_to_string识别验证码
    code=code.strip().replace(' ','')
    print u'系统尝试第%d次登录。。。。' %total
    print u'识别验证码为：'+code
    elem_user.clear()
    elem_psw.clear()
    elem_code.clear()
    elem_user.send_keys('15224833308')
    if total>6:
        elem_psw.send_keys('fang201314')
    else:
        elem_psw.send_keys('fang20131')
    elem_code.send_keys(code)
    click_login = driver.find_element_by_xpath('//a[@id="submitBtn"]')
    click_login.click()
    try:
        login_info=driver.find_element_by_xpath('//div[@id="validatecode_label"]')  #定位登录信息提示
        lgoin_info_status=login_info.value_of_css_property('display')
        time.sleep(1)   
        if lgoin_info_status=='block':
            print u'状    态：登录失败，重新登录！'
            print u'失败原因：%s' %login_info.text
            print u'---------------------------------'
        imgelement.click()
        time.sleep(1)   
    except  Exception as e:
        print u'状   态：登录成功！'
        print u'---------------------------------'
        break

time.sleep(5)
driver.close()