import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_helper import *

with get_webdriver() as driver:

    """
    1. 强制等待：
    sleep()
    弊端：适应场景较少，对于出现以后会消失的元素，无法精确的确定sleep的秒数，
    """
    # driver.get("http://101.34.221.219:8010/?s=user/logininfo.html")
    # driver.find_element(By.XPATH, "/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[1]/input").send_keys(
    #     'beifan')
    #
    # driver.find_element(By.XPATH, "/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[2]/div/input").send_keys(
    #     '123123')
    #
    # driver.find_element(By.XPATH, "/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[3]/button").click()
    # #
    # time.sleep(1)  # 等待时间无法准确确定！
    # mes = driver.find_element(By.XPATH, '/html/body/div[10]/div/p').text
    # assert mes == '登录成功'

    """
    2.隐式等待：
    原理：让selenium查找元素，如果失败，就重试
    默认参数0表示禁用
    大于0表示启用，参数最大值为10？？？(可能不为10！)，表示最大重试秒数为10秒
    一旦启用，全局生效
    弊端：只会等待元素出现，不会等待元素就绪，对于复杂的业务场景，不仅要求元素存在，也要要求元素的状态就绪
    测试网页：http://118.24.147.95:8086/flash.html
    """
    # driver.get("http://118.24.147.95:8086/delay.html")
    # driver.implicitly_wait(10)
    #
    # msg = driver.find_element(By.XPATH, '//*[@id="content"]/p').text
    # ele = driver.find_element(By.XPATH, '//*[@id="content"]/input')
    # print(ele.text, ele.tag_name)
    #
    # assert msg == '大家好，我是北凡'
