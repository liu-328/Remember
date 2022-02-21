from selenium.webdriver.common.by import By
from webdriver_helper import *


with get_webdriver() as driver:
    driver.get('http://101.34.221.219:8010/')

    # ID 根据元素的ID属性进行定位
    ele = driver.find_element(By.ID, 'search-input')
    print('定位到的元素', ele.tag_name, ele.text)

    # NAME 根据元素的NAME属性进行定位
    ele = driver.find_element(By.NAME, 'wd')
    print('定位到的元素', ele.tag_name, ele.text)

    # TAG_NAME 根据元素的TAG_NAME(标签名)进行定位
    ele = driver.find_element(By.TAG_NAME, 'input')
    print('定位到的元素', ele.tag_name, ele.text)

    # CLASS_NAME 根据元素的CLASS_NAME属性进行定位
    # ele = driver.find_element(By.CLASS_NAME, 'search-group')  # 不可以使用复合类
    ele = driver.find_element(By.CLASS_NAME, 'search-group')
    print('定位到的元素', ele.tag_name, ele.text)

    # 定位多个元素find_elements()
    ele = driver.find_elements(By.NAME, 'wd')
    print('定位到的元素', ele)

    """以上四种选择器进行定位，在源码底层处理时，会被转换为css选择器"""

    """
    <a class="am-dropdown-toggle " data-am-dropdown-toggle="" href="javascript:;">
                                         "商品分类"
                                        <span class="am-icon-caret-down"></span>
                                    </a>
    """
    # 只可以定位a标签且只可以定位标签和标签之间的完整文本信息例如：
    #   "商品分类"
    ele = driver.find_element(By.LINK_TEXT, '商品分类')
    print('定位到的元素', ele.tag_name, ele.text)

    # 只可以定位a标签且只可以定位标签和标签之间的非完整文本信息例如：
    ele = driver.find_element(By.PARTIAL_LINK_TEXT, '分类')
    print('定位到的元素', ele.tag_name, ele.text)


"""
find_element 返回单个元素
find_elements 返回一个由多个元素组成的列表
"""


