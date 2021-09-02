info_tuple = ('zhangsan', 18, 1.75)

# 使用迭代遍历元组
for my_info in info_tuple:
    # 使用格式化字符串拼接 吗，info_tuple 这个变量不方便
    # 因为元组中一般包含的数据类型是不同的
    print('元组中包含的元素有 %s' % my_info)
# 使用迭代遍历元组索引
for index in range(len(info_tuple)):

    print(index, info_tuple[index])









