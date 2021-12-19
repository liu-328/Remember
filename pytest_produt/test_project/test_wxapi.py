# -*- coding: utf-8 -*-
import pytest
import requests
from Commons.request_util import RequestsUtil
from Commons.yaml_util import read_case_yml
from Debug_talk import DebugTalk


class TestWxApi:
    session = requests.session()
    access_token = ''
    id = ''

    @pytest.mark.parametrize('args_name', read_case_yml('/test_project/wx_get_token.yml'))
    def test_get_token(self, args_name):

        RequestsUtil('base_wx_api', DebugTalk()).standard_yaml(args_name)

    @pytest.mark.parametrize('args_name', read_case_yml('/test_project/wx_get_label.yml'))
    def test_get_label(self, args_name):

        RequestsUtil('base_wx_api', DebugTalk()).standard_yaml(args_name)

        # 返序列化
        # a = json.loads(json.dumps(res.json()).replace(r'\\', '\\'))
        # write_relation_yml({'id': res.json()["tag"]['id']})

    @pytest.mark.parametrize('args_name', read_case_yml('/test_project/wx_make_label.yml'))
    def test_make_label(self, args_name):

        RequestsUtil('base_wx_api', DebugTalk()).standard_yaml(args_name)

    @pytest.mark.parametrize('args_name', read_case_yml('/test_project/wx_edit_label.yml'))
    def test_edit_label(self, args_name):

        RequestsUtil('base_wx_api', DebugTalk()).standard_yaml(args_name)

    @pytest.mark.parametrize('args_name', read_case_yml('/test_project/wx_delete_label.yml'))
    def test_delete_label(self, args_name):

        RequestsUtil('base_wx_api', DebugTalk()).standard_yaml(args_name)

    @pytest.mark.parametrize('args_name', read_case_yml('/test_project/wx_upload_api.yml'))
    def test_upload_picture(self, args_name):

        RequestsUtil('base_wx_api', DebugTalk()).standard_yaml(args_name)

