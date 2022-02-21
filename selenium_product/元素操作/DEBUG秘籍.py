import pdb

from selenium.webdriver.common.by import By
from webdriver_helper import *

"""
元素交互过程中出错：
1. 元素不存在
2. 元素不可见
3. 元素被遮挡
4. 元素被禁用
### 在浏览器开发者工具中，输入debugger会使浏览器暂停
"""

with get_webdriver() as driver:

    driver.get('http://118.24.147.95:8086/delay.html')

    # cdp：chrome devtools 协议
    driver.execute_cdp_cmd("Debugger.enable", {})  # JS断点 selenium 4 新特性
    # 两个断点一次只能用一个否则会导致浏览器崩溃 for mac
    driver.execute_script("setTimeout('debugger', 0.1 * 1000)")  # JS断点  selenium 3中直接使用js代码来对浏览器使用断点
    pdb.set_trace()  # python断点

    ele = driver.find_element(By.XPATH, '//*[@id="content"]/input')
    print(ele)
