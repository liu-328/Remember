name_list = ['张三', '李四', '王五', '张三']

# len（lenght 长度） 函数可以统计列表的长度
list_len = len(name_list)

print('列表中包含 %d 个元素' % list_len)

# count 方法可以统计列表中某一个数据出现的次数
count = name_list.count('张三')
print('列表中张三出现了 %d 次' % count)
print(name_list.count('张三'))

# remove 从列表中删除数据（如果列表内有两个一样的元素），如果数据不存在，程序会报错value error
name_list.remove('张三')

print(name_list)









