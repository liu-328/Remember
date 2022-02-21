from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_helper import *

"""
selenium 核心是用什么语言开发的？ java
在Java 语言中，流畅等待指的是 FluentWait 对象，是 WebDriverWait 的父类
在Python中，没有定义 FluentWait 对象，直接使用 WebDriverWait 对象完成流畅等待
和显式等待相比，流畅等待增加2个参数：
    1. 重试频率 (等待的原理：失败重试，多久重试一次？)
    2. 忽略的异常列表
    3. 可以实现更加复杂的业务场景
"""

with get_webdriver() as driver:

    """
    如果元素闪现太快，则不会定位到元素
    ele = WebDriverWait(driver, 10).until(lambda x: driver.find_element(By.XPATH, '//*[@id="content"]/p'))

    print(ele.text)
    """
    # driver.get("http://118.24.147.95:8086/flash_fast.html")
    # # 在WebDriverWait对象中添加第三个参数0.01(可以为任意数字)，表示重试频率
    # ele = WebDriverWait(driver, 10, 0.01  # 0.01表示指定重试频率， 10 表示重试时间。
    #                     ).until(lambda x: driver.find_element(By.XPATH, '//*[@id="content"]/p'))
    #
    # print(ele.text)

    """
    如果等待的过程中出现除 NoSuchElementException 以外的异常，则显示等待不会定位到元素，直接报错
    driver.get("http://118.24.147.95:8086/delay_alert.html")
    alert = WebDriverWait(driver, 10, 0.01).until(driver.switch_to.alert)
    print(alert.text)
    """

    # driver.get("http://118.24.147.95:8086/delay_alert.html")
    # # 添加参数ignored_exceptions=[NoAlertPresentException]参数表示指定异常名字，如果出现了此异常名字，则继续重试。
    # alert = WebDriverWait(driver, 10, ignored_exceptions=[NoAlertPresentException]
    #                       ).until(lambda x: driver.switch_to.alert)
    # print(alert.text)

    """
    等待策略可以复用
    复用前:
    driver.get("http://118.24.147.95:8086/flash.html")
    p = WebDriverWait(driver, 10, 0.01).until(lambda x: driver.find_element(By.XPATH, '//*[@id="content"]/p'))
    i = WebDriverWait(driver, 10, 0.01).until(lambda x: driver.find_element(By.XPATH, '//*[@id="content"]/input'))
    print(p.text)
    print(i.tag_name)
    """
    # 复用后：
    driver.get("http://118.24.147.95:8086/flash.html")
    wait = WebDriverWait(driver, 10)

    p = wait.until(lambda x: driver.find_element(By.XPATH, '//*[@id="content"]/p'))
    i = wait.until(lambda x: driver.find_element(By.XPATH, '//*[@id="content"]/input'))
    print(p.text)
    print(i.tag_name)


