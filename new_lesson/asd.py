import time
from selenium import webdriver
# def Ui_automatic_open(website):
driver = webdriver.Chrome("C:\Program Files\Google\Chrome\Application\chromedriver.exe")#让chrome能找到你的webdriver
            # driver.implicitly_wait(10)
driver.get("http://erp.lemfix.com/login.html")#获取你要打开的网站
            # driver.get("http://erp.lemfix.com/login.html")
driver.maximize_window()#窗口最大化
driver.find_element_by_id("username").send_keys("123456")