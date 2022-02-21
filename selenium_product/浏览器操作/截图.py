from base64 import b64decode
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service()

options = webdriver.ChromeOptions()

driver = webdriver.Chrome()

driver.get('https://www.baidu.com')

# 截图的二进制内容
with open('tupian.png', 'wb') as file:
    file.write(driver.get_screenshot_as_png())

# 截图的base64内容
with open('tutu.png', 'wb') as file:
    file.write(b64decode(driver.get_screenshot_as_base64()))

# 截取图片保存在指定路径
driver.get_screenshot_as_file(r"/Users/liushijia/Documents/git/Remember/selenium_product/浏览器操作/tu.png")

driver.quit()



