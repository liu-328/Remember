from selenium import webdriver
from selenium.webdriver.chrome.service import Service


options = webdriver.ChromeOptions()

service = Service()

driver = webdriver.Chrome(service=service, options=options)

driver.get('https://www.baidu.com')

# 浏览器名字
print(driver.name)
# 浏览器能力
print(driver.capabilities)
# 当前网址
print(driver.current_url)
# 页面tittle
print(driver.title)
# HTML源码
print(driver.page_source)
# 当前窗口ID
print(driver.current_window_handle)
# 所有窗口ID
print(driver.window_handles)
# 窗口切换
print(driver.switch_to)
# 超时时间
print(driver.timeouts)

driver.quit()


