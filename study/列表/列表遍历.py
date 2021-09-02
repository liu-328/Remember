name_list = ['zhangsan', 'lisi', 'wangwu', 'xiaoliu']

# 使用迭代遍历列表
for name in name_list:

    print(name)
# 使用迭代遍历列表索引
for index in range(len(name_list)):

    # 因为index表示的为元素索引，循环列表a内的索引就对应的为name_list[0],name_list[1]...所以name_list[index]=对应索引的元素
    print('list_name中第 {} 个元素为 {}'.format(index, name_list[index]))











