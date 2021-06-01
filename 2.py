# import random
# # 剪刀 = 0， 石头 = 1， 布 = 2
# player = int(input("石头剪刀布："))
# while True:
#     computer = random.randint(0, 2)
#     if player == 3:
#         print("游戏结束")
#         break
#     if player > 3:
#         player = int(input("请输入正确的数字："))
#     elif (player == 0 and computer == 2) or (player == 2 and computer == 1) or (player == 1 and computer == 0):
#         print("玩家：%d, 电脑： %d" % (player, computer))
#         print("恭喜你胜利了")
#         player = int(input("石头剪刀布："))
#     elif player == computer:
#         print("玩家：%d, 电脑： %d" % (player, computer))
#         print("不要走决战到天亮")
#         player = int(input("石头剪刀布："))
#     else:
#         print("玩家：%d, 电脑： %d" % (player, computer))
#         print("失败咯")
#         player = int(input("石头剪刀布："))

# sum = 0
# a = 1
# while a <= 100:
#     sum = sum + a
#     a += 1
#     print(sum)

# i = 1
# sum = 0
#
# while i <= 100:
#     if i % 2 == 0:
#         sum = sum + i
#
#     i = i + 1
#
# print("1--100之间的偶数和为 %d " % sum)

# i = 1
# jishu = 0
# while i <= 100:
#     if i % 2 == 1:
#         jishu = jishu + i
#     i = i + 1
# print(jishu)

# print(bin(112))         # 10转2进制
# print(oct(112))         # 10转8进制
# print(hex(112))         # 10转16进制
# print(int(0b1110000))   # 2转10进制
# print(int(0o160))       # 2转8进制
# print(int(0x70))        # 2转16进制

"""
小数计算引用decimal库里面的Decimal进行计算
"""
# from decimal import Decimal
# print(Decimal('11.2') + Decimal('11.2') - Decimal('22.4'))
# print(6 ** 2)
import platform

"""
    对于不可变类型的对象，内存可能会被重用，比如小的整数对象，。
    使用id函数进行验证，内置函数id用于返回对象的唯一标识。（对象在内存中的唯一地址）
"""
# a = 9992
# b = 9902
# print(a == b)  # False
# print(id(a))  # 4502353168
# print(id(b))  # 4502353232

# a = 12
# print(id(a))
# b = 122
# print(id(b))
# print(a == b)
# print(a is b)
#  "is"是比较的是两个对象的id值是否相等，也就是比较俩对象是否为同一个实例对象，是否指向同一个内存地址。

"""
对象None 用于变量的初始化，或将变量重置为"数据值不存在的状态"
"""

# a = 1
# print(a)
# a = None
# print(a)

""" 
    range是一种序列类型，表示不可变的整数序列
    可以调用内置函数range，创建range类型的对象，有三种方式
    range(stop)   传入一个参数
    range(start,stop)  传入两个参数
    range(start,stop,step)  传入三个参数
其中，整数序列的起始的默认值为0.使用参数start指定；
     可以使用参数stop指定整数序列的结束值；创建的range对象不包含stop
     整数序列的布长的默认值为1，使用参数step指定
     
     内置函数range返回值是一个迭代的对象，为了清楚的标识返回的迭代器对象所表示的整数序列，
     可以将其转换成列表
     不管range对象有多长，所有range对象所占用的内存空间都是相同的，
     只需要存储start，stop，step。只有用到range对象的时候，才会去计算序列中的相关元素
"""
#
# print(range(5))
#
# print(list(range(5)))
#
# print(list(range(0, 5, 2)))
#
# print(3 in range(5))  # 用in来检查range5中是否含有整数3
# print(6 not in range(5))  # 用not in 来检查range5中是否不存在整数8

# A = [i for i in range(1,101)]
# print(A[::-1])
"""
列表创建:
L = [1, 2, 3, 4]
print(L)

print(list(range(1, 5)))

print(list())
"""

# 调用索引index

# a = [1, 2, 3, 4, 5, 3, 6]
# print(a.index(3))  # 2

"""
    如果列表中含有多个指定元素，index返回第一个指定元素的索引
    如果列表中不存在指定元素，index返回 ValueError
    调用index时使用起始索引start结束索引stop。
    起始索引包含指定索引，
    结束索引不包含指定索引。
"""

# print(a.index(3, 3))  # 从索引 3 开始，查找元素 3 在列表中的索引。
# print(a.index(3, 3, 6))  # 从索引 3 开始，索引 6 结束， 在列表中查找元素 3 在列表中的索引。

# 使用索引获得列表中的单个元 素，
# a = [1, 2, 3, 4, 5]
# print(a[1])
# print(a[-4])

# a = [1, 2, 3, 4, 5, 6]
# print(a[::-1])
#
# print(4 in a)
# print(9 in a)
# print(4 not in a)
# print(9 not in a)
"""
    修改列表中的元素，
未指定索引的元素赋予一个新值。(一次只修改一个元素)
为指定的切片赋予一个新值。(一次至少修改一个新值)
"""

# a = [1, 2, 3, 4, 5]
# a[2] = 9
# print(a)

# 二

# a[1:3] = [99, 12]
# print(a)
# a[0:1] = [5]
# print(a)
# a[1:4] = [1, 7]
# print(a)

"""
    列表末尾添加一个元素(只添加一个元素)
"""
# a = [1, 2, 3, 4, 5]

# a.append(6)
# print(a)

# a.append([7, 8, 9])  # [1, 2, 3, 4, 5, 6, [7, 8, 9]]
# print(a)
"""
列表末尾添加多个元素。(至少添加一个元素)
"""
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# a.extend([10, 11])
# print(a)

"""
列表中任意位置插入一个元素，使用insert
"""

# a = [1, 2, 3, 4, 5]

# a.insert(3, 5)
# print(a)  # [1, 2, 3, 5, 4, 5]
#
# a.insert(len(a), 6)   # 使用内置函数len ，获取列表中的元素个数。
# print(a)

"""
    为指定的切片赋予一个新值(在列表中的任意位置一次至少添加一个元素)
"""

# a = [1, 2, 3, 4, 5]
#
# a[2:2] = [9, 6]
# print(a)  # [1, 2, 9, 6, 3, 4, 5]
#
# a[len(a):] = [6, 7]  # [1, 2, 9, 6, 3, 4, 5, 6, 7]
# print(a)

# a = [1, 2, 3, 5, 2, 6, 7]
#
# a[2:5] = [3, 4, 5]
# print(a)

#
#  data：6.1
"""
列表的删除操作：
调用remove方法，指定的为元素
"""
# a = [3, 4, 5, 6, 7]
# a.remove(5)
# print(a)  # [3, 4, 6, 7]
#
# b = [3, 4, 5, 4, 6]
# b.remove(4)
# print(b)  # [3, 5, 4, 6]  如果存在多个相同元素，，只删除第一个元素。

"""
调用方法pop（一次只删除一个指定索引的元素）
返回被删除的元素
"""
# a = [3, 4, 5, 6, 7]
# a.pop(2)
# print(a)  # [3, 4, 6, 7]
#
# print(a.pop(2))  # 6
#
# print(a)  # [3, 4, 7]
#
# print(a.pop())  # 7 如果未指定元素，删除列表中最后一个元素
# print(a)  # [3, 4]
"""
使用del语句，一次至少删除一个元素。
"""

# a = [1, 2, 3, 4, 5, 6]
# del a[2]
# print(a)   # [1, 2, 4, 5, 6]
# del a[1:3]  # [1, 5, 6] 通过列表切片，一次删除多个元素。
# print(a)

"""
给指定的切片赋值一个空列表，一次至少删除一个元素 
"""
# a = [1, 2, 3, 4, 5, 6]
#
# a[3:4] = []
# print(a)  # [1, 2, 3, 5, 6]
# # 请空列表
# a[:] = []
# print(a)  # []

"""
使用clear请空列表
"""

# a = [1, 2, 3, 4, 5, 6]
#
# a.clear()
# print(a)  # []

"""
使用加法运算列表
可以使用加法运算符将两个列表合并后生成一个新的列表，被合并的列表不发生任何变化。
"""

# a1 = [1, 2, 3]
# a2 = [4, 5, 6]
# a3 = a1 + a2
# print(a3)  # [1, 2, 3, 4, 5, 6]
# print(a2)  # [4, 5, 6]
# print(a1)  # [1, 2, 3]

# a1 = a2 = [1, 2]
# a1 = a1 + [3, 4]
# print(a1, a2)  # [1, 2, 3, 4] [1, 2]
#
# a1 = a2 = [1, 2]
# a1 += [3, 4]
# print(a1, a2)  # [1, 2, 3, 4] [1, 2, 3, 4] 参数赋值运算符+= ，会对列表本身进行修改。

"""
使用乘法运算列表
被乘的列表不发生任何变化，被乘后的列表重复打印*次，生成一个新的列表。 
"""
# a1 = [1, 2, 3, 4]
# a = a1 * 3
# print(a)  # [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
# print(a1)  # [1, 2, 3, 4]
#
# a = [0] * 5
# print(a)  # [0, 0, 0, 0, 0]  常用于列表的初始化。

# a1 = a2 = [1, 2, 3]
# a1 = a1 * 3
# print(a1, a2)  # [1, 2, 3, 1, 2, 3, 1, 2, 3] [1, 2, 3]
#
# # 参数赋值运算，使用*=会对列表进行更改，会对列表本身进行修改
#
# a1 = a2 = [1, 2, 3]
# a1 *= 3
# print(a1)  # [1, 2, 3, 1, 2, 3, 1, 2, 3]
# print(a2)  # [1, 2, 3, 1, 2, 3, 1, 2, 3]


