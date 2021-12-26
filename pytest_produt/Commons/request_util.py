import json
import re
import traceback

import jsonpath
import requests

from Commons.logger_util import error_log, logs
from Commons.yaml_util import read_config_yml, write_relation_yml


class RequestsUtil:

    session = requests.session()

    # 读取base_url
    def __init__(self, two, obj):
        self.base_url = read_config_yml('base', two)
        self.obj = obj

    # 规范yml
    def standard_yaml(self, info):
        try:
            logs('---------------测试开始---------------')
            info_keys = info.keys()
            # 判断一级关键字
            if 'name' in info_keys and 'request' in info_keys and 'validate' in info_keys:
                request_key = info['request'].keys()
                # 判断二级关键字
                if 'method' in request_key and 'url' in request_key:
                    # 发送请求
                    method = info['request'].pop('method')
                    url = info['request'].pop('url')
                    name = info['name']
                    logs('接口名称：%s' % name)
                    res = self.send_request(method, url, **info['request'])
                    extract_association(info, res, self.obj)
                else:
                    error_log('在request下必须包含：method,url')
            else:
                error_log("一级关键字必须要包含：name,request,validate")
        except Exception as e:
            error_log('规范yml方法standard_yaml异常：%s' % str(traceback.format_exc()))

    # 请求
    def send_request(self, method, url, **kwargs):
        try:
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
            logs('请求方法：%s' % method)
            logs('请求路径：%s' % url)
            logs('接口参数：%s' % url)
            if 'headers' in kwargs.keys():
                logs('请求头：%s' % kwargs['headers'])
            if 'params' in kwargs.keys():
                logs('接口参数params：%s' % kwargs['params'])
            elif 'data' in kwargs.keys():
                logs('接口参数data：%s' % kwargs['data'])
            elif 'json' in kwargs.keys():
                logs('接口参数json：%s' % kwargs['json'])
            if "files" in kwargs.keys():
                logs('文件上传：%s' % kwargs["files"])
            # 请求
            res = RequestsUtil.session.request(method, url, **kwargs)
            return res
        except Exception as e:
            error_log('发送请求方法standard_yaml异常：%s' % str(traceback.format_exc()))


# 值替换
# 替换值的方法
# 考虑问题1：(替换url,params,data,json,headers)
# 考虑问题2：(string,int,float,list,dict)
def replace_value(data, obj):

    try:
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
    except Exception as e:
        error_log('替换值方法replace_value异常：%s' % str(traceback.format_exc()))


# 提取关键字实现接口关联
def extract_association(info, response, obj):
    try:
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
                        error_log("返回的结果不是JSON格式，不能使用jsonpath提取")

        # 断言值的替换
        try:
            for i in info['validate']:
                for validate_key, validate_value in i.items():
                    if validate_key == 'equals':
                        for k, v in validate_value.items():
                            validate_value[k] = replace_value(v, obj)
                    if validate_key == 'contains':
                        replace_value(validate_value, obj)
        except Exception as e:
            error_log('断言值替换异常')

        # 断言
        assert_result(info['validate'], response, response_code)
    except Exception as e:
        error_log('提取关键字实现接口关联方法extract_association异常：%s' % str(traceback.format_exc()))


# 断言
def assert_result(validate, response, response_code):
    try:
        logs('预期结果：%s' % validate)
        logs('实际结果：%s' % response.text)
        flag = 0
        if response_code != 200:
            error_log('断言失败：返回的状态码不等于200')
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
                            error_log('暂不支持的断言方式')
        except:
            return_txt = response.text
            for expect_result in validate:
                for key, value in expect_result.items():
                    if key == 'contains':
                        flag += assert_contains(value, return_txt)

        assert flag == 0
        logs('测试成功')
        logs('---------------接口测试结束---------------\n')

    except Exception as e:
        logs('测试失败')
        logs('---------------接口测试结束---------------\n')
        error_log('断言方法assert_result异常：%s' % str(traceback.format_exc()))


# 相等断言
def assert_equals(value, return_json):
    flag = 0
    for assert_key, assert_value in value.items():
        # print(key, value, '11111111')
        if assert_key == 'equals':
            lists = jsonpath.jsonpath(return_json, '$..%s' % assert_key)
            if lists:
                if assert_value not in lists:
                    error_log('断言失败：%s的值不为%s' % (assert_key, assert_value))
                    flag += 1
            else:
                error_log('断言失败：返回结果内不存在%s' % assert_key)
                flag += 1

    return flag


# 包含断言
def assert_contains(value, response):
    flag = 0
    if str(value) not in response:
        error_log('断言失败%s不在%s内' % (value, response))
        flag += 1

    return flag


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
