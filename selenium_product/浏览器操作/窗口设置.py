from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# driver对象创建
service = Service(executable_path=r'/Library/Frameworks/Python.framework/Versions/3.10/bin/chromedriver')

# 浏览器对象创建
options = webdriver.ChromeOptions()

# 打开浏览器
driver = webdriver.Chrome(service=service, options=options)

driver.set_window_size(width=2000, height=1000)  # 设置窗口大小
print(driver.get_window_size())                # 获取窗口大小

# driver.minimize_window()  # 窗口最小化
# driver.maximize_window()  # 窗口最大化  不适用于mac！！！
# driver.fullscreen_window()  # 窗口全屏  ps： windows窗口全屏后无法退出  mac使用control+command+f可退出全屏

# driver.set_window_position(x=66, y=77)  # 设置窗口位置
# print(driver.get_window_position())  # 获取窗口位置
#
# driver.set_window_rect(x=23, y=48, width=600, height=700)  # 设置窗口大小和位置
# print(driver.get_window_rect())  # 获取窗口大小和位置

driver.quit()










