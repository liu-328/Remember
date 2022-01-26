from selenium import webdriver
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
service = Service()

driver = webdriver.Chrome()

driver.get('http://118.24.147.95:8087/cookies')

# 添加cookie
driver.add_cookie({"name": "c", "value": "2"})

# 获取指定的cookie
print(driver.get_cookie('c'))

# 删除cookie
driver.delete_cookie('c')

# 刷新页面
driver.refresh()

# 获取所有的cookie
print(driver.get_cookies())

# 刷新页面
driver.refresh()

# 删除所有cookie
driver.delete_all_cookies()

print(driver.get_cookies())

# 退出浏览器
driver.quit()



















