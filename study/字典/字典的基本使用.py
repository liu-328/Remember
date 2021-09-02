xiaoming_dict = {'name': '小明'}

# 1.取值
print(xiaoming_dict['name'])
a = xiaoming_dict['name']
print(a)

# 2.增加/修改
# 如果key不存在，新增键值对，如果key存在会修改已经存在的键值对
xiaoming_dict['age'] = 18
xiaoming_dict['name'] = '小刘'

# 3.删除
xiaoming_dict.pop('name')
xiaoming_dict.clear()

print(xiaoming_dict)


