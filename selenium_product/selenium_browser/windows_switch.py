from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_helper import *

# 浏览器driver对象创建

service = Service()
# 浏览器对象创建
options = webdriver.ChromeOptions()

# 打开浏览器
driver = get_webdriver()

# 查看窗口id
print('当前页面ID', driver.current_window_handle)
# 查看所有窗口id
print('所有窗口id', driver.window_handles)

# 创建tab页
driver.switch_to.new_window('tab')

# 创建新窗口
driver.switch_to.new_window('window')

# 查看窗口id
print('当前页面ID', driver.current_window_handle)

# 查看所有窗口id
print('所有窗口id', driver.window_handles)
# 切换窗口
for win_id in driver.window_handles:
    driver.switch_to.window(win_id)
    print('当前窗口id为；', win_id)

driver.get("http://118.24.147.95:8086/switch_to.html")

# 切换弹窗alert
alert = driver.switch_to.alert  # js弹窗是阻塞形代码
print(alert)
# 点击弹窗的确定按钮
alert.accept()
# # 点击取消按钮
# alert.dismiss()
# # 向弹窗输入内容
# alert.send_keys('x')

# 切换到frame标签  ---->进入标签
driver.switch_to.frame(0)  # 通过frame的id切换

"""方法1"""
# 使用CSS选择器定位到h2元素
ele = driver.find_element(By.CSS_SELECTOR, "h2")
print(ele)

"""方法2"""
# 定位到iframe本身
# ls = driver.find_element(By.XPATH, "/html/body/iframe")
# driver.switch_to.frame(ls)
#
# ele = driver.find_element(By.CSS_SELECTOR, "h2")
# print(ele)

# 返回上一层iframe  如果返回到最上层后多次返回上一层则在最上层页面不动。
driver.switch_to.parent_frame()

# 返回最上层iframe
driver.switch_to.default_content()

"""
多个iframe定位
ls = driver.find_elements(By.XPATH, "/html/body/iframe")
driver.switch_to.frame(ls[0])
ele = driver.find_element(By.CSS_SELECTOR, "h2")
print(ele)
"""

# 关闭浏览器
driver.quit()



