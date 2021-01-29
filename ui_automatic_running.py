import sys
sys.path.append("F:\python editing tool\new_lesson")
print(sys.path)

from new_lesson import ui_automatic_data
from new_lesson import ui_automatic_method
from selenium import webdriver
import time
driver = webdriver.Chrome("C:\Program Files\Google\Chrome\Application\chromedriver.exe")
time.sleep(10)
website = ui_automatic_data.data["website"]
username = ui_automatic_data.data["username"]
password = ui_automatic_data.data["password"]
verifying_value = ui_automatic_data.data["verifying_value"]
running_result = ui_automatic_method.Ui_automatic_search(driver, website, username, password)
if running_result == verifying_value:
    print("验证成功")
else:
    print("验证失败")
    
