from webdriver_helper import *
from selenium.webdriver.common.by import By

with get_webdriver() as driver:


    driver.get("http://101.34.221.219:8010/")

    """XPATH字符串操作函数"""

    # 包含函数contains()  获取属性中包含指定字符串的元素
    ele = driver.find_element(By.XPATH, '//img[contains(@alt, "ZK星星绣花雪纺连衣裙中长款sukol裙少女心温柔超仙女chic裙子夏")]')
    print('获取到的元素：', ele.tag_name, ele.text)

    # 判断字符串以指定内容开头starts-with  获取属性中以指定字符串开头的元素
    ele = driver.find_element(By.XPATH, '//img[starts-with(@alt, "MIUI/小米")]')
    print('获取到的元素：', ele.tag_name, ele.text)

    """
    判断字符串以指定内容结尾starts-with  获取属性中以指定字符串结尾的元素 !!!谷歌浏览器没有此函数
    ele = driver.find_element(By.XPATH, "//img[ends-with(@alt, '新品 闪耀白')]")
    print('获取到的元素', ele.tag_name, ele.text)
    """

    # 如果元素内无其他属性，只有一个字符串可以使用text()函数
    # text()指的是元素内的标签文本
    ele = driver.find_element(By.XPATH, '//div[text()="iphoneX新品发布了"]')
    print('获取到的元素：', ele.tag_name, ele.text)



