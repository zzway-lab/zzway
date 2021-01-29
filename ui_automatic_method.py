import time
from selenium import webdriver
# driver = webdriver.Chrome("C:\Program Files\Google\Chrome\Application\chromedriver.exe")#让chrome能找到你的webdriver
def Ui_automatic_open(driver,website):
            # driver.implicitly_wait(10)
    driver.get(website)#获取你要打开的网站
            # driver.get("http://erp.lemfix.com/login.html")
    driver.maximize_window()#窗口最大化

            # driver.forward()进一步
            # driver.back()退一步
            # driver.
            # page_title = driver.title #获取页面的标题
            # if page_title == "柠檬ERP":
            #     print("this title of page is %s"%(page_title))
            # else:
            #     print("%s不是正确结果，这次运行结果不正确"%(page_title))
            # return driver

            #web页面组成（html，css,js)
'''
    html:定义页面的呈现内容：标签语言<>值</>
    css:控制页面布局(字体，颜色，页面大小）
    js:可让页面在不同情形下呈现不同事情
    html页面：标签---属性
    页面定位元素：能唯一标识这个元素的内容
    
    xpath也是最主要的定位元素的方法的之一
    xpath: head/boby/div/div/div[1]/a/small 从根开始的找的是绝对路径
           //input[@id="username"] 从相对路径开始找，id是属性名，id后面这些属性值去帮忙确定所要的元素定位
           //div[@class="login-logo"}//b 层级定位，相对路径方法有偏差时，可以用返回上几层后再直接定位
           //b[text()='柠檬ERP'] 通过具体文本去直接定位
           //b[contains(text(),'拧檬')] 若属性值太长了，可以用这种方法
           //input[@id="rememeberUserCode"]/following-silbling::ins 轴定位
           若id是变化的则不可以作定位使用
    '''

def Ui_automatic_login(driver,username,password):
    driver.find_element_by_id("username").send_keys(username)
        #send_keys("test123")
    driver.find_element_by_id("password").send_keys(password)
        #send_keys("123456")
    driver.find_element_by_xpath("//input[@id='rememberUserCode']/following-sibling::ins").click()
    driver.find_element_by_id("btnSubmit").click()
    # if __name__ == '__main__':
    #     time.sleep(3)
    #     page_text = driver.find_element_by_xpath("//p").text
    #     if page_text == "测试用户":
    #         print("this title of page is %s"%(page_text))
    #     else:
    #         print("%s不是正确结果，这次运行结果不正确"%(page_text))


def Ui_automatic_search(driver,website,username,password):
    Ui_automatic_open(driver,website)
    time.sleep(5)
    Ui_automatic_login(driver,username,password)
    #driver.switch_to.frame(iframe_id) #用子页面,因iframe_id是变动的，故不能直接用它定位
    driver.implicitly_wait(10)
    driver.find_element_by_xpath("//span[text()='零售出库']").click()
    driver.implicitly_wait(10)        
    li_id = driver.find_element_by_xpath("//div[text()='零售出库']/..").get_attribute("id") #或许id属性
    iframe_id = li_id + "-frame"
    driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@id='%s']"%(iframe_id)))
    driver.find_element_by_xpath("//input[@id='searchNumber']").send_keys("712")
    time.sleep(4)
        # time.sleep(2)
    driver.find_element_by_xpath("//span[text()='查询']").click()
    time.sleep(2)
    text1 = driver.find_element_by_xpath("//tr[@id='datagrid-row-r1-2-0']//td[@field='number']/div").text
    if text1 == 'LSCK00000007712':
        print("%s该搜索结果符合"%(text1))
    else:
        print("%s该搜索结果不符合" %(text1))
    return text1



'''
强制等待：---sleep()-----等待时长没有到期，即便代码执行完成也要继续等待
智能等待：driver.implicitly_wait(10)-----默认等待时间，只要代码执行完成，自动执行到下一步

1.
driver.find_element_by_xpath("span[text()='零售出库']").click()
    

'''
