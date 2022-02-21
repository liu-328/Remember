from selenium.webdriver.common.by import By
from webdriver_helper import *

with get_webdriver() as driver:

    driver.get('http://101.34.221.219:8010/')

    """
    XPATH语法$x('/html/body/div')
    /   表示根路径
    //  表示任意一级
    """

    # 层级表示: $x('/html/body/div')
    # $x('/html/*')  *表示所有
    ele = driver.find_element(By.XPATH, '/html/body/div')
    print('定位到的元素：', ele.tag_name, ele.text)

    # 属性表示: $x('//input[@id="search-input"]')
    ele = driver.find_element(By.XPATH, '//input[@id="search-input"]')
    print('定位到的元素：', ele.tag_name, ele.text)

    # 位置表示1: $x('//input[@name="wd"]')[1]
    ele = driver.find_elements(By.XPATH, '//input[@name='+"'"+"wd"+"'"+']')[1]
    ele1 = driver.find_elements(By.XPATH, '//input[@name='+"'"+"wd"+"'"+']')[0]
    ele2 = driver.find_elements(By.XPATH, '//div[last()]')
    print(ele.tag_name)
    print(ele1.tag_name)
    print(len(ele2))  # 每个层级的最后一个div元素

    # 位置表示2：$x('/html/body/div')[1]
    # 使用位置表示时需要使用find_elements()
    ele = driver.find_elements(By.XPATH, '/html/body/div')[1]
    print('定位到的元素：', ele.tag_name, ele.text)

    # 元素表示：$x('//input')   同样可以使用位置表示定位
    ele = driver.find_element(By.XPATH, '//input')
    print('定位到的元素：', ele.tag_name, ele.text)



