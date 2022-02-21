from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_helper import *

options = webdriver.ChromeOptions()
service = Service()

with get_webdriver() as driver:
    driver.get('http://118.24.147.95:8087/cookies')  # 显示cookies的网站
    # http://118.24.147.95:8087/cookies  # 设置cookie的网站

    # 添加cookie
    # *****cookie一定是字符串*****
    driver.add_cookie({"name": "c", "value": "2"})

    # 获取指定的cookie
    print(driver.get_cookie('c'))

    # 删除cookie
    driver.delete_cookie('c')

    # 获取所有的cookie
    print(driver.get_cookies())

    # 刷新页面
    driver.refresh()

    # 再次添加cookie
    driver.add_cookie({"name": "1", "value": "3"})

    # 刷新页面
    driver.refresh()

    # 获取所有的cookie
    print(driver.get_cookies())

    # 删除所有cookie
    driver.delete_all_cookies()

    # 获取所有的cookie
    print(driver.get_cookies())

    # 退出浏览器
    driver.quit()



















