# 跳过测试用例
import pytest
age = 10


@pytest.mark.usefixtures('open_browser')
class TestOne:

    # @pytest.mark.skip(reason='没有理由')
    def test_one(self, browser_login):
        print('测试1')
        assert 1 == 1

    @pytest.mark.skipif(age > 10, reason='年龄大于10跳过')
    def test_two(self):
        print('测试2')
        assert 'h' in 'hello'


class TestTwo:

    def test_three(self, base_url):
        print('测试3')
        assert 1 == 1
