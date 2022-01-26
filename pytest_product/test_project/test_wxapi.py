# -*- coding: utf-8 -*-
import pytest
from Commons.request_util import RequestsUtil
from Debug_talk import DebugTalk
from Commons.parametrize_util import read_case_yml


class TestWxApi:

    @pytest.mark.parametrize('args_name', read_case_yml('/test_project/wx_get_token.yml'))
    def test_get_token(self, args_name):
        RequestsUtil('base_wx_api', DebugTalk()).standard_yaml(args_name)

    @pytest.mark.parametrize('args_name', read_case_yml('/test_project/wx_get_label.yml'))
    def test_get_label(self, args_name):

        RequestsUtil('base_wx_api', DebugTalk()).standard_yaml(args_name)

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

