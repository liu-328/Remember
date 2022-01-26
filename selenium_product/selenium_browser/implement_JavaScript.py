from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path=r'/Library/Frameworks/Python.framework/Versions/3.10/bin/chromedriver')

options = webdriver.ChromeOptions()
# 打开浏览器
driver = webdriver.Chrome(service=service, options=options)

# 执行代码
# 不需要返回值的js代码
driver.execute_script("alert(1)")
alert = driver.switch_to.alert

# 去除弹窗
alert.accept()

# 需要返回值的js代码
a = driver.execute_script("return 1+1")
print('1 + 1 = ', a)

# 传递参数
a = driver.execute_script("return 1+arguments[0]", 100)

print('a = ', a)

# 定位元素赋值给ele
ele = driver.find_element(By.TAG_NAME, 'body')
print(ele)

# 传递元素
driver.execute_script("console.log(arguments[0])", ele)

driver.quit()
