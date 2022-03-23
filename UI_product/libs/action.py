"""
封装了关键字驱动的相关代码
"""
import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_helper import get_webdriver


class KeyWord:
    """
    关键字类： 代表用户操作的指令集
    """

    def __init__(self, driver: Chrome = None):
        """
        实例化， 如果没有driver是，自动获取
        :param driver:
        """
        if not driver:
            driver = get_webdriver()
            driver.maximize_window()

        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # 可复用的等待策略，最长等待10秒
        self.__vars = {}  # 存储变量

    def find_element(self, xpath) -> WebElement:
        """
        封装元素定位方法，自动使用xpath，自动使用显式等待
        :param xpath: 定位表达式
        :return:
        """

        def f(_):
            return self.driver.find_element(By.XPATH, xpath)

        return self.wait.until(f)

    @classmethod
    def all_keyword(cls):
        """
        列出所有可用的关键字：

        1. key_开头
        2. 可调用的
        :return:
        """

        _all_keyword = []  # 所有可以用关键字

        for attr in dir(cls):  # 遍历自己的所有成员
            if attr.startswith("key_"):  # 关键字前缀
                method = getattr(cls, attr)
                if callable(method):  # 如果是可调用的
                    _all_keyword.append(attr[4:])

        return _all_keyword

    def key_sleep(self, times):
        times = float(times)
        time.sleep(times)

    def key_goto(self, url):
        return self.key_get(url)

    def key_get(self, url):
        """
        关键字： get
        跳转到指定的页面
        :param url: 指定页面的url
        :return:
        """

        self.driver.get(url)

    def key_click(self, xpath, force=False):
        """
        关键字：click

        自定等待元素，然后进行点击
        :param xpath: 元素定位表达式
        :param force: 是否强制点击
        :return:
        """

        ele = self.find_element(xpath)

        if force:  # 使用js强制点击
            self.driver.execute_script("argumnets[0].click()", ele)
        else:
            ele.click()

    def key_input(self, xpath, value):
        """
        关键字 ：input
        向指定的元素，输入内容

        :param xpath: 元素的定位表达式
        :param value: 要输入的内容
        :return:
        """

        ele = self.find_element(xpath)
        # todo 等待元素就绪：可交互

        ele.clear()
        ele.send_keys(value)

    def key_alert_ok(self):
        """
        关键字：alert_ok
        为alert点击确定
        :return:
        """
        alert = self.wait.until(expected_conditions.alert_is_present())

        alert.accept()

    def key_frame_enter(self, xpath):
        """
        关键字 ：frame_enter
        进入到指定的frame

        :param xpath: 元素定位表达式
        :return:
        """
        ele = self.find_element(xpath)
        assert ele.tag_name == "iframe"

        self.driver.switch_to.frame(ele)

    def key_frame_exit(self):
        """
        关键字 ：frame_exit
        退出当前的frame

        :return:
        """

        self.driver.switch_to.parent_frame()  # 返回上一层

    def key_frame_top(self):
        """
        关键字 ：frame_top
        返回顶层frame

        :return:
        """

        self.driver.switch_to.default_content()  # 返回到顶层

    def key_get_text(self, xpath, var_name):
        """
        关键字 : get_text
        获取页面上的text内容
        :param xpath: 元素定位表达式
        :param var_name: 要保存的变量名
        :return:
        """

        ele = self.find_element(xpath)
        self.__vars[var_name] = ele.text

    def key_assert(self, value, assert_nam, actual_value=""):
        """
        关键字 assert
        :param value: 预期结果
        :param assert_nam: 断言表达式
        :param actual_value: 实际结果 ，支持字符串格式化的写法来使用变量`{var}`
        :return:
        """

        actual_value = actual_value.format_map(self.__vars)

        validator = Validator(value, assert_nam, actual_value)

        assert validator.is_valid() is True

    def key_save_text(self, var_name, xpath, not_expect_empty=False):
        """
        关键字：save_text
        保存页面上text内容

        :param var_name: 要保存的变量名
        :param xpath: 元素定位表达式，如果要获取alert的内容，请传递alert
        :param not_expect_empty: 是否不期望空，
        :return:
        """
        if xpath.lower() == "alert":
            text = self.wait.until(expected_conditions.alert_is_present()).text
        elif not_expect_empty:
            # 不期望空，等待元素有text值
            text = self.wait.until(lambda _: self.find_element(xpath).text)
        else:
            text = self.find_element(xpath).text

        self.__vars[var_name] = text

    def key_save_url(self, var_name):
        """
        关键字：save_url
        保存当前网址

        :param var_name: 要保存的变量名
        :return:
        """
        self.__vars[var_name] = self.driver.current_url


class Validator:
    def __init__(self, value, assert_nam, actual_value):
        """
        预期结果 和 实际结果 进行比较

        :param value:
        :param assert_nam:
        :param actual_value:
        """
        self.value = value
        self.assert_nam = assert_nam
        self.actual_value = actual_value

    def is_valid(self):
        """
        执行断言，如果返回True表示断言成功
        :return:
        """

        _assert = getattr(self, f"assert_{self.assert_nam}")  # 找到断言方法

        _assert(self.value, self.actual_value)

        return True

    def assert_in(self, a, b):
        """
        断言方法 ： in
        a 在 b 其中

        :return:
        """

        assert a in b

    def assert_contains(self, a, b):
        """
        断言方法 ： contains
        a 包含 b

        :return:
        """

        assert b in a

    def assert_equal(self, a, b):
        """
        断言方法 ： equal
        a 等于 b

        :return:
        """

        assert b == a

    def assert_not_equal(self, a, b):
        """
        断言方法 ： not_equal
        a 不等于 b

        :return:
        """

        assert b != a
