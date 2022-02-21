from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_helper import *

with get_webdriver() as driver:
    """
    显示等待【重点】：
    显示等待指的是WebdriverWait对象
    所谓的"显示"，是为了前面的"隐式"而言的
    在显示等待中，等待的时机、内容更加的清晰而且可控
    """
    driver.get("http://101.34.221.219:8010/?s=user/logininfo.html")

    driver.find_element(By.XPATH, "/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[1]/input").send_keys(
        'beifan')

    driver.find_element(By.XPATH, "/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[2]/div/input").send_keys(
        '123123')

    driver.find_element(By.XPATH, "/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[3]/button").click()

    msg = WebDriverWait(driver, 10).until(
        lambda x: driver.find_element(
            By.XPATH, '/html/body/div[10]/div/p'
        ).text
    )
    assert msg == '登录成功'

    """
    1.实例化WebDriverWait对象
    WebDriverWait(driver, 10)
    WebDriverWait对象的两个参数：
    driver：WebDriverWait实例（浏览器对象）
    10：超时时间，等待最多不超过10s
    2.等待条件：
    lambda x: driver.find_element(By.XPATH, '/html/body/div[10]/div/p').text
    x 是匿名函数的参数，被传递了driver----> lambda x: x.find_element(By.XPATH, '/html/body/div[10]/div/p').text
    3.等待条件的具体要求：
        >1 等待条件是一个函数(普通函数or匿名函数)
        >2 返回值必须是布尔值，如果不是布尔值，也会按照布尔值判断"
            返回值为True：如果判断成功，表示等待成功，停止等待
            返回值为False：如果判断失败，表示等待失败，继续等待直至超时
            >>> 如果想要False表示成功： 使用until_not方法"WebDriverWait(driver, 10).until_not(lambda x: False)"
            >>> WebDriverWait(driver, 10).until(lambda x: False)  # 会超时
        >3 只有一个参数且参数必须为driver
        >4 出现异常
           出现 NoSuchElementException 异常表示等待失败，将继续等待
           出现其他异常，表示出错，停止等待
           出现TimeOut异常，表示超时，停止等待
    自定义等待条件函数：满足以上四个条件！
    def a(driver):  # 参数名自定义，有且只有一个

        return True
    WebDriverWait(driver, 10).until(a)

    """
    driver.get('http://118.24.147.95:8086/delay.html')

    # 成功
    ele = WebDriverWait(driver, 10).until(lambda x: driver.find_element(By.XPATH, '//*[@id="content"]/input'))

    # 失败::不可以在等待中交互元素
    # WebDriverWait(driver, 10).until(lambda x: driver.find_element(By.XPATH, '//*[@id="content"]/input').click())
    """
    成功：返回值是driver.find_element(By.XPATH, '//*[@id="content"]/input'的返回值，是一个对象，布尔值为True
    失败：返回值是driver.find_element(By.XPATH, '//*[@id="content"]/input').click()的返回值，返回值为None，布尔值为False
    """
    print(driver.find_element(By.XPATH, '//*[@id="content"]/input'))
    print(driver.find_element(By.XPATH, '//*[@id="content"]/input').click())
    ele.click()

