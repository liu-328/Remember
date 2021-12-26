import json
import traceback

import yaml

from Commons.logger_util import error_log
from Commons.yaml_util import get_object_path, read_data_yml


# 读取DDT数据
def read_case_yml(path):
    try:
        with open(get_object_path()+path, 'r', encoding='utf-8') as f:
            value = yaml.load(f, Loader=yaml.FullLoader)
            if len(value) >= 2:
                return value
            else:
                if 'parameterize' in dict(*value).keys():
                    return ddt(*value)
                else:
                    return value
    except Exception as e:
        error_log('读取DDT数据read_case_yml方法异常：%s' % str(traceback.format_exc()))


# DDT数据驱动
def ddt(args_name):
    try:
        new_args_name = []
        if 'parameterize' in args_name.keys():
            caseinfo_str = json.dumps(args_name)
            for param_key, param_value in args_name['parameterize'].items():
                key_list = param_key.split('-')
                data_list = read_data_yml(param_value)
                # 规范写法
                long_flag = True
                for data in data_list:
                    if len(data) != len(key_list):
                        long_flag = False
                        break
                if long_flag:
                    for x in range(1, len(data_list)):  # 循环数据行数
                        temp_caseinfo = caseinfo_str
                        for y in range(0, len(data_list[x])):  # 循环数据列数
                            if data_list[0][y] in key_list and data_list[0][y] == key_list[y]:
                                # 替换值
                                if isinstance(data_list[x][y], int) or isinstance(data_list[x][y], float):
                                    temp_caseinfo = temp_caseinfo.replace('"' + "$ddt{" + data_list[0][y] + "}" + '"',
                                                                          str(data_list[x][y]))
                                else:
                                    temp_caseinfo = temp_caseinfo.replace("$ddt{" + data_list[0][y] + "}",
                                                                          str(data_list[x][y]))
                            else:
                                print('DDT数据异常')
                                break
                        new_args_name.append(json.loads(temp_caseinfo))
            return new_args_name
        else:
            return args_name
    except Exception as e:
        error_log('ddt数据驱动方法异常：%s' % str(traceback.format_exc()))