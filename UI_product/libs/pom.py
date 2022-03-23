
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait


class FakeElement:
    def __new__(cls, args) -> WebElement:
        return args


class BasePage:
    """抽象类：是抽象的，不代码任意一个页面"""

    _url = ""

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # 可复用的等待策略，最长等待10秒

        self.check_url()
        # 实例化的时候，根据表达式，创建真正的元素
        self.check_element()

    def find_element(self, xpath):
        """
        封装元素定位方法，自动使用xpath，自动使用显式等待
        :param xpath: 定位表达式
        :return:
        """

        def f(_):
            return self.driver.find_element(By.XPATH, xpath)

        return self.wait.until(f)

    def check_url(self):
        """
        检查当前url是不是本page的url
        :return:
        """
        assert self.driver.current_url == self._url, self.driver.current_url

    def check_element(self):
        """
        检查所有元素是否存在，如果存在，就保存为属性
        :return:
        """
        for attr in dir(self):  # 遍历自己的所有成员
            if attr.startswith("_ele_"):  # 如果是定位表达式
                loc = getattr(self, attr)  # 通过反射获取表达式内容
                ele = self.find_element(loc)  # 定位到元素

                setattr(self, attr, ele)  # 通过反射，保存元素为属性

    def get_msg(self):
        """元素操作的高级方法：获取系统提示"""

        ele = self.find_element('//p[@class="prompt-msg"]')
        return ele.text


class RegPage(BasePage):
    """
    用户注册页面
    """

    _url = "http://101.34.221.219:8010/?s=user/regInfo.html"

    _ele_username = FakeElement(
        "/html/body/div[4]/div/div/div[2]/div/div/div/form/div[1]/input",
    )
    _ele_password = FakeElement(
        "/html/body/div[4]/div/div/div[2]/div/div/div/form/div[2]/div/input",
    )
    _ele_agreement = FakeElement(
        "/html/body/div[4]/div/div/div[2]/div/div/div/form/div[3]/label/span",
    )
    _ele_btn = FakeElement(
        "/html/body/div[4]/div/div/div[2]/div/div/div/form/div[4]/button",
    )

    def input_username(self, username):
        """元素操作的低级方法"""
        self._ele_username.send_keys(username)

    def input_password(self, password):
        """元素操作的低级方法"""
        self._ele_password.send_keys(password)

    def click_agreement(self):
        """元素操作的低级方法"""
        self._ele_agreement.click()

    def click_btn(self):
        """元素操作的低级方法"""
        self._ele_btn.click()

    def submit(self, username, password):
        """元素操作的高级方法：提交表单"""
        self._ele_username.send_keys(username)
        self._ele_password.send_keys(password)
        self._ele_agreement.click()
        self._ele_btn.click()


class LoginPage(BasePage):
    """登录页面"""

    _url = "http://101.34.221.219:8010/?s=user/logininfo.html"

    _ele_username = FakeElement(
        "/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[1]/input"
    )
    _ele_password = FakeElement(
        "/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[2]/div/input"
    )

    _ele_btn = FakeElement(
        "/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[3]/button"
    )

    def submit(self, username, password):
        """元素操作的高级方法：提交表单"""
        self._ele_username.send_keys(username)
        self._ele_password.send_keys(password)
        self._ele_btn.click()


class DetailPage(BasePage):
    _url = "http://101.34.221.219:8010/?s=goods/index/id/5.html"

    _ele_by_count = FakeElement('//*[@id="text_box"]')
    _ele_add_cart = FakeElement(
        "/html/body/div[4]/div[2]/div[2]/div/div[3]/div[2]/button[2]"
    )

    def add_to_crat(self, count):
        """
        元素交互的高级API： 输入数量并加入购物车
        :param count:
        :return:
        """

        self._ele_by_count.send_keys(count)
        self._ele_add_cart.click()
