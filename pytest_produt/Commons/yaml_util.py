import os
import yaml


def get_object_path():
    return os.getcwd()


# 读取config.yml文件的base_url
def read_config_yml(one, two):
    with open(get_object_path()+'/config.yml', 'r') as f:
        value = yaml.load(f, Loader=yaml.FullLoader)
        return value['base'][two]


# 读取relation.yml文件保存的关联数据
def read_relation_yml(key):
    with open(get_object_path()+'/relation.yml', 'r', encoding='utf-8') as f:
        value = yaml.load(f, Loader=yaml.FullLoader)
        return value[key]


# 写入relation.yml
def write_relation_yml(data):
    with open(get_object_path()+'/relation.yml', 'a+', encoding='utf-8') as f:
        yaml.dump(data=data, stream=f, allow_unicode=True)


# 清空relation.yml
def clear_relation_yml():
    with open(get_object_path() + '/relation.yml', 'w', encoding='utf-8') as f:
        f.truncate()


# 读取测试用例
def read_case_yml(path):
    with open(get_object_path()+path, 'r') as f:
        value = yaml.load(f, Loader=yaml.FullLoader)
        return value


