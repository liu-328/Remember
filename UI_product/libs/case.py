
import unittest
from pathlib import Path

import ddt
from webdriver_helper import get_webdriver

from libs import action


def create_test(test_suite):
    @ddt.ddt
    class Test(unittest.TestCase):
        @classmethod
        def setUpClass(cls) -> None:
            cls.driver = get_webdriver()

        @classmethod
        def tearDownClass(cls) -> None:
            cls.driver.quit()

        @ddt.data(*test_suite["cases"].values())  # 通过数据生成用例
        def test(self, case):
            key_word = action.KeyWord(driver=self.driver)

            for step in case["steps"]:
                print("步骤", step)

                f = getattr(key_word, f"key_{step[0]}")
                f(*step[1])

            print("用例结束")

    return Test


class PytestExcel:
    def __init__(self, base_dir):
        """

        :param base_dir: 指定搜索excel的目录
        """
        self.base_dir = Path(base_dir)
        self.py_path = self.base_dir / "test_beifan.py"

    def put_py(self):
        """
        测试开始前，创建py文件
        :return:
        """
        code = f"""
from glob import glob

from libs import case, data

file_list = glob(r"{self.base_dir.absolute()}\\test_*.xlsx")  # 搜索到多个文件

no = 0

for file in file_list:

    for suite in data.case_by_excel(file):  # 1. 读取数据
        no += 1
        globals()[f"Test_{{no}}"] = case.create_test(suite)  # 2.根据数据生成用例"""
        self.py_path.write_text(code, encoding="utf-8")

    def del_py(self):
        """
        测试结束后，删除py文件
        :return:
        """

        self.py_path.unlink(True)  # 如果文件不存在，不报错
