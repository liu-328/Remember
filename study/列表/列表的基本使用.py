name_list = ['zhangsan', 'lisi', 'wangwu']

# 1. 取值和索引
print(name_list[2])

# 知道数据的内容，想确定数据在列表中的位置
# 使用index方法需要注意，如果传递的数据不在列表中会报错。
print(name_list.index('zhangsan'))

# 2.修改
# 中括号内部使用索引超出范围会报错
name_list[2] = 'liu'

# 3.增加
# append 方法用于在列表末尾添加数据
name_list.append('王小二')

# insert 方法用于在列表的指定位置插入数据
name_list.insert(1, '小刘')

# extend 方法可以把其他列表中的完整内容，追加到当前列表的末尾
temp_list = ['孙悟空', '猪二哥', '沙三弟']
name_list.extend(temp_list)

# 4.删除
# remove 方法可以从列表中删除指定的数据
name_list.remove('liu')

# pop 方法默认删除列表中最后一个元素删除
name_list.pop()

# pop 方法可以指定要删除元素的索引
name_list.pop(3)

# clear 方法可以清空整个列表
name_list.clear()

print(name_list)


