from selenium.webdriver.common.by import By
from webdriver_helper import *

with get_webdriver() as driver:

    driver.get('http://101.34.221.219:8010/')

    # ID表达式：$("#ID")
    ele = driver.find_element(By.CSS_SELECTOR, "#left-main-quick-popup")
    print('定位到的元素', ele.tag_name, ele.text)

    # CLASS表达式：$(".search-group")
    ele = driver.find_element(By.CSS_SELECTOR, ".search-group")
    print('定位到的元素', ele.tag_name, ele.text)

    # 元素选择器：$("input")
    ele = driver.find_element(By.CSS_SELECTOR, 'input')
    print('定位到的元素', ele.tag_name, ele.text)

    # 属性选择器：$("input[id=search-input]")
    ele = driver.find_element(By.CSS_SELECTOR, 'input[id=search-input]')
    print('定位到的元素', ele.tag_name, ele.text)

    # 层级选择器：$("#goods-category > div > div > div > ul")
    ele = driver.find_element(By.CSS_SELECTOR, "#goods-category > div > div > div > ul")
    print('定位到的元素', ele.tag_name, ele.text)


"""
CSS选择器内包含需要掌握的几种表达式
    ID表达式：$("#ID")
"""