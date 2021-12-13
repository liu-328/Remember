# -*- coding: utf-8 -*-
import json
import re
import pytest
import requests
import random
from Commons.request_util import RequestsUtil
from Commons.yaml_util import write_relation_yml, read_relation_yml, read_case_yml


class TestWxApi:
    session = requests.session()
    access_token = ''
    id = ''

    @pytest.mark.parametrize('args_name', read_case_yml('/test_project/wx_get_token.yml'))
    def test_get_token(self, args_name):

        RequestsUtil('base_wx_api').standard_yaml(args_name)
        # write_relation_yml({'access_token': res.json()['access_token']})
        # TestWxApi.access_token = res.json()["access_token"]

        # 正则表达式
        # TestWxApi.csrf_token = re.search('name="csrf_token" value="(. *?)"', res.text)[1]

    # @pytest.mark.parametrize('args_name', read_case_yml('/test_project/wx_get_label.yml'))
    # def test_get_label(self, args_name):
    #     RequestsUtil('base_wx_api').standard_yaml(args_name)

    @pytest.mark.parametrize('args_name', read_case_yml('/test_project/wx_make_label.yml'))
    def test_build_label(self, args_name):
        RequestsUtil('base_wx_api').standard_yaml(args_name)

        # 返序列化
        # a = json.loads(json.dumps(res.json()).replace(r'\\', '\\'))
        # write_relation_yml({'id': res.json()["tag"]['id']})
    #
    # def test_edit_label(self):
    #
    #     urls = "/tags/update?access_token="+read_relation_yml('access_token')
    #
    #     jsons = {"tag": {"id": read_relation_yml('id'), "name": '修改'+str(random.randint(00000, 99999))}}
    #
    #     RequestsUtil('base_wx_api').send_request('post', url=urls, json=jsons)
    #
    # def test_delete_label(self):
    #
    #     urls = "/tags/delete?access_token="+read_relation_yml('access_token')
    #
    #     jsons = {"tag": {"id": read_relation_yml('id')}}
    #
    #     RequestsUtil("base_wx_api").send_request('post', url=urls, json=jsons)
    #
    # # 数据驱动
    # @pytest.mark.parametrize('args_name', read_case_yml('/test_project/wx_upload_api.yml'))
    # def test_upload_picture(self, args_name):
    #     name = args_name['name']
    #     headers = args_name['request']['headers']
    #     validate = args_name['validate']
    #     methods = args_name['request']['method']
    #     datas = args_name['request']['datas']
    #
    #     urls = args_name['request']['url']+read_relation_yml('access_token')
    #     for key, value in dict(datas).items():
    #         datas[key] = open(value, 'rb')
    #     print(RequestsUtil("base_wx_api").send_request('post', url=urls, files=datas))
    #
    #
