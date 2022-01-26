# fixture固件保存位置
import pytest

from Commons.yaml_util import clear_relation_yml


@pytest.fixture(scope='function')
def browser_login():
    print('登录')
    yield
    print('退出登录')


@pytest.fixture(scope='class')
def open_browser():
    print('打开浏览器')
    yield
    print('关闭浏览器')


@pytest.fixture(scope='module', autouse=False)
def module_fix():
    print('模块前置')
    yield
    print('模块后置')


@pytest.fixture(scope='session', autouse=False)
def session_fix():
    print("会话前置")
    yield
    print('会话后置')


@pytest.fixture(scope='session', autouse=True)
def clear_relation():
    clear_relation_yml()
