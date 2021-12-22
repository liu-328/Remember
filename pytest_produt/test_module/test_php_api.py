import pytest
from Commons.request_util import RequestsUtil
from Commons.yaml_util import read_case_yml
from Debug_talk import DebugTalk


class TestPhPApi:

    @pytest.mark.parametrize('args_name', read_case_yml('/test_module/php_home_page.yml'))
    def test_php_home(self, args_name):

        RequestsUtil('base_php_api', DebugTalk()).standard_yaml(args_name)
