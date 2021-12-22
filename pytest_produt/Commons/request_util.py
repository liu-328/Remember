import json
import re
import jsonpath
import requests
from Commons.yaml_util import read_config_yml, write_relation_yml


# 提取关键字实现接口关联
def extract_association(info, response, obj):
    info_keys = info.keys()
    return_txt = response.text
    response_code = response.status_code

    if 'extract' in info_keys:
        for key, value in info['extract'].items():
            if '(.*?)' in value or '(.+?)' in value:
                regular = re.search(value, return_txt)
                if regular:
                    # 判断提取值类型
                    if regular.group(1).isdigit():
                        write_relation_yml({key: int(regular.group(1))})

                    elif isfloat(regular.group(1)) is True:
                        write_relation_yml({key: float(regular.group(1))})

                    else:
                        write_relation_yml({key: regular.group(1)})
            else:
                try:
                    return_json = response.json()
                    js_expression = jsonpath.jsonpath(return_json, value)

                    if js_expression:
                        write_relation_yml({key: js_expression[0]})
                except Exception:
                    print("返回的结果不是JSON格式，不能使用jsonpath提取")

    # 断言值的替换
    for i in info['validate']:
        for validate_key, validate_value in i.items():
            if validate_key == 'equals':
                for k, v in validate_value.items():
                    validate_value[k] = replace_value(v, obj)
            if validate_key == 'contains':
                replace_value(validate_value, obj)

    # 断言
    assert_result(info['validate'], response, response_code)


# 断言
def assert_result(validate, response, response_code):
    flag = 0
    if response_code != 200:
        print('断言失败：返回的状态码不等于200')
        flag += 1
    try:
        if response.json():
            return_json = response.json()
            for expect_result in validate:
                for key, value in expect_result.items():
                    # print(key, value)
                    if key == 'equals':
                        flag += assert_equals(value, return_json)
                    elif key == 'contains':
                        flag += assert_contains(value, response.text)
                    else:
                        print('暂不支持的断言方式')
    except:
        return_txt = response.text
        for expect_result in validate:
            for key, value in expect_result.items():
                if key == 'contains':
                    flag += assert_contains(value, return_txt)

    assert flag == 0


# 相等断言
def assert_equals(value, return_json):
    flag = 0
    for assert_key, assert_value in value.items():
        # print(key, value, '11111111')
        if assert_key == 'equals':
            lists = jsonpath.jsonpath(return_json, '$..%s' % assert_key)
            if lists:
                if assert_value not in lists:
                    print('断言失败：%s的值不为%s' % (assert_key, assert_value))
                    flag += 1
            else:
                print('断言失败：返回结果内不存在%s' % assert_key)
                flag += 1

    return flag


# 包含断言
def assert_contains(value, response):
    flag = 0
    str_return = json.dumps(response)
    if value not in str_return:
        print('断言失败%s不在%s内' % (value, str_return))
        flag += 1

    return flag


# 值替换
# 替换值的方法
# 考虑问题1：(替换url,params,data,json,headers)
# 考虑问题2：(string,int,float,list,dict)
def replace_value(data, obj):

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
                func = old_value[2: old_value.index('(')]
                args = old_value[old_value.index('(')+1:old_value.index(")")]
                args1 = args.split()
                args2 = args.split(',')
                if args2 is None:
                    new_value = getattr(obj, func)
                else:
                    new_value = getattr(obj, func)(*args2)
                if isinstance(new_value, int) or isinstance(new_value, float):
                    str_data = str_data.replace('"'+old_value+'"', str(new_value))
                else:
                    str_data = str_data.replace(old_value, str(new_value))
        if isinstance(data, dict) or isinstance(data, list):
            data = json.loads(str_data)
        else:
            data = data_type(str_data)
    return data


# 判断浮点数：
def isfloat(str_num):
    s = str_num.split('.')
    if len(s) > 2:
        return False
    else:
        for int_str in s:
            if int_str.isdigit() is False:
                return False
        return True

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
                extract_association(info, res, self.obj)
            else:
                print('在request下必须包含：method,url')
        else:
            print("一级关键字必须要包含：name,request,validate")

    # 读取base_url
    def __init__(self, two, obj):
        self.base_url = read_config_yml('base', two)
        self.obj = obj

    # 请求
    def send_request(self, method, url, **kwargs):

        # 请求方法改成小写
        method = str(method).lower()
        # url拼接
        url = self.base_url + replace_value(url, self.obj)
        # 替换params,data,json,headers
        for key, values in kwargs.items():
            if key in ['params', 'data', 'json', 'headers']:
                kwargs[key] = replace_value(values, self.obj)
            elif key == "files":
                for file_key, file_path in values.items():
                    values[file_key] = open(file_path, 'rb')
        # 请求
        res = RequestsUtil.session.request(method, url, **kwargs)
        print(res.text)
        return res






