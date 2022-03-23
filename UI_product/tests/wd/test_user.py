import time

import pytest
from libs.action import KeyWord
from selenium.webdriver.common.by import By
from webdriver_helper import get_webdriver


@pytest.fixture
def user_chrome(cache):
    """
    登录夹具：
    1.判断是否已经登录
    2.如果未登录，就进行登录
    :return:
    """
    driver = get_webdriver()
    driver.get("http://101.34.221.219:8010/")

    cookie = cache.get("user_cookie", {})  # 读取cookie
    for c in cookie:
        driver.add_cookie(c)  # 设置cookie
    driver.refresh()

    ele = driver.find_elements(By.XPATH, '//a[text()="退出"]')
    if ele:  # 有退出按钮，说明已登录
        pass
    else:
        # 否则，是没有登录，就进行登录
        driver.get("http://101.34.221.219:8010/?s=user/loginInfo.html")
        ele = driver.find_element(
            By.XPATH,
            "/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[1]/input",
        )
        ele.send_keys("beifan")

        ele = driver.find_element(
            By.XPATH,
            "/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[2]"
            "/div/input",
        )
        ele.send_keys("123123")

        ele = driver.find_element(
            By.XPATH,
            "/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[3]/button",
        )
        ele.click()
        time.sleep(0.2)

        cache.set("user_cookie", driver.get_cookies())  # 保存cookies

    yield driver

    driver.quit()  # 测试结束时，关闭浏览器


def test_new_address(user_chrome):
    key_word = KeyWord(user_chrome)
    key_word.key_get("http://101.34.221.219:8010/?s=useraddress/index.html")
    key_word.key_click("/html/body/div[4]/div[3]/div/div/button")
    key_word.key_alert_ok()

    key_word.key_frame_enter(
        '//iframe[@src="http://101.34.221.219:8010/?s=useraddress/saveinfo.html"]'
    )

    key_word.key_input("/html/body/div[1]/form/div[2]/input", "啊啊大苏打")
    # /html/body/div[1]/form/div[2]/input
    key_word.key_input("/html/body/div[1]/form/div[3]/input", "13811112222")
    key_word.key_input('//*[@id="form-address"]', "详细地址")

    key_word.key_click("/html/body/div[1]/form/div[4]/div[1]")
    key_word.key_click('//ul/li[text()="湖南省"]')

    key_word.key_click("/html/body/div[1]/form/div[4]/div[2]")
    key_word.key_click('//ul/li[text()="长沙市"]')

    key_word.key_click("/html/body/div[1]/form/div[4]/div[3]")
    key_word.key_click('//ul/li[text()="岳麓区"]')

    key_word.key_click("/html/body/div[1]/form/div[7]/button")  # 点击保存

    key_word.key_get_text('//p[@class="prompt-msg"]', "msg")  # 获取实际结果

    key_word.key_assert("操作成功", "equal", "{msg}")

    user_chrome.get_screenshot_as_file("a.png")


def test_new_address_fail(user_chrome):
    key_word = KeyWord(user_chrome)
    key_word.key_get("http://101.34.221.219:8010/?s=useraddress/index.html")
    key_word.key_click("/html/body/div[4]/div[3]/div/div/button")
    key_word.key_alert_ok()

    key_word.key_frame_enter(
        '//iframe[@src="http://101.34.221.219:8010/?s=useraddress/saveinfo.html"]'
    )

    key_word.key_input("/html/body/div[1]/form/div[2]/input", "啊啊大苏打")
    # /html/body/div[1]/form/div[2]/input
    key_word.key_input("/html/body/div[1]/form/div[3]/input", "13811112222")
    key_word.key_input('//*[@id="form-address"]', "详细地址")

    key_word.key_click("/html/body/div[1]/form/div[7]/button")  # 点击保存

    key_word.key_get_text('//p[@class="prompt-msg"]', "msg")  # 获取实际结果

    key_word.key_assert("操作成功", "not_equal", "{msg}")  # 表单不完整，应该操作不成功

    user_chrome.get_screenshot_as_file("a.png")
