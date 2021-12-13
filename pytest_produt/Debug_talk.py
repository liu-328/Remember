import random

from Commons.yaml_util import read_relation_yml


class DebugTalk:

    def get_random(self, min_number, max_number):
        return random.randint(min_number, max_number)

    def read_yml(self, key):
        return read_relation_yml(key)

#
# a = 'aaa, bbb'
# print(a.split(''))