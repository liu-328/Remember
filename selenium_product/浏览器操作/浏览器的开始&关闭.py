import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

"""
手动安装driver时：
webdriver.Chrome()需要传递两个参数
    service：浏览器驱动的对象，driver的存放路径（自动配置的情况可以省略service参数）
    options：浏览器参数对象  
新版本selenium中，只接收service和options两个参数
chrome参数地址：
    谷歌浏览器驱动可以接收的参数 ChromeDriver： https://chromedriver.chromium.org/capabilities
    谷歌浏览器可以接收的参数 Chrome：https://peter.sh/experiments/chromium-command-line-switches/
"""
# driver 安装位置 driver对象创建
service = Service(executable_path=r'/Library/Frameworks/Python.framework/Versions/3.10/bin/chromedriver')

# 浏览器对象创建
options = webdriver.ChromeOptions()
# 为浏览器对象添加参数
options.add_argument("--start-fullscreen")  # 举个栗子

# 手动关闭
# 1.启动浏览器
driver = webdriver.Chrome(service=service, options=options)

print(driver.get_window_rect())
time.sleep(3)
driver.set_window_rect(width=1300, height=2000)
time.sleep(3)
print(driver.get_window_rect())

# 2.启动浏览器并访问https://www.baidu.com
driver.get('https://www.baidu.com')

# 退出浏览器
driver.quit()
# 关闭标签页
# driver.close()

"""
ps: open()的返回值也是上下文管理器
    webdriver.Chrome()对象的返回值也是上下文管理器
    所以都可以使用with的方式打开
"""
# 自动关闭
# with webdriver.Chrome(service=service, options=options) as driver:
#     driver.get('https://www.baidu.com')

