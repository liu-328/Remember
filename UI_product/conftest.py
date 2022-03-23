

from libs import case

obj = case.PytestExcel(r"tests\excel")

# pytest hooks


def pytest_configure():
    """
    pytest 启动的时候自动调用
    :return:
    """
    obj.put_py()


def pytest_terminal_summary():
    """
    pytest 执行完成的之后，自动调用
    :return:
    """
    obj.del_py()
