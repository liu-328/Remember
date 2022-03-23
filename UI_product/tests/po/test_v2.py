
import pytest
from webdriver_helper import get_webdriver

from libs import pom


@pytest.fixture(scope="session")
def driver():
    d = get_webdriver()  # 启动浏览器

    yield d
    # 关闭浏览器
    d.quit()


@pytest.mark.skip("todo")
def test_rege(driver):
    driver.get("http://101.34.221.219:8010/?s=user/regInfo.html")

    page = pom.RegPage(driver)  # 实例化PO

    page.submit("beifan_002", "123123")  # 提交表单
    msg = page.get_msg()  # 获取系统提示

    assert msg == "注册成功"  # 没有输出，代表测试通过


def test_login(driver, cache):
    driver.get("http://101.34.221.219:8010/?s=user/logininfo.html")

    page = pom.LoginPage(driver)
    page.submit("beifan_002", "123123")

    msg = page.get_msg()

    assert msg == "登录成功"

    cookie = driver.get_cookies()

    cache.set("cookie", cookie)  # 暂存cookies


def test_detail_to_cart(driver, cache):
    driver.maximize_window()
    driver.get("http://101.34.221.219:8010/?s=goods/index/id/5.html")

    cookie = cache.get("cookie", {})  # 读取cookie
    for c in cookie:
        driver.add_cookie(c)  # 设置cookie

    driver.refresh()  # 刷新页面，变成已登录状态

    page = pom.DetailPage(driver)
    page.add_to_crat(2)

    msg = page.get_msg()

    assert msg == "加入成功"
