import random
import requests

from Commons.yaml_util import read_relation_yml


class DebugTalk:

    def get_random(self, min_number, max_number):
        min_number = int(min_number)
        max_number = int(max_number)
        return str(random.randint(min_number, max_number))

    def read_relation_data(self, key):
        return read_relation_yml(key)

#
# a = 'aaa, bbb'
# print(a.split(''))
