import json
import re
import jsonpath
import requests
from Commons.yaml_util import read_config_yml, write_relation_yml, read_relation_yml


# 提取关键字实现接口关联
from Debug_talk import DebugTalk


def extract_association(info, response):
    info_keys = info.keys()
    return_txt = response.text

    if 'extract' in info_keys:
        for key, value in info['extract'].items():
            if '(.*?)' in value or '(.+?)' in value:
                regular = re.search(value, return_txt)

                if regular:
                    write_relation = {key: regular.group(1)}
                    write_relation_yml(write_relation)
            else:
                try:
                    return_json = response.json()
                    js_expression = jsonpath.jsonpath(return_json, value)
                    if js_expression:
                        write_relation = {key: js_expression[0]}
                        write_relation_yml(write_relation)
                except Exception:
                    print("返回的结果不是JSON格式，不能使用jsonpath提取")


# 值替换
# 替换值的方法
# 考虑问题1：(替换url,params,data,json,headers)
# 考虑问题2：(string,int,float,list,dict)
def replace_value(data):

    if data:
        # 保存数据类型
        data_type = type(data)
        # 判断数据类型
        if isinstance(data, dict) or isinstance(data, list):
            str_data = json.dumps(data)
        else:
            str_data = str(data)
        for i in range(1, str_data.count('${') + 1):
            if '${' in str_data and '}' in str_data:
                start_str = str_data.index('${')
                end_str = str_data.index('}')
                old_value = str_data[start_str:end_str + 1]
                # new_value = read_relation_yml(old_value[2:-1])
                # str_data = str_data.replace(old_value, new_value)
                # a = getattr(DebugTalk(), old_value)
                print(old_value)
                new_value = old_value[2: old_value.index('}')]
                args = new_value[new_value.index('(')+1:new_value.index(")")]
                print("args: ", args)
                print(new_value)
                # ccc = getattr(DebugTalk(), "get_random")(111, 222)

                ddd = getattr(DebugTalk(), "read_yml")(*args)
                # print(ccc)
                print(ddd)
        if isinstance(data, dict) or isinstance(data, list):
            data = json.loads(str_data)
        else:
            data = data_type(str_data)

    return data


class RequestsUtil:

    session = requests.session()

    # 规范yml
    def standard_yaml(self, info):
        info_keys = info.keys()
        # 判断一级关键字
        if 'name' in info_keys and 'request' in info_keys and 'validate' in info_keys:
            request_key = info['request'].keys()
            # 判断二级关键字
            if 'method' in request_key and 'url' in request_key:
                # 发送请求
                method = info['request'].pop('method')
                url = info['request'].pop('url')
                res = self.send_request(method, url, **info['request'])
                extract_association(info, res)
            else:
                print('在request下必须包含：method,url')
        else:
            print("一级关键字必须要包含：name,request,validate")

    # 读取base_url
    def __init__(self, two):
        self.base_url = read_config_yml('base', two)

    # 请求
    def send_request(self, method, url, **kwargs):
        # 请求方法改成小写
        method = str(method).lower()
        # url拼接
        url = self.base_url + replace_value(url)
        # 替换params,data,json,headers
        for key, values in kwargs.items():
            if key in ['params', 'data', 'json', 'headers']:
                kwargs[key] = replace_value(values)
            elif key == "files":
                for file_key, file_path in values.items():
                    values[file_key] = open(file_path, 'rb')
        # 请求
        res = RequestsUtil.session.request(method, url, **kwargs)
        return res







