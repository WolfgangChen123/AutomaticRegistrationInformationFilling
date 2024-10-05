# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import webbrowser

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
import time
# 确保Edge WebDriver的路径正确
edge_webdriver_path = 'C:\edgedriver_win64'

while True:
    try:
        # 初始化Edge WebDriver
        edge_driver = webdriver.Edge()

        # 打开网页
        # edge_driver.get('https://www.baidu.com')
        edge_driver.get('https://www1.nsdszsyxx.com/User/Apply')
        print("open successfully!")
        break
    except WebDriverException as e:
        print(f"open error:{e}")
        time.sleep(3)
        #edge_driver.get('https://www1.nsdszsyxx.com/User/Apply')

edge_driver.maximize_window()
# 执行其他操作，例如点击按钮、填写表单
#input_element = edge_driver.find_element(By.ID, "kw")
#input_element = edge_driver.find_element(By.CLASS_NAME, 's_ipt')
#input_element = edge_driver.find_element(By.NAME, 'wd')
#input_element = edge_driver.find_element(By.XPATH, '//*[@id="kw"]')
#input_element.send_keys('it is test')

#input_element = edge_driver.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/div/div[4]/div[2]/select')
#sinput_element.send_keys('男 / Male')
time.sleep(2)
#Student information
input_element0 = edge_driver.find_element(By.NAME, 'Name')
input_element0.send_keys('陈安安')

input_element1 = edge_driver.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/div/div[4]/div[2]/select')
input_element1.send_keys('男 / Male')

input_element2 = edge_driver.find_element(By.NAME, 'Birthday')
input_element2.send_keys('2016-09-23')

input_element3 = edge_driver.find_element(By.NAME, 'IdType')
input_element3.send_keys('身份证 ID')

input_element5 = edge_driver.find_element(By.NAME, 'IdNumber')
input_element5.send_keys('320502222233412345')

input_element6 = edge_driver.find_element(By.NAME, 'RegPlace')
input_element6.send_keys('江苏省苏州市123师大')

input_element7 = edge_driver.find_element(By.NAME, 'Address')
input_element7.send_keys('相城区')

input_element8 = edge_driver.find_element(By.NAME, 'OldSchool')
input_element8.send_keys('东方幼儿园')
time.sleep(1)
#Parent information1
input_element9 = edge_driver.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/div/div[5]/div[1]/div[2]/input')
input_element9.send_keys('陈大大大')

input_element10 = edge_driver.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/div/div[5]/div[1]/div[3]/select')
input_element10.send_keys('硕士')

input_element10 = edge_driver.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/div/div[5]/div[1]/div[4]/input')
input_element10.send_keys('宇宙有限公司')

input_element11 = edge_driver.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/div/div[5]/div[1]/div[5]/input')
input_element11.send_keys('1801122334455')
time.sleep(1)
#Parent information2
input_element12 = edge_driver.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/div/div[5]/div[2]/div[2]/input')
input_element12.send_keys('额额')

input_element13 = edge_driver.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/div/div[5]/div[2]/div[3]/select')
input_element13.send_keys('本科')

input_element14 = edge_driver.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/div/div[5]/div[2]/div[4]/input')
input_element14.send_keys('都是有限公司')

input_element15 = edge_driver.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/div/div[5]/div[2]/div[5]/input')
input_element15.send_keys('13099965674')
time.sleep(1)
#other
input_element16 = edge_driver.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/div/div[7]/div[1]/select')
input_element16.send_keys('学校官网或微信School official website or WeChat')

input_element17 = edge_driver.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/div/div[7]/div[2]/div[1]/div/div/input')
input_element17.send_keys('183456789')
time.sleep(360)
# 关闭浏览器
#edge_driver.quit()

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
