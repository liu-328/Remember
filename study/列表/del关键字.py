name_list = ['张三', '李四', '王五']

# （知道）使用del关键字（delete）删除列表中的元素
# 提示：在日常开发中，要从列表删除数据，建议使用列表提供的方法。
del name_list[1]

# del 关键字本质上是用来将一个变量从内存中删除的
name = '小刘'

del name
# 注意 如果使用del关键字将变量删除， 后续就不可以使用这个变量了
# print(name)  # NameError: name 'name' is not defined

print(name_list)




