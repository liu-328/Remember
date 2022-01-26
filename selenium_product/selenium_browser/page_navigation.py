from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=r'/Library/Frameworks/Python.framework/Versions/3.10/bin/chromedriver')

options = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=service, options=options)

# 访问百度
driver.get('https://www.baidu.com')

# 返回空白页（返回上一级）
driver.back()

# 前进到百度（前进到下一个页面）
driver.forward()

# 刷新网页
driver.refresh()

# 退出网页
driver.quit()







