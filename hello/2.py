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
#     if (player == 0 and computer == 2) or (player == 2 and computer == 1) or (player == 1 and computer == 0):
#         print("玩家：%d, 电脑： %d" % (player, computer))
#         print("恭喜你胜利了")
#         player = int(input("石头剪刀布："))
#         if player == computer:
#             print("玩家：%d, 电脑： %d" % (player, computer))
#             print("不要走决战到天亮")
#             player = int(input("石头剪刀布："))
#         else:
#             print("玩家：%d, 电脑： %d" % (player, computer))
#             print("失败咯")
#             player = int(input("石头剪刀布："))

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
# import platform
# import distutils.filelist

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
为指定索引的元素赋予一个新值。(一次只修改一个元素)
为指定的切片赋予一个新值。(一次至少修改一个新值)
"""

# a = [1, 2, 3, 4, 5]
# a[2] = 9
# print(a)

# 二

# a[1:3] = [99, 12]
# print(a)  # [1, 99, 12, 4, 5]
# a[0:1] = [5]
# print(a)
# a[1:4] = [1, 7]
# print(a)  # [1, 1, 7, 5]

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

# a[2:2] = [9, 6]
# print(a)  # [1, 2, 9, 6, 3, 4, 5]

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
使用del语句，一次至少删除一个元素。del指定索引
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

"""
比较运算符对两个列表比较
> , >= , >= , < , <= , == , !=
从第一个元素进行比较，如果相等比较下一个元素，以此类推，直到两个元素不相等。两个列表中所有元素都不被比较
"""
# a = [1, 2, 3, 4, 5]
# b = [1, 2, 3, 5, 6]
# print(a > b)  # False
#
# print([3, [2, 6]] > [3, [2, 5]])  # Ture
"""
也可以使用is进行比较  
is是同一性测试， == 是相同性测试
"""
# a = b = [1, 2, 3]
# c = [1, 2, 3]
#
# print(a == b)  # True
# print(a == c)  # True
#
# print(a is b)  # True
# print(a is c)  # False
"""
列表的翻转：
1、调用方法reverse
"""
# a = [1, 2, 3, 4, 5]
# a.reverse()
# print(a)
#
# # 2.调用内置函数reversed    返回值为迭代器对象，且被翻转的列表不发生变化。
# a = [1, 2, 3 , 4, 5]
#
# print(reversed(a))  # <list_reverseiterator object at 0x10e0ebfa0> = 列表翻转迭代器对象
# print(list(reversed(a)))  # [5, 4, 3, 2, 1]

"""
列表的排序
1，对列表中的所有元素进行排序，调用方法sort,默认按照从小到大排序.
"""

# a = [2, 4, 5, 7, 6]
# a.sort()
# print(a)  # [2, 4, 5, 6, 7]

"""
调用方法 sort时，可以指定参数reverse = Ture ，从大到小排序
"""

# a.sort(reverse=True)  # [2, 4, 5, 6, 7]
# print(a)

"""
2.调用内置函数sorted 
    内置函数sorted的返回值是排序后的新列表，且排序的列表不发生变化。
"""

# a = [2, 4, 5, 7, 6]
# print(sorted(a))  # [2, 4, 5, 6, 7]
# print(a)  # [2, 4, 5, 7, 6]

"""
2.调用内置函数sorted时，可以指定参数reverse = Ture ，从大到小排序
"""

# print(sorted(a, reverse=True))  # [7, 6, 5, 4, 2]
# print(a)  # [2, 4, 5, 7, 6]


"""
多维列表
当列表中的元素也是列表，就构成了多维列表，例如:当列表中的元素是一维列表时，就构成了二维列表，；当列表中的元素是二维列表时，
就构成了三维列表，因此，可以把多维列表看做是特殊的一维列表。

1、一维列表的操作也适用于多维列表
"""
# a = [[3, 4], [1, 5, 2], [3, 4, 5, 6]]
#
# print(a[2][3])  # 6  在列表a中索引为2 里面 索引为 3 的 元素为6
#
# a[1] = 2  # 把列表内索引为1的元素重新赋值为2
# print(a)  # [[3, 4], 2, [3, 4, 5, 6]]
#
# a.append([3, 4])  # 在列表的末尾添加一个元素
# print(a)  # [[3, 4], 2, [3, 4, 5, 6], [3, 4]]
#
# a.extend([[3, 4], [5, 6]])  # 在列表的末尾添加多个元素
# print(a)  # [[3, 4], 2, [3, 4, 5, 6], [3, 4], [3, 4], [5, 6]]
#
# a.remove([5, 6])  # 指定元素为[5, 6]的进行删除。
# print(a)  # [[3, 4], 2, [3, 4, 5, 6], [3, 4], [3, 4]]
#
# a.pop(3)  # 删除指定列表索引为3的指定元素 一次只能删除一个，如果未指定索引，默认删除最后一个元素
# print(a)  # [[3, 4], 2, [3, 4, 5, 6], [3, 4]]  pop指定的为列表的索引
#
# del a[2:3]  # 删除指定索引到结束索引内的元素
# print(a)  # [[3, 4], 2, [3, 4]]
#
# b = [[3, 4], 2, [3, 4, 5, 6], [3, 4], [3, 4], [5, 6]]
#
# del b[2:len(b)]  # 删除指定索引到列表最后的所有元素。
# print(b)  # [[3, 4], 2]
#
# b.insert(1, [[1, 2], [2, 3]])  # 在指定元素位置前，添加元素
# print(b)  # [[3, 4], [[1, 2], [2, 3]], 2]
#
# """
# 多维列表的初始化
# """
# # 一维列表初始化
# print([0] * 3)  # [0, 0, 0]
#
# # 多维列表的初始化
# print([[0] * 3] * 4)  # [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
#
# # 列表生成式
# print([0 for i in range(3)])  # [0, 0, 0]
#
# print([[0 for i in range(3)] for j in range(4)])  # [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]


# print([[[0] * 3] for i in range(4)])  # [[[0, 0, 0]], [[0, 0, 0]], [[0, 0, 0]], [[0, 0, 0]]]

"""
 元组：内置数据结构之一
元组和列表的区别:列表可以更改，列表用[]表示
              元组不可以更改，用()表示
"""
# a = ("hello", 1, True)
# print(a)  # ('hello', 1, True)
#
# a = "hello", 1, True  # 小括号是可以省略的
# print(a)  # ('hello', 1, True)

"""
空列表的表示方式：
"""

# a = (())
# print(a)  # ()
#
# a = (tuple())
# print(a)  # ()

"""
不可变类型的对象，对象内部所有数据就不能被修改了，这样就避免了由于修改数据导致的错误。此外，对于不可变类型的对象，
在多任务环境下同时操作对象时不需要加锁。因此，在程序中尽量使用不可变类型的对象。
"""

# a = ("hello", 1, True)
# # a[1] = 2
# print(a)  # TypeError: 'tuple' object does not support item assignment

# a = ("hello", [1, 2, 3], True)
# a[1][2] = 3
# print(a)  # ('hello', [1, 2, 3], True)
# 元组内的列表是可以进行更改的，因为元组储存的是元素在内存的地址，因此，地址不可以改变，地址内可以改变

"""
只包含一个元素的元组
"""

# a = (11)
# print(a)  # 11
# print(type(a))  # <class 'int'>

"""
元组中至少要包含一个,否则，会被看成数学公式中的小括号，
"""

# a = (11,)
# print(a)  # (11,)
# print(type(a))  # <class 'tuple'>

"""
多个变量同时赋值：
赋值运算符左边可以是一个所有元素都为变量的元组或列表，从而一次给多个变量同时赋值
注意左右两边元素个数必须相同，否则报出ValueError
"""

# a, b = [3, 4]
# print(a, b)  # 3 4
#
# a, b = (5, 8)
# print(a, b)  # 5 8
#
# [a, b] = 1, 3
# print(a, b)  # 1 3

"""
可以在赋值运算符前面 加*号以匹配赋值运算符右边的0或多个元素。
"""

# *a, b = 1, 2, 3, 4, 5
# print(a, b)  # [1, 2, 3, 4] 5     *a = [1, 2, 3, 4]
#
# a, *b, c = 1, 2
# print(a, b, c)  # 1 [] 2

"""
交换两个变量的值
"""

# a = 5
# b = 3
# temp = a
# a = b
# b = temp
# print(a, b)  # 3 5
# 赋值运算符，的左右两边都是元组，左边的是变量的元组，右边的是表达式的元组
# 先将右边的所有表达式都计算完之后，再分别赋值给左边的所有变量，
# a = 3
# b = 4
# a, b = 4, 3
# print(a, b)  # 4 3


"""
字符串和列表一样，都是有序类型，
可以将字符串看成列表，列表很多操作对于字符串也是适用的
没有单独的字符类型，字符就只包含一个元素的字符串，例如'a'、'b'、'c'
"""

"""
内置函数str的结构方法（类str的构造方法）

""x""   "'y'"       '"y"'
"""

# print(str("12"))

"""
转义字符：
        换行：newline：光标移动到下一行开头
        回车：光标移动到本行开头
        水平制表符：键盘上的tab键，光标移动到下一组4个空格的开始处
        退格：键盘上扬的backspace键，回退一个字符
    
    换行：\n
    回车：\r
    水平制表符：\t
    退格：\b
"""

# print('abc\ndef')       # abc
#                         # def
#
# print('abc\rdef')  # def
#
# print('123456\t123\t45')  # 123456  123	45
#
# print('abc\bdef')  # abdef


"""
使用转义字符，表示在字符串中有特殊用途的字符，
    某些字符串中有特殊用途，比如：反斜杠用于转义，单引号和双引号用于字符串的便捷，因此，
    不能在字符串中直接包含这些有特殊用途的字符例如''''或者双引号
"""

# print('aaa\'cc\'')  # aaa'cc'
#
# print('abc\\aaa')  # abc\aaa
#
# print("abc\"aaa\"")  # abc"aaa"

"""
原始字符串：
如果不想让字符串中的转义字符生效，可以在字符串的前面添加r 或者 R 来展示原始字符串。
"""

# print('\tC:\\Program Files')  # 	C:\Program Files
#
# print(R'\tC:\\Program Files')  # \tC:\\Program Files

"""
原始字符串的最后一个字符不能是反斜杠，（最后两个字符都是反斜杠除外）
"""

# # print(r'helloworld\')  # SyntaxError: EOL while scanning string literal
#
# print(r'helloworld\\')  # helloworld\\
#
# # 解释器不会吧 r'what\' 看做为一个原始字符串，因为原始字符串不能以反斜杠结尾
# print(r'what\'s your name')
#
# # 解释器会吧r'what\\'看成是一个原始字符串，因为原始字符窜可以用两个反斜杠结尾
# # print(r'what\\'s your name')

"""
跨越多行的字符串
1，使用三个引号  
    在三个引号中，可以包含双引号，也可以包含双引号
    可以在三个引号中嵌套三个双引号，也可以在三个双引号中，嵌套三个单引号。
"""

# print('''我是一个
# 跨越多行的
# 字符串''')


"""
2.在每行的结尾添加一个反斜杠
在解释器中显示为一行，在代码中为换行，
"""

# print('abc\
# def\
# 嘻嘻嘻')  # abcdef嘻嘻嘻

# a = 'hello'\
#     ','\
#     'world'
# print(a)

# print('hello ' * 3)  # hello hello hello

"""
    字符串的'查操作'
当获得字符串的索引时，除了调用方法index还可以使用find。rfind，rindex
其中，子串的索引指的是子串中的第一个字符的索引

其中find和index是从左边查找，rfind和rindex是到最后一个。
当字符串中不存在指定的子串的时候，index和rindex返回valueeroor， find和rfind返回-1
"""

# a = '124578234789'
#
# print(a.index('78'))  # 4
# print(a.find('78'))  # 4
# print(a.rfind('78'))  # 9
# print(a.rindex('78'))  # 9

"""
字符串是不可变类型，列表时可变类型，元组也是不可变。
字符串没有 增 删 改   操作
"""

# a = 'hello，world'
# # a[5] = '!'  # typeerror
#
# print(a[:5] + '!' + a[6:])  # hello!world    通过切片的方式先取到前五个字符hello然后使用+连接！再取到后五个字符world

"""
两个字符进行比较时，比较的是ordinal value， 调用内置函数ord来获得指定字符的ordinal value、
与内置函数ord对应的内置函数为chr，调用内置函数chr时指定 ordinal vaule 可以得到对应的字符。
"""
# print(ord('a'))  # 97
# print(ord('b'))  # 98
# print(ord('c'))  # 99
#
# print(chr(1))  # 
# print(ord(''))

# print('a' < 'b')  # True
#
# a = b = 'hello'
# c = 'hello'

# print(a == b)  # True
# print(a == c)  # True
# print(a is b)  # True
# print(a is c)  # True

"""
    字符串常量会被缓存和重用。
"""
# print(id(a))  # 4367235440
# print(id(c))  # 4367235440
#
# a = b = 1
# a = 1
# print(a == c)
#
# print(id(a))  # 4365998384
# print(id(c))  # 4367235440

"""
    字符串的翻转：
因为字符串是不可变类型所以要想让字符串翻转要使用不改变字符串本身的reversed，而不是使用改变裂变本身的reverse
"""
# a = '12345'
#
# b = reversed(a)
# print(b)  # <reversed object at 0x1080f8fd0>
# print(list(b))  # ['5', '4', '3', '2', '1']
# print(a)  # 12345

"""
    字符串的排序
和字符串的翻转一样，不可以使用sort，只可以使用sroted，因为sort是改变数据结构，而sorted不改变数据结构
"""

# a = 'DBeFac'
# print(sorted(a))  # ['B', 'D', 'F', 'a', 'c', 'e']
#
# print(sorted(a, reverse=True))  # ['e', 'c', 'a', 'F', 'D', 'B']
#
# print((sorted(a, key=str.lower)))  # ['a', 'B', 'c', 'D', 'e', 'F']

"""
调用内置函数sorted时的参数key同样适用于列表和元组

调用列表的方法sort时，也可以指定key
"""
# a = ['Python', 'java', 'Swift']
#
# print(sorted(a, key=len))  # ['java', 'Swift', 'Python']     len 根据字符长度来排序，
# print(sorted(a, key=str.lower))  # ['java', 'Python', 'Swift']

# a = ['Python', 'java', 'Swift']
#
# a.sort(key=len)
# print(a)  # ['java', 'Swift', 'Python']
# a.sort(key=str.lower)
# print(a)  # ['java', 'Python', 'Swift']   PS: 只有列表内为字符串的时候可以使用

"""
格式化字符串
    按照一定格式输出的字符串
    例1：'2021-05-21 13:14:21'就是格式化字符串
    例2：想要通过计算获得一个结果，想用一个有个事的字符串进行输出，格式为"计算结果为：xxxx"
    
    如果想要得到格式化字符串，常见的方式有三种：
    1.使用%作为占位符： 
    %s ：字符串
    %i或%d：整数
    %f：浮点数
    2.使用{}作为占位符
    3.使用$作为占位符
    
占位符 = 站住一个位置的符号，在定义一个格式化字符串时，可以使用占位符先站住某些固定位置，等访问字符串时，再将占位符替换成实际值
'%Y-%m-%d %H:%M:%S'     给出的实际值为年月日时分秒
"""

# from datetime import datetime
#
# datetime(2018, 8, 18, 18, 18, 18)
# print(datetime(2018, 8, 18, 18, 18, 18).strftime('%Y-%m-%d %H:%M:%S'))


# a = 'hahaha'
# b = '嘻嘻嘻'
# print('小明说了句： %s, ' "小刚说了句： %s" % (a, b))

"""
如果定义的格式化字符串中的% 是一个普通字符，需要使用%%对其进行转义
占位符%中也可以指定宽度，   数字和字符串都是右对齐
占位符%也可以指定精度。
"""

# print('我得工作已经完成了%d%%' % 80)  # 我得工作已经完成了80%
#
# print('%10d' % 100)  #        100
#
# print('%10s' % '100')  #       100
#
# print('%.2f' % 10)  # 10.00
#
# print('%.3f' % 3.1415926)  # 3.142
#
# print('%.5s' % 'hello，world')  # hello
#
# print('%8.3f' % 3.1415926)  #    3.142          同时指定宽度为8精确到小数点后三位。

"""
占位符{}中可以指定位置参数，0表示方法format中的第一个参数，1表示方法format的第二个参数.......
也可以在方法format中指定关键字参数的名称和值，在占位符{}中指定关键字参数的名称。
    占位符{}中可以使用冒号指定整数的表示形式, 位置参数或关键字参数的名称放在冒号前面。
"""

# book = '《金瓶梅》'
# price = 199
#
# print('买了一本书，花了{}元, 名为：{}'.format(price, book))
#
# print('买了一本书{1}，花了{0}元，只花了{0}元！'.format(price, book))  # 买了一本书《金瓶梅》，花了199元，只花了199元！
# print('买了一本书{b}，花了{p}元，只花了{p}元！'.format(p=price, b=book))  # 买了一本书《金瓶梅》，花了199元，只花了199元！
#
# print('{:b}'.format(58))  # 111010    :b二进制
# print('{:d}'.format(58))  # 58      :d十进制
# print('{:x}'.format(58))  # 3a      :x十六进制 a小写
# print('{:X}'.format(58))  # 3A      :X十六进制 a大写
# print('{:f}'.format(58))  # 58.000000   :f浮点数
# print('{:.2f}'.format(58))  # 58.00     :.2f精确到小数点后两位
#
# # 使用逗号作为千位分隔符
# print('{:,}.'.format(12345678))  # 12,345,678.
# print('{:,.2f}.'.format(12345678))
#
# print('{1:b}'.format(11, 22))  # 10110    {}内1位元组中第二个元素
# print('{a:b}'.format(a=11, b=22))  # 1011
#
# print('{:10.2f}'.format(3.1415926))  #       3.14
# print('{:10d}'.format(123))  #        123              整数为右对齐
# print('{:10s}'.format('hello'))  # hello                字符串为左对齐
# print('{:.3}'.format(3.1415926))  # 3.14
#
# from datetime import datetime
# print('{:%Y-%m-%d %H:%M:%S}'.format(datetime(2021, 6, 12, 12, 59, 00)))  # 2021-06-12 12:59:00
#
# print(format(18, 'b'))  # 10010
# print(format(18, 'f'))  # 18.000000
# print(format(3.1415926, '10.2f'))  #       3.14
# print(format('3.1415926', '10.4s'))     # 3.14

"""
美元符作为占位符，可以使用string模块中的Template类b并使用美元符作为占位符，从而得到格式化字符串。
"""
# from string import Template

# price = 99.98
# book = '《金瓶梅》'
# a = Template('买了一次本书$b,花了$p')
# #
# # c = a.substitute(p=price, b=book)
# # c = a.substitute({'p': price, 'b': book})       # 买了一次本书《金瓶梅》,花了99.98
# # print(c)  # 买了一次本书《金瓶梅》,花了99.98
# c = a.safe_substitute(p=price)
# print(c)

"""
"""
# a = '"txId": "339436155542139718",\
# "txId": "3394361555421397174",\
# "txId": "3394361555421397165",\
# "txId": "3394361555421397145",\
# "txId": "3394361555421397141",\
# "txId": "3394361555421397132",\
# "txId": "3394361555421397129",\
# "txId": "3394361555421397255",\
# "txId": "3394361555421397284",\
# "txId": "3394361555421397279",'
#
# print(list(a.split('"txId": ')))

"""
字符串的大小写转换
1.upper         把所有字符全部转换为大写
2.lower         把所有字符全部转换为小写
3.swapcase      把所有小写字符串转换为大写，所有大写字符转换为小写
4.capitalize    把第一个字符转换为大写，其余字符转换为小写
5.title         把每个单词的第一个字符转换为大写，剩余字符串转换为小写
"""
# a = 'hello world'
# print(a.upper())  # HELLO WORLD
# print(a.lower())  # hello world
# print(a.swapcase())  # HELLO WORLD
# print(a.capitalize())  # Hello world
# print(a.title())  # Hello World

"""
判断字符大小写
1.isupper   判断所有字符全部为大写
2.islower   判断所有字符全部为小写
3.istitle   判断第一个字符为大写,剩余字符串为小写
"""
# print(a.isupper())  # False
# print(a.upper().isupper())  # True
#
# print(a.islower())  # True
# print(a.lower().islower())  # True
#
# print(a.istitle())  # False
# print(a.title().istitle())  # True

"""
字符串的对齐
1、center：中心对齐
2、ljust：左对齐
3、rjust：右对齐
123 三种方法都可以接收两个参数，
第一个参数指定字符串的宽度   如果指定的宽度小于等于字符串的长度 ，则返回字符串的本身
第二个参数指定填充字符，且第二个参数是可选的，其默认值是空格
"""

# print('hello，world'.center(18, "*"))  # ***hello，world****
# print('hello，world'.center(18))  #   hello，world
# print('hello,world'.center(8))  # hello,world
#
# print('hello,world'.ljust(18))  # hello,world
# print('hello,world'.ljust(18, '*'))  # hello,world*******
# print('hello,world'.ljust(8))  # hello,world
#
# print('hello,world'.rjust(18))  #        hello,world
# print('hello,world'.rjust(18, '*'))  # *******hello,world
# print('hello,world'.rjust(8))  # hello,world

# zfill：右对齐，左边用0填充。    指定一个字符串的宽度   如果指定的宽度小于等于字符串的长度 ，则返回字符串的本身

# print('1234'.zfill(18))  # 000000000000001234
# print('-123'.zfill(18))  # -00000000000000123
#
# print('1234'.zfill(4))  # 1234
# print('-1234'.zfill(5))  # -1234

"""
字符串的子串替换
如果想将字符串中的某个子串替换为指定的字符串，可以调用方法replace、
该方法的第一个参数用于指定被替换的子串，第二个参数用于指定替换子串的字符串
该方法返回替换后得到的字符串，替换前的字符串不发生变化，
"""

# a = 'hello，hello，hello'
# print(a.replace('hello', 'hi'))  # hi，hi，hi
# print(a.replace('hello', 'hi', 1))  # hi，hello，hello    第三个参数指的是最大替换次数

"""
字符串的字符转换
如果想对字符串中的某些字符，进行转换，可以调用方法，maketrans和translate
首先调用方法maketrans创建一个转换表，然后把创建的转换表作为参数传给方法translate
"""

# a = str.maketrans('bcd', '234')
# # a = str.maketrans({98: 50, 99: 51, 100: 52})  # {98: 50, 99: 51, 100: 52}
# # a = str.maketrans({'b': '2', 'c': '3', 'd': "4"})  # {98: '2', 99: '3', 100: '4'}
# print(a)  # {98: 50, 99: 51, 100: 52}
#
# print(ord('b'))  # 98
# print(ord('2'))  # 50
#
# print(ord('c'))  # 99
# print(ord('3'))  # 51
#
# print(ord('d'))  # 100
# print(ord('4'))  # 52
#
# b = 'incredible'
# print(b.translate(a))  # in3re4i2le     a的值替换b里面对应的值

"""
在调用方法maketrans创建表转换的时候， 还可以指定删除的所有字符
在 Python 中，有一个特殊的常量 None（N 必须大写）。和 False 不同，它不表示 0，也不表示空字符串，而表示没有值，也就是空值。
"""

# a = str.maketrans('bcd', '234', 'ie')
# print(a)  # {98: 50, 99: 51, 100: 52, 105: None, 101: None}  其中 i=105  e=101
# b = 'incredible'
# print(b.translate(a))  # n3r42l
#
# # 不转换，只指定要删除的所有字符
# a = str.maketrans('', '', 'ie')
# print(a)  # {105: None, 101: None}
#
# print(b.translate(a))  # ncrdbl

"""
字符串的劈分和合并
调用方法split或rsplit劈分字符串
方法split从字符串左边开始，rsplit是右边开始
  默认劈分的是空格字符串
  这两个方法的返回值都是一个列表。
"""
# a = 'hello   world   hi   world'
# print(a.split())  # ['hello', 'world', 'hi', 'world']
# print(a.rsplit())  # ['hello', 'world', 'hi', 'world']

"""
使用sep指定劈分字符串的劈分符
"""
# a = 'hello|world|hi|world'
# print(a.split(sep='|'))  # ['hello', 'world', 'hi', 'world']
# print(a.rsplit(sep='|'))  # ['hello', 'world', 'hi', 'world']

"""
使用参数maxsplit指定劈分字符串时的最大劈分次数，在领过最大次劈分后，剩余的子串会单独作为一部分
此事方法split和rsplit就有区别了
"""

# a = 'python Swift kotlin java'
# print(a.split(maxsplit=2))  # ['python', 'Swift', 'kotlin java']
# print(a.rsplit(maxsplit=2))  # ['python Swift', 'kotlin', 'java']

"""
调用方法partition或rpartition劈分字符串   必须指定劈分符
partition从左边开始劈分    在指定的劈分符第一次出现的地方，将字符串劈分为三部分
rpartition从右面开始劈分   在指定的劈分符最后一次出现的地方，将字符串劈分为三部分
1、劈分符前面的部分
2、劈分符
3、劈分符后面的部分
    返回的是一个元组
"""

# a = 'hello-world-!'
# print(a.partition('-'))  # ('hello', '-', 'world-!')
# print(a.rpartition('-'))  # ('hello-world', '-', '!')
#
# a = 'helloworld-'
# print(a.partition('-'))  # ('helloworld', '-', '')
# print(a.rpartition('-'))  # ('helloworld', '-', '')
#
# a = 'hello world'
# print(a.partition('-'))  # ('hello world', '', '')
# print(a.rpartition('-'))   # ('', '', 'hello world')

"""
合并多个字符串，调用方法join
"""
#
# a = '|'.join(['python', 'swift', 'kotlin'])
# print(a)  # python|swift|kotlin
# a = '|'.join(('python', 'swift', 'kotlin'))
# print(a)  # python|swift|kotlin
#
# a = ''.join(('python', 'swift', 'kotlin'))
# print(a)  # pythonswiftkotlin

# 可以把字符串看做字符的列表
# a = '|'.join('python')
# print(a)  # p|y|t|h|o|n

"""
is相关的字符串方法
1、isidentifier  判断指定的字符串是否是合法的标识符
"""

# print('abc'.isidentifier())  # True
# print('123'.isidentifier())  # False

"""
调用模块keyword中的方法iskeyword来判断这个字符串是否是关键字
"""

# import keyword
#
# print(keyword.iskeyword('if'))  # True
# print(keyword.iskeyword('iF'))  # False

"""
2.isspace 判断指定字符串是否全部由空白字符组成
"""

# print('\n   \r   \t'.isspace())  # True
# print('a  c'.isspace())  # False

"""
3.isalpha  判断字指定符串是否全部由字母组成
4.isdecimal 判断指定字符串是否全部由十进制的数字组成。
5.isnumeric 判断指定字符串是否全部由数字组成
6.isalnum 判断指定字符串是否全部由字母和数字组成
"""

# print('abc'.isalpha())  # True
# print('abc1'.isalpha())  # False
# print('123'.isdecimal())  # True
# print('123六VI'.isdecimal())  # False
# print('123六Ⅵ'.isnumeric())  # True
# print('123六Ⅵa'.isnumeric())  # False
# print('123六Ⅵa'.isalnum())  # True
# print('123六Ⅵa!'.isalnum())  # False

"""
去除字符串的前导字符串和后续字符串调用方法
1、lstrip：去除字符串的前导字符串
2、rstrip:去除字符串的后续字符串
3、strip：去除字符串的前导字符串和后续字符串调
默认去除空格字符串
"""

# a = '    123,1231241209,123124     '
# print(a.lstrip())  # 123,1231241209,123124
# print(a.strip())  # 123,1231241209,123124
# print(a.rstrip())  #     123,1231241209,123124

"""
前导字符串：从左边第一个字符开始依次往后，直到某个字符串不在指定的字符串中
后续字符串：从右边开始第一个字符开始一次往前，直到某个字符不在指定的字符串中
"""

# a = 'www.baidu.com'
# print(a.lstrip('cmow.'))  # baidu.com
# print(a.rstrip('cmow.'))  # www.baidu
# print(a.strip('cmow.'))  # baidu

"""
字典：
为什么需要字典
"""

# names = ['张三', '李四', '王五', '赵六']
# mobile = ['13333333333', '14444444444', '15555555555', '16666666666']
"""
如果想要找到某人的电话号码
先取到names的索引。
然后到mobile里面根据索引取到对应的电话号码
"""
# print(mobile[names.index('张三')])  # 13333333333

"""
    姓名和电话号码存储在一个数据结构中，指定姓名后直接得到对应的电话号码
"""

# a = {'张三': '13333333333', '李四': '14444444444', '王五': '15555555555', '赵六': '16666666666'}

# print(a['王五'])  # 15555555555

"""
字典的实现原理：
    和查字典类似。当我们在字典中查找某个字时，
    一种办法是从第一也开始往后翻，直到找到我们要查找的字为止，这种办法就是在列表中查找元素的办法，缺点：字典中的字数越多，效率越低
    第二种办法现在字典的索引表里（比如说部首表）超照这个字对应的页码，然后直接翻到这个字对应的页。优点：查找效率不会随着字典中字数的增加而降低
    无论查找哪个字，查找速度都非常快
字典的特点
    1.字典中所有元素都是key ： value  通过key 对应value   。字典中的key不可重复，value可以重复
    2.字典中的元素是无序的，顺序不重要，重要而是key和value的映射关系
    3.字典中的key是不可变对象，存取字典中的key-value对时，系统会调用内置函数hash根据指定的key计算出value的储存位置，也就是哈希值，对于指定的
    key，为了保证每次计算出的哈希值都是相同的，要求key必须是不可变对象，只有不可变对象才存在哈希值
    4.字典可以根据需要，动态伸缩
    系统会根据需要动态的分配和回收内存，因此在使用前无须预先声明字典的容量
    5.字典会浪费较大的内存，于列表相比，就是空间换取了时间
"""

"""
创建字典的方式
调用内置函数dict
"""

# print(dict({'name': 'dongdong', 'age': 18}))  # {'name': 'dongdong', 'age': 18}
# print(dict(name='dongdong', age=18))  # {'name': 'dongdong', 'age': 18}
# print(dict())  # {}
# print(dict([('name', 'dongdong'), ('age', 18)]))  # {'name': 'dongdong', 'age': 18}
# print(dict(zip(range(3), 'ABC')))  # {0: 'A', 1: 'B', 2: 'C'}   zip 用于将多个可迭代的对象进行打包压缩

"""
调用类dict方法fromKeys
调用方法fromKeys时，通过参数指定所有的key，所有的value值都为None
"""

# print(dict.fromkeys(['name', 'age']))  # {'name': None, 'age': None}
# print(dict.fromkeys(('name', 'age')))  # {'name': None, 'age': None}

"""
调用方法fromkeys时可以通过参数指定所有的value值
"""

# print(dict.fromkeys(['name', 'age'], ('hello', 'hi')))  # {'name': ('hello', 'hi'), 'age': ('hello', 'hi')}

"""
字典   查操作
1.使用中括号{}
2.调用方法get    如果方法中不包括指定的key，不报出KeyError，而是返回None
可以通过参数来设置默认的value，以便在字典中不存在指定的key值将其返回
"""

# a = {'name': 'DongDong', 'age': 18}
# print(a['name'])  # DongDong
#
# print(a.get('name'))  # DongDong
# print(a.get('hello'))  # None
# print(a.get('hello', 'hi'))  # hi

"""
可以使用运算符in来检查字典中是否存在指定的key & 使用not in 来检查字典中是否不存在指定的key
"""
# print('age' in a)  # True
# print('age' not in a)  # False

"""
字典的改操作
修改字典中指定的key对应的value
1.为已经存在的key赋予一个新的value值(一次只能修改一个key对应的value)
2.调用方法update（一次至少修改一个key对应的value）

"""

# a = {'name': 'jack', 'age': 18, 'gender': '男'}
#
# a['age'] = 20
# print(a)  # {'name': 'jack', 'age': 20, 'gender': '男'}
#
# a.update({'name': 'liu', 'age': 99})
# print(a)  # {'name': 'liu', 'age': 99, 'gender': '男'}
# a.update([('name', 'wang'), ('age', 21)])
# print(a)  # {'name': 'wang', 'age': 21, 'gender': '男'}
# a.update(name='z', age=10)
# print(a)  # {'name': 'z', 'age': 10, 'gender': '男'}

"""
字典中的增操作
增加的key不能是字典中存在的key
1.为不存在的key赋予一个value值   一次添加一个key-value对
2.调用方法update    一次至少增加一个key-value对
"""

# a = {'name': 'jack', 'age': 18, 'gender': '男'}
# a['class'] = 1
# print(a)  # {'name': 'jack', 'age': 18, 'gender': '男', 'class': 1}
#
# a.update({'score': 90, 'class': 1})
# print(a)  # {'name': 'jack', 'age': 18, 'gender': '男', 'class': 1, 'score': 90}
# a.update([('aaa', 'bbb'), ('ccc', 'ddd')])
# print(a)  # {'name': 'jack', 'age': 18, 'gender': '男', 'class': 1, 'score': 90, 'aaa': 'bbb', 'ccc': 'ddd'}
# a.update(aaac=1, bbbc=2)
# print(a)  # {'name': 'jack', 'age': 18, 'gender': '男', 'class': 1, 'score': 90, 'aaa': 'bbb', 'ccc': 'ddd',
# 'aaac': 1, 'bbbc': 2}

"""
字典的删除操作
调用方法pop用来返回指定key对应的value值-----一次只删除一个key-value对 
使用del语句删除key-value对-----一次只删除一个key-value对  
调用方法popitem来删除key-value对--该方法返回被删除的key-value对--一次删除任意一个key-value对 
调用方法clear清空字典 
"""
# a = {'name': 'jack', 'age': 18, 'gender': '男'}
# print(a.pop('name'))  # jack
# print(a)  # {'age': 18, 'gender': '男'}
#
# a = {'name': 'jack', 'age': 18, 'gender': '男'}
# del a['age']
# print(a)  # {'name': 'jack', 'gender': '男'}
#
# a = {'name': 'jack', 'age': 18, 'gender': '男'}
# print(a.popitem())  # ('gender', '男')
# print(a)  # {'name': 'jack', 'age': 18}
#
# a = {'name': 'jack', 'age': 18, 'gender': '男'}
# a.clear()
# print(a)  # print(a)

"""
为字典中的key设置默认的value值
为了确保字典中指定的key总是存在的，可以调用方法setdefault：
1.如果字典中存在指定的key，该方法返回指定key对应的value值，字典不发生变化
2.如果字典中不存在指定的key，该方法返回指定的默认value值，字典中增加一对key-value对,key为字典中不存在的key，value为指定的默认value值。
if ... not in 
"""

# a = {'name': 'liu'}
# print(a.setdefault('name', 'duck'))  # liu
# print(a)  # {'name': 'liu'}
# print(a.setdefault('age', 18))  # 18
# print(a)  # {'name': 'liu', 'age': 18}
# if 'name' not in a:
#     a['age'] = 18

"""
字典的视图
keys
values
items  
"""

# a = {'name': 'jack', 'age': 18, 'gender': '男'}
# print(a.keys())  # dict_keys(['name', 'age', 'gender'])
# print(list(a.keys()))  # ['name', 'age', 'gender']
# print(a.values())  # dict_values(['jack', 18, '男'])
# print(list(a.values()))  # ['jack', 18, '男']
# print(a.items())  # dict_items([('name', 'jack'), ('age', 18), ('gender', '男')])
# print(list(a.items()))  # [('name', 'jack'), ('age', 18), ('gender', '男')]

"""
视图会随着字典的变化而变化
"""

# a = {'name': 'jack', 'age': 18, 'gender': '男'}
# a.pop('name')
# print(a)  # {'age': 18, 'gender': '男'}
# print(a.items())  # dict_items([('age', 18), ('gender', '男')])
# a.update({'name': 'jack'})
# print(a)
# print(list(a.items()))  # [('age', 18), ('gender', '男'), ('name', 'jack')]

"""
借助字典创建格式化字符串

"""

# mobile = {'张三': 13333333333,
#           '李四': 14444444444,
#           '王五': 15555555555,
#           '赵六': 16666666666}
#
# print('王五的电话号码为 %s ，张三的电话号码为 %s' % (mobile['王五'], mobile['张三']))
# 不使用格式化字符串的办法
# 王五的电话号码为 15555555555 ，张三的电话号码为 13333333333

"""
当字符串中的占位符是百分号，并且占位符对应的实际值来自于某个字典的value时，可以把所有的实际值改写成为字典，勇士根绝字典的value对应的key在占位符%
的后面添加：（字典的key）。其中，字典的key挥别添加一堆对引号，因此，如果字典的key是字符串，需要去掉字典的key自带的引号。
"""

# print('张三的电话号是 %(张三)s ， 李四的电话号是 %(李四)s' % mobile)  # 张三的电话号是 13333333333 ， 李四的电话号是 14444444444

"""
使用花括号作为占位符
"""

# mobile = {'张三': 13333333333,
#           '李四': 14444444444,
#           '王五': 15555555555,
#           '赵六': 16666666666}
# print('王五的电话号码:{}, 李四的电话号码:{}'.format(mobile['王五'], mobile['李四']))  # 王五的电话号码:15555555555, 李四的电话号码:14444444444
"""
当定义的格式化字符串中的占位符是花括号，可以调用方法format_map并把该字典直接作为方法的参数，同时根据字典的value在花括号中指定对应的key：
{字典中的key}。其中字典的key会被添加一对引号，因此，如果字典的key是字符串，需要去掉字典的key自带的引号
"""
# print('张三的电话号码:{张三}, 王五的电话号码:{王五}'.format_map(mobile))  # 张三的电话号码:13333333333, 王五的电话号码:15555555555

"""
集合
除了列表[]，元组()和字典{}，集合{}也是python提供的内置数据结构之一
可以把集合看成一个没有储存value的字典，
    集合中不可以存在重复的数据
    集合中的数据是无序的
    集合中的数据可以是任何不可变的类型，多种类型的数据可以混合存储在一个集合中
    集合可以根据需要动态伸缩，系统会根据需要动态的分配回收内存
    集合会浪费较大的内存，与列表相比，是用空间换取了时间。
"""

"""
创建方式
1.使用花括号
    将创建的集合赋值给变量时，变量名不要取名为set，因为set是集合对应的类名
2.
"""

# a = {2, 3, 45, 9, 11}
# print(a)  # {2, 3, 9, 11, 45}

# a = {2, 3, 45, 9, 11, 2, 3}
# print(a)  # {2, 3, 9, 11, 45}    >重复的数据会被去掉
# 不能直接使用{}来表示一个空集合

# print(type({}))  # <class 'dict'>  字典

"""
调用内置函数set
"""

# print(set(range(1, 6)))  # {1, 2, 3, 4, 5}
# print(set([3, 5, 6, 7]))  # {3, 5, 7, 9}
# print(set((1, 3, 5, 7, 9)))  # {1, 3, 5, 7, 9}
# print(set('13579'))  # {'9', '3', '7', '5', '1'}
# print(set({1, 3, 5, 7, 9}))  # {1, 3, 5, 7, 9}
#
# print(set())  # set() 空集合
#
# print(set({2, 3, 45, 9, 11, 2, 3}))  # {2, 3, 9, 11, 45}

"""
集合的关系
如何判断两个集合是否相等
    可以使用== 和！=进行判断
"""

# a = {1, 3, 4, 6}
# b = {3, 4, 1, 6}
# print(a == b)  # True
# print(a != b)  # False

"""
判断一个集合是否是另一个集合的子集
    调用方法issubset进行判读
"""

# a = {1, 3, 5, 7, 9, 11, 13}
# b = {1, 3, 4, 6, 7, 0}
# c = {1, 3, 5, 7, 9, 11}

# print(a.issubset(b))  # False  判断a是否是b的子集
# print(c.issubset(a))  # True   判断c是否是a的子集
# print(b.issubset(c))  # False  判断b是否是c的子集

# import time      时间戳

# a = time.time()
# print("当前的时间戳为 %.f" % a)

"""
    如何判断一个集合是否是另一个集合的超集
    调用方法issuperset进行判断
"""

# print(a.issuperset(c))  # True
# print(b.issuperset(c))  # True
# print(c.issuperset(a))  # False

"""
    如何判断两个集合是否没有交集
    调用方法isdisjoint
"""

# a = {1, 3, 5, 7, 9}
# b = {2, 3, 6, 8, 10}
# c = {2, 4, 6, 8, 10}
#
# print(a.isdisjoint(b))  # False
# print(a.isdisjoint(c))  # True
# print(b.isdisjoint(c))  # False

"""
两个集合的交集
调用方法intersection来查看两个集合的交集
使用 ' & ' 也可以查看两个集合的交集
使用两个方法 集合本身不发生变化

"""

# a = {1, 3, 5, 6, 7}
# b = {1, 4, 7, 3, 9}
# print(a.intersection(b))  # {1, 3, 7}
# print(a & b)  # {1, 3, 7}
# print(a)  # {1, 3, 5, 6, 7}
# print(b)  # {1, 3, 4, 7, 9}

"""
a.intersection_update(b)的执行结果
    使用 a.intersection(b)返回值更新a，  b不变
    方法intersection_update的返回值为None
"""

# print(a.intersection_update(b))  # None
# print(a)  # {1, 3, 7}
# print(b)  # {1, 3, 4, 7, 9}

# print(b.intersection_update(a))
# print(a)  # {1, 3, 5, 6, 7}
# print(b)  # {1, 3, 7}

"""
两个集合的并集
调用方法union来查看两个集合的并集
使用 ' | ' 也可以查看两个集合的并集
不存在方法union_update
且两个集合不发生变化
"""
# a = {1, 3, 5, 6, 7}
# b = {1, 4, 7, 3, 9}
# print(a.union(b))  # {1, 3, 4, 5, 6, 7, 9}
# print(a | b)  # {1, 3, 4, 5, 6, 7, 9}
# print(a)
# print(b)


"""
两个集合的差集
调用方法difference来查看两个集合的差集
使用 ' - ' 也可以查看两个集合的交集
做差级操作后生成一个新的集合，做差级操作的两个集合不变
"""
# a = {1, 3, 5, 6, 7}
# b = {1, 4, 7, 3, 9}
# print(a.difference(b))  # {5, 6}
# print(b.difference(a))  # {9, 4}
#
# print(a - b)  # {5, 6}
# print(a)
# print(b)

"""
difference_update
a.difference_update(b)的返回值为None
a集合生成了一个新的集合
b集合不变
"""
# print(a.difference_update(b))  # None
# print(a)  # {5, 6}
# print(b)  # {1, 3, 4, 7, 9}

"""
两个集合的对称差集
两个集合的并集去除两个集合的差集为两个集合的对称差集
调用方法symmetric_difference来查看两个集合的差集
使用 ' ^ ' 也可以查看两个集合的交集
使用对称差集操作后生成一个新的集合，做对称差集的两个集合不变
"""

# a = {1, 3, 5, 6, 7}
# b = {1, 4, 7, 3, 9}
#
# print(a.symmetric_difference(b))  # {4, 5, 6, 9}
# print(a ^ b)  # {4, 5, 6, 9}
# print(a)  # {1, 3, 5, 6, 7}
# print(b)  # {1, 3, 4, 7, 9}

"""
a.symmetric_difference_update(b)的返回值为None
a集合生成了一个新的集合
b集合不变
"""
# print(a.symmetric_difference_update(b))  # None
# print(a)  # {4, 5, 6, 9}
# print(b)  # {1, 3, 4, 7, 9}

"""
集合的查操作；
可以使用运算符in检查集合中是否存在指定的元素，或者使用not in来检查集合中是否不存在指定的元素
"""

# a = {3, 4, 5, 6, 7}
# print(5 in a)  # True
# print(8 in a)  # False
#
# print(5 not in a)  # False
# print(8 not in a)  # False

"""
集合的增操作
如果想要往集合里面添加元素，常见的方式有两种；
1.调用方法add,      一次添加一个元素。如果集合内存在指定的元素，则不会被添加  
2.调用方法update:   一次至少添加一个元素。如果集合内存在指定的元素，则不会被添加  
"""

# a = {1, 2, 3, 5, 6}
# a.add(7)
# print(a)  # {1, 2, 3, 5, 6, 7}
#
# a = {1, 2, 3, 5, 6}
# a.update({4, 7})  # {1, 2, 3, 4, 5, 6, 7}
# print(a)
#
# a.update([4, 7])
# print(a)  # {1, 2, 3, 4, 5, 6, 7}
#
# a.update((4, 7))
# print(a)  # {1, 2, 3, 4, 5, 6, 7}

"""
集合的删操作
1.调用方法remove    如果想要删除的元素不存在，则报错KeyError    一次只删除一个元素
2.调用方法discard   如果想要删除的元素不存在，不会报KeyError    一次只删除一个元素
3.调用方法pop       该方法返回被删除的元素，一次只删除一个任意的元素
4.调用方法clear     该方法用来清空集合
"""

# a = {3, 4, 5, 6, 7}
# a.remove(5)
# print(a)  # {3, 4, 6, 7}
#
# a = {3, 4, 5, 6, 7}
# a.discard(5)
# print(a)  # {3, 4, 6, 7}
#
# a.discard(8)
# print(a)  # {3, 4, 6, 7}
#
# a = {3, 4, 5, 6, 7}
# print(a.pop())  # 3
# print(a)  # {4, 5, 6, 7}
#
# a = {3, 4, 5, 6, 7}
# a.clear()
# print(a)  # set()

"""
不可变集合 frozenset     
    frozenset的意思是"被冻结的set"，也就是不可变的set
    frozenset之于set就好比tuole之于list
     因为frozenset是不可变类型，所以frozenset类型的对象：
1.存在哈希值（哈希值只有在不可变类型中存在）
2.可以作为字典的key
3.可以作为set中的元素
"""

"""
frozenset对象的创建
    可以调用内置函数frozenset来创建frozenset对象
    
"""

# print(frozenset())  # frozenset()
#
# print(frozenset(range(1, 6)))  # frozenset()
#
# print(frozenset([1, 3, 5, 6]))  # frozenset()
#
# print(frozenset((1, 3, 5)))  # frozenset({1, 3, 5})
#
# print(frozenset("35926"))  # frozenset({1, 3, 5})
#
# print(frozenset({3, 5, 9, 2, 6}))  # frozenset({1, 3, 5})

# 在程序中尽量使用不可变类型的对象，一旦创建不可变类型的对象，所有数据不会被修改，就不会导致修改数据产生的错误
# 在多任务环境下，同时操作对象时，不需要加锁。

"""
流程控制的概述
任何简单或者复杂的算法，都可以由：顺序结构，选择结构和循环结构三种节本结构组合而成
顺序结构   指的是程序从上到下顺序的执行代码。中间没有任何判断和跳转，直到程序结束
选择结构   if语句          程序根据判断条件的布尔值，选择执行部分代码
循环结构   while和for      程序根据循环条件反复执行某段代码，知道不满足循环条件为止。
"""

"""
顺序结构   指的是程序从上到下顺序的执行代码。中间没有任何判断和跳转，直到程序结束

"""
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
# import platform
# import distutils.filelist

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
为指定索引的元素赋予一个新值。(一次只修改一个元素)
为指定的切片赋予一个新值。(一次至少修改一个新值)
"""

# a = [1, 2, 3, 4, 5]
# a[2] = 9
# print(a)

# 二

# a[1:3] = [99, 12]
# print(a)  # [1, 99, 12, 4, 5]
# a[0:1] = [5]
# print(a)
# a[1:4] = [1, 7]
# print(a)  # [1, 1, 7, 5]

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
使用del语句，一次至少删除一个元素。del指定索引
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

"""
比较运算符对两个列表比较
> , >= , >= , < , <= , == , !=
从第一个元素进行比较，如果相等比较下一个元素，以此类推，直到两个元素不相等。两个列表中所有元素都不被比较
"""
# a = [1, 2, 3, 4, 5]
# b = [1, 2, 3, 5, 6]
# print(a > b)  # False
#
# print([3, [2, 6]] > [3, [2, 5]])  # Ture
"""
也可以使用is进行比较  
is是同一性测试， == 是相同性测试
"""
# a = b = [1, 2, 3]
# c = [1, 2, 3]
#
# print(a == b)  # True
# print(a == c)  # True
#
# print(a is b)  # True
# print(a is c)  # False
"""
列表的翻转：
1、调用方法reverse
"""
# a = [1, 2, 3, 4, 5]
# a.reverse()
# print(a)
#
# # 2.调用内置函数reversed    返回值为迭代器对象，且被翻转的列表不发生变化。
# a = [1, 2, 3 , 4, 5]
#
# print(reversed(a))  # <list_reverseiterator object at 0x10e0ebfa0> = 列表翻转迭代器对象
# print(list(reversed(a)))  # [5, 4, 3, 2, 1]

"""
列表的排序
1，对列表中的所有元素进行排序，调用方法sort,默认按照从小到大排序.
"""

# a = [2, 4, 5, 7, 6]
# a.sort()
# print(a)  # [2, 4, 5, 6, 7]

"""
调用方法 sort时，可以指定参数reverse = Ture ，从大到小排序
"""

# a.sort(reverse=True)  # [2, 4, 5, 6, 7]
# print(a)

"""
2.调用内置函数sorted 
    内置函数sorted的返回值是排序后的新列表，且排序的列表不发生变化。
"""

# a = [2, 4, 5, 7, 6]
# print(sorted(a))  # [2, 4, 5, 6, 7]
# print(a)  # [2, 4, 5, 7, 6]

"""
2.调用内置函数sorted时，可以指定参数reverse = Ture ，从大到小排序
"""

# print(sorted(a, reverse=True))  # [7, 6, 5, 4, 2]
# print(a)  # [2, 4, 5, 7, 6]


"""
多维列表
当列表中的元素也是列表，就构成了多维列表，例如:当列表中的元素是一维列表时，就构成了二维列表，；当列表中的元素是二维列表时，
就构成了三维列表，因此，可以把多维列表看做是特殊的一维列表。

1、一维列表的操作也适用于多维列表
"""
# a = [[3, 4], [1, 5, 2], [3, 4, 5, 6]]
#
# print(a[2][3])  # 6  在列表a中索引为2 里面 索引为 3 的 元素为6
#
# a[1] = 2  # 把列表内索引为1的元素重新赋值为2
# print(a)  # [[3, 4], 2, [3, 4, 5, 6]]
#
# a.append([3, 4])  # 在列表的末尾添加一个元素
# print(a)  # [[3, 4], 2, [3, 4, 5, 6], [3, 4]]
#
# a.extend([[3, 4], [5, 6]])  # 在列表的末尾添加多个元素
# print(a)  # [[3, 4], 2, [3, 4, 5, 6], [3, 4], [3, 4], [5, 6]]
#
# a.remove([5, 6])  # 指定元素为[5, 6]的进行删除。
# print(a)  # [[3, 4], 2, [3, 4, 5, 6], [3, 4], [3, 4]]
#
# a.pop(3)  # 删除指定列表索引为3的指定元素 一次只能删除一个，如果未指定索引，默认删除最后一个元素
# print(a)  # [[3, 4], 2, [3, 4, 5, 6], [3, 4]]  pop指定的为列表的索引
#
# del a[2:3]  # 删除指定索引到结束索引内的元素
# print(a)  # [[3, 4], 2, [3, 4]]
#
# b = [[3, 4], 2, [3, 4, 5, 6], [3, 4], [3, 4], [5, 6]]
#
# del b[2:len(b)]  # 删除指定索引到列表最后的所有元素。
# print(b)  # [[3, 4], 2]
#
# b.insert(1, [[1, 2], [2, 3]])  # 在指定元素位置前，添加元素
# print(b)  # [[3, 4], [[1, 2], [2, 3]], 2]
#
# """
# 多维列表的初始化
# """
# # 一维列表初始化
# print([0] * 3)  # [0, 0, 0]
#
# # 多维列表的初始化
# print([[0] * 3] * 4)  # [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
#
# # 列表生成式
# print([0 for i in range(3)])  # [0, 0, 0]
#
# print([[0 for i in range(3)] for j in range(4)])  # [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]


# print([[[0] * 3] for i in range(4)])  # [[[0, 0, 0]], [[0, 0, 0]], [[0, 0, 0]], [[0, 0, 0]]]

"""
 元组：内置数据结构之一
元组和列表的区别:列表可以更改，列表用[]表示
              元组不可以更改，用()表示
"""
# a = ("hello", 1, True)
# print(a)  # ('hello', 1, True)
#
# a = "hello", 1, True  # 小括号是可以省略的
# print(a)  # ('hello', 1, True)

"""
空列表的表示方式：
"""

# a = (())
# print(a)  # ()
#
# a = (tuple())
# print(a)  # ()

"""
不可变类型的对象，对象内部所有数据就不能被修改了，这样就避免了由于修改数据导致的错误。此外，对于不可变类型的对象，
在多任务环境下同时操作对象时不需要加锁。因此，在程序中尽量使用不可变类型的对象。
"""

# a = ("hello", 1, True)
# # a[1] = 2
# print(a)  # TypeError: 'tuple' object does not support item assignment

# a = ("hello", [1, 2, 3], True)
# a[1][2] = 3
# print(a)  # ('hello', [1, 2, 3], True)
# 元组内的列表是可以进行更改的，因为元组储存的是元素在内存的地址，因此，地址不可以改变，地址内可以改变

"""
只包含一个元素的元组
"""

# a = (11)
# print(a)  # 11
# print(type(a))  # <class 'int'>

"""
元组中至少要包含一个,否则，会被看成数学公式中的小括号，
"""

# a = (11,)
# print(a)  # (11,)
# print(type(a))  # <class 'tuple'>

"""
多个变量同时赋值：
赋值运算符左边可以是一个所有元素都为变量的元组或列表，从而一次给多个变量同时赋值
注意左右两边元素个数必须相同，否则报出ValueError
"""

# a, b = [3, 4]
# print(a, b)  # 3 4
#
# a, b = (5, 8)
# print(a, b)  # 5 8
#
# [a, b] = 1, 3
# print(a, b)  # 1 3

"""
可以在赋值运算符前面 加*号以匹配赋值运算符右边的0或多个元素。
"""

# *a, b = 1, 2, 3, 4, 5
# print(a, b)  # [1, 2, 3, 4] 5     *a = [1, 2, 3, 4]
#
# a, *b, c = 1, 2
# print(a, b, c)  # 1 [] 2

"""
交换两个变量的值
"""

# a = 5
# b = 3
# temp = a
# a = b
# b = temp
# print(a, b)  # 3 5
# 赋值运算符，的左右两边都是元组，左边的是变量的元组，右边的是表达式的元组
# 先将右边的所有表达式都计算完之后，再分别赋值给左边的所有变量，
# a = 3
# b = 4
# a, b = 4, 3
# print(a, b)  # 4 3


"""
字符串和列表一样，都是有序类型，
可以将字符串看成列表，列表很多操作对于字符串也是适用的
没有单独的字符类型，字符就只包含一个元素的字符串，例如'a'、'b'、'c'
"""

"""
内置函数str的结构方法（类str的构造方法）

""x""   "'y'"       '"y"'
"""

# print(str("12"))

"""
转义字符：
        换行：newline：光标移动到下一行开头
        回车：光标移动到本行开头
        水平制表符：键盘上的tab键，光标移动到下一组4个空格的开始处
        退格：键盘上扬的backspace键，回退一个字符

    换行：\n
    回车：\r
    水平制表符：\t
    退格：\b
"""

# print('abc\ndef')       # abc
#                         # def
#
# print('abc\rdef')  # def
#
# print('123456\t123\t45')  # 123456  123	45
#
# print('abc\bdef')  # abdef


"""
使用转义字符，表示在字符串中有特殊用途的字符，
    某些字符串中有特殊用途，比如：反斜杠用于转义，单引号和双引号用于字符串的便捷，因此，
    不能在字符串中直接包含这些有特殊用途的字符例如''''或者双引号
"""

# print('aaa\'cc\'')  # aaa'cc'
#
# print('abc\\aaa')  # abc\aaa
#
# print("abc\"aaa\"")  # abc"aaa"

"""
原始字符串：
如果不想让字符串中的转义字符生效，可以在字符串的前面添加r 或者 R 来展示原始字符串。
"""

# print('\tC:\\Program Files')  # 	C:\Program Files
#
# print(R'\tC:\\Program Files')  # \tC:\\Program Files

"""
原始字符串的最后一个字符不能是反斜杠，（最后两个字符都是反斜杠除外）
"""

# # print(r'helloworld\')  # SyntaxError: EOL while scanning string literal
#
# print(r'helloworld\\')  # helloworld\\
#
# # 解释器不会吧 r'what\' 看做为一个原始字符串，因为原始字符串不能以反斜杠结尾
# print(r'what\'s your name')
#
# # 解释器会吧r'what\\'看成是一个原始字符串，因为原始字符窜可以用两个反斜杠结尾
# # print(r'what\\'s your name')

"""
跨越多行的字符串
1，使用三个引号  
    在三个引号中，可以包含双引号，也可以包含双引号
    可以在三个引号中嵌套三个双引号，也可以在三个双引号中，嵌套三个单引号。
"""

# print('''我是一个
# 跨越多行的
# 字符串''')


"""
2.在每行的结尾添加一个反斜杠
在解释器中显示为一行，在代码中为换行，
"""

# print('abc\
# def\
# 嘻嘻嘻')  # abcdef嘻嘻嘻

# a = 'hello'\
#     ','\
#     'world'
# print(a)

# print('hello ' * 3)  # hello hello hello

"""
    字符串的'查操作'
当获得字符串的索引时，除了调用方法index还可以使用find。rfind，rindex
其中，子串的索引指的是子串中的第一个字符的索引

其中find和index是从左边查找，rfind和rindex是到最后一个。
当字符串中不存在指定的子串的时候，index和rindex返回valueeroor， find和rfind返回-1
"""

# a = '124578234789'
#
# print(a.index('78'))  # 4
# print(a.find('78'))  # 4
# print(a.rfind('78'))  # 9
# print(a.rindex('78'))  # 9

"""
字符串是不可变类型，列表时可变类型，元组也是不可变。
字符串没有 增 删 改   操作
"""

# a = 'hello，world'
# # a[5] = '!'  # typeerror
#
# print(a[:5] + '!' + a[6:])  # hello!world    通过切片的方式先取到前五个字符hello然后使用+连接！再取到后五个字符world

"""
两个字符进行比较时，比较的是ordinal value， 调用内置函数ord来获得指定字符的ordinal value、
与内置函数ord对应的内置函数为chr，调用内置函数chr时指定 ordinal vaule 可以得到对应的字符。
"""
# print(ord('a'))  # 97
# print(ord('b'))  # 98
# print(ord('c'))  # 99
#
# print(chr(1))  # 
# print(ord(''))

# print('a' < 'b')  # True
#
# a = b = 'hello'
# c = 'hello'

# print(a == b)  # True
# print(a == c)  # True
# print(a is b)  # True
# print(a is c)  # True

"""
    字符串常量会被缓存和重用。
"""
# print(id(a))  # 4367235440
# print(id(c))  # 4367235440
#
# a = b = 1
# a = 1
# print(a == c)
#
# print(id(a))  # 4365998384
# print(id(c))  # 4367235440

"""
    字符串的翻转：
因为字符串是不可变类型所以要想让字符串翻转要使用不改变字符串本身的reversed，而不是使用改变裂变本身的reverse
"""
# a = '12345'
#
# b = reversed(a)
# print(b)  # <reversed object at 0x1080f8fd0>
# print(list(b))  # ['5', '4', '3', '2', '1']
# print(a)  # 12345

"""
    字符串的排序
和字符串的翻转一样，不可以使用sort，只可以使用sroted，因为sort是改变数据结构，而sorted不改变数据结构
"""

# a = 'DBeFac'
# print(sorted(a))  # ['B', 'D', 'F', 'a', 'c', 'e']
#
# print(sorted(a, reverse=True))  # ['e', 'c', 'a', 'F', 'D', 'B']
#
# print((sorted(a, key=str.lower)))  # ['a', 'B', 'c', 'D', 'e', 'F']

"""
调用内置函数sorted时的参数key同样适用于列表和元组

调用列表的方法sort时，也可以指定key
"""
# a = ['Python', 'java', 'Swift']
#
# print(sorted(a, key=len))  # ['java', 'Swift', 'Python']     len 根据字符长度来排序，
# print(sorted(a, key=str.lower))  # ['java', 'Python', 'Swift']

# a = ['Python', 'java', 'Swift']
#
# a.sort(key=len)
# print(a)  # ['java', 'Swift', 'Python']
# a.sort(key=str.lower)
# print(a)  # ['java', 'Python', 'Swift']   PS: 只有列表内为字符串的时候可以使用

"""
格式化字符串
    按照一定格式输出的字符串
    例1：'2021-05-21 13:14:21'就是格式化字符串
    例2：想要通过计算获得一个结果，想用一个有个事的字符串进行输出，格式为"计算结果为：xxxx"

    如果想要得到格式化字符串，常见的方式有三种：
    1.使用%作为占位符： 
    %s ：字符串
    %i或%d：整数
    %f：浮点数
    2.使用{}作为占位符
    3.使用$作为占位符

占位符 = 站住一个位置的符号，在定义一个格式化字符串时，可以使用占位符先站住某些固定位置，等访问字符串时，再将占位符替换成实际值
'%Y-%m-%d %H:%M:%S'     给出的实际值为年月日时分秒
"""

# from datetime import datetime
#
# datetime(2018, 8, 18, 18, 18, 18)
# print(datetime(2018, 8, 18, 18, 18, 18).strftime('%Y-%m-%d %H:%M:%S'))


# a = 'hahaha'
# b = '嘻嘻嘻'
# print('小明说了句： %s, ' "小刚说了句： %s" % (a, b))

"""
如果定义的格式化字符串中的% 是一个普通字符，需要使用%%对其进行转义
占位符%中也可以指定宽度，   数字和字符串都是右对齐
占位符%也可以指定精度。
"""

# print('我得工作已经完成了%d%%' % 80)  # 我得工作已经完成了80%
#
# print('%10d' % 100)  #        100
#
# print('%10s' % '100')  #       100
#
# print('%.2f' % 10)  # 10.00
#
# print('%.3f' % 3.1415926)  # 3.142
#
# print('%.5s' % 'hello，world')  # hello
#
# print('%8.3f' % 3.1415926)  #    3.142          同时指定宽度为8精确到小数点后三位。

"""
占位符{}中可以指定位置参数，0表示方法format中的第一个参数，1表示方法format的第二个参数.......
也可以在方法format中指定关键字参数的名称和值，在占位符{}中指定关键字参数的名称。
    占位符{}中可以使用冒号指定整数的表示形式, 位置参数或关键字参数的名称放在冒号前面。
"""

# book = '《金瓶梅》'
# price = 199
#
# print('买了一本书，花了{}元, 名为：{}'.format(price, book))
#
# print('买了一本书{1}，花了{0}元，只花了{0}元！'.format(price, book))  # 买了一本书《金瓶梅》，花了199元，只花了199元！
# print('买了一本书{b}，花了{p}元，只花了{p}元！'.format(p=price, b=book))  # 买了一本书《金瓶梅》，花了199元，只花了199元！
#
# print('{:b}'.format(58))  # 111010    :b二进制
# print('{:d}'.format(58))  # 58      :d十进制
# print('{:x}'.format(58))  # 3a      :x十六进制 a小写
# print('{:X}'.format(58))  # 3A      :X十六进制 a大写
# print('{:f}'.format(58))  # 58.000000   :f浮点数
# print('{:.2f}'.format(58))  # 58.00     :.2f精确到小数点后两位
#
# # 使用逗号作为千位分隔符
# print('{:,}.'.format(12345678))  # 12,345,678.
# print('{:,.2f}.'.format(12345678))
#
# print('{1:b}'.format(11, 22))  # 10110    {}内1位元组中第二个元素
# print('{a:b}'.format(a=11, b=22))  # 1011
#
# print('{:10.2f}'.format(3.1415926))  #       3.14
# print('{:10d}'.format(123))  #        123              整数为右对齐
# print('{:10s}'.format('hello'))  # hello                字符串为左对齐
# print('{:.3}'.format(3.1415926))  # 3.14
#
# from datetime import datetime
# print('{:%Y-%m-%d %H:%M:%S}'.format(datetime(2021, 6, 12, 12, 59, 00)))  # 2021-06-12 12:59:00
#
# print(format(18, 'b'))  # 10010
# print(format(18, 'f'))  # 18.000000
# print(format(3.1415926, '10.2f'))  #       3.14
# print(format('3.1415926', '10.4s'))     # 3.14

"""
美元符作为占位符，可以使用string模块中的Template类b并使用美元符作为占位符，从而得到格式化字符串。
"""
# from string import Template

# price = 99.98
# book = '《金瓶梅》'
# a = Template('买了一次本书$b,花了$p')
# #
# # c = a.substitute(p=price, b=book)
# # c = a.substitute({'p': price, 'b': book})       # 买了一次本书《金瓶梅》,花了99.98
# # print(c)  # 买了一次本书《金瓶梅》,花了99.98
# c = a.safe_substitute(p=price)
# print(c)

"""
"""
# a = '"txId": "339436155542139718",\
# "txId": "3394361555421397174",\
# "txId": "3394361555421397165",\
# "txId": "3394361555421397145",\
# "txId": "3394361555421397141",\
# "txId": "3394361555421397132",\
# "txId": "3394361555421397129",\
# "txId": "3394361555421397255",\
# "txId": "3394361555421397284",\
# "txId": "3394361555421397279",'
#
# print(list(a.split('"txId": ')))

"""
字符串的大小写转换
1.upper         把所有字符全部转换为大写
2.lower         把所有字符全部转换为小写
3.swapcase      把所有小写字符串转换为大写，所有大写字符转换为小写
4.capitalize    把第一个字符转换为大写，其余字符转换为小写
5.title         把每个单词的第一个字符转换为大写，剩余字符串转换为小写
"""
# a = 'hello world'
# print(a.upper())  # HELLO WORLD
# print(a.lower())  # hello world
# print(a.swapcase())  # HELLO WORLD
# print(a.capitalize())  # Hello world
# print(a.title())  # Hello World

"""
判断字符大小写
1.isupper   判断所有字符全部为大写
2.islower   判断所有字符全部为小写
3.istitle   判断第一个字符为大写,剩余字符串为小写
"""
# print(a.isupper())  # False
# print(a.upper().isupper())  # True
#
# print(a.islower())  # True
# print(a.lower().islower())  # True
#
# print(a.istitle())  # False
# print(a.title().istitle())  # True

"""
字符串的对齐
1、center：中心对齐
2、ljust：左对齐
3、rjust：右对齐
123 三种方法都可以接收两个参数，
第一个参数指定字符串的宽度   如果指定的宽度小于等于字符串的长度 ，则返回字符串的本身
第二个参数指定填充字符，且第二个参数是可选的，其默认值是空格
"""

# print('hello，world'.center(18, "*"))  # ***hello，world****
# print('hello，world'.center(18))  #   hello，world
# print('hello,world'.center(8))  # hello,world
#
# print('hello,world'.ljust(18))  # hello,world
# print('hello,world'.ljust(18, '*'))  # hello,world*******
# print('hello,world'.ljust(8))  # hello,world
#
# print('hello,world'.rjust(18))  #        hello,world
# print('hello,world'.rjust(18, '*'))  # *******hello,world
# print('hello,world'.rjust(8))  # hello,world

# zfill：右对齐，左边用0填充。    指定一个字符串的宽度   如果指定的宽度小于等于字符串的长度 ，则返回字符串的本身

# print('1234'.zfill(18))  # 000000000000001234
# print('-123'.zfill(18))  # -00000000000000123
#
# print('1234'.zfill(4))  # 1234
# print('-1234'.zfill(5))  # -1234

"""
字符串的子串替换
如果想将字符串中的某个子串替换为指定的字符串，可以调用方法replace、
该方法的第一个参数用于指定被替换的子串，第二个参数用于指定替换子串的字符串
该方法返回替换后得到的字符串，替换前的字符串不发生变化，
"""

# a = 'hello，hello，hello'
# print(a.replace('hello', 'hi'))  # hi，hi，hi
# print(a.replace('hello', 'hi', 1))  # hi，hello，hello    第三个参数指的是最大替换次数

"""
字符串的字符转换
如果想对字符串中的某些字符，进行转换，可以调用方法，maketrans和translate
首先调用方法maketrans创建一个转换表，然后把创建的转换表作为参数传给方法translate
"""

# a = str.maketrans('bcd', '234')
# # a = str.maketrans({98: 50, 99: 51, 100: 52})  # {98: 50, 99: 51, 100: 52}
# # a = str.maketrans({'b': '2', 'c': '3', 'd': "4"})  # {98: '2', 99: '3', 100: '4'}
# print(a)  # {98: 50, 99: 51, 100: 52}
#
# print(ord('b'))  # 98
# print(ord('2'))  # 50
#
# print(ord('c'))  # 99
# print(ord('3'))  # 51
#
# print(ord('d'))  # 100
# print(ord('4'))  # 52
#
# b = 'incredible'
# print(b.translate(a))  # in3re4i2le     a的值替换b里面对应的值

"""
在调用方法maketrans创建表转换的时候， 还可以指定删除的所有字符
在 Python 中，有一个特殊的常量 None（N 必须大写）。和 False 不同，它不表示 0，也不表示空字符串，而表示没有值，也就是空值。
"""

# a = str.maketrans('bcd', '234', 'ie')
# print(a)  # {98: 50, 99: 51, 100: 52, 105: None, 101: None}  其中 i=105  e=101
# b = 'incredible'
# print(b.translate(a))  # n3r42l
#
# # 不转换，只指定要删除的所有字符
# a = str.maketrans('', '', 'ie')
# print(a)  # {105: None, 101: None}
#
# print(b.translate(a))  # ncrdbl

"""
字符串的劈分和合并
调用方法split或rsplit劈分字符串
方法split从字符串左边开始，rsplit是右边开始
  默认劈分的是空格字符串
  这两个方法的返回值都是一个列表。
"""
# a = 'hello   world   hi   world'
# print(a.split())  # ['hello', 'world', 'hi', 'world']
# print(a.rsplit())  # ['hello', 'world', 'hi', 'world']

"""
使用sep指定劈分字符串的劈分符
"""
# a = 'hello|world|hi|world'
# print(a.split(sep='|'))  # ['hello', 'world', 'hi', 'world']
# print(a.rsplit(sep='|'))  # ['hello', 'world', 'hi', 'world']

"""
使用参数maxsplit指定劈分字符串时的最大劈分次数，在领过最大次劈分后，剩余的子串会单独作为一部分
此事方法split和rsplit就有区别了
"""

# a = 'python Swift kotlin java'
# print(a.split(maxsplit=2))  # ['python', 'Swift', 'kotlin java']
# print(a.rsplit(maxsplit=2))  # ['python Swift', 'kotlin', 'java']

"""
调用方法partition或rpartition劈分字符串   必须指定劈分符
partition从左边开始劈分    在指定的劈分符第一次出现的地方，将字符串劈分为三部分
rpartition从右面开始劈分   在指定的劈分符最后一次出现的地方，将字符串劈分为三部分
1、劈分符前面的部分
2、劈分符
3、劈分符后面的部分
    返回的是一个元组
"""

# a = 'hello-world-!'
# print(a.partition('-'))  # ('hello', '-', 'world-!')
# print(a.rpartition('-'))  # ('hello-world', '-', '!')
#
# a = 'helloworld-'
# print(a.partition('-'))  # ('helloworld', '-', '')
# print(a.rpartition('-'))  # ('helloworld', '-', '')
#
# a = 'hello world'
# print(a.partition('-'))  # ('hello world', '', '')
# print(a.rpartition('-'))   # ('', '', 'hello world')

"""
合并多个字符串，调用方法join
"""
#
# a = '|'.join(['python', 'swift', 'kotlin'])
# print(a)  # python|swift|kotlin
# a = '|'.join(('python', 'swift', 'kotlin'))
# print(a)  # python|swift|kotlin
#
# a = ''.join(('python', 'swift', 'kotlin'))
# print(a)  # pythonswiftkotlin

# 可以把字符串看做字符的列表
# a = '|'.join('python')
# print(a)  # p|y|t|h|o|n

"""
is相关的字符串方法
1、isidentifier  判断指定的字符串是否是合法的标识符
"""

# print('abc'.isidentifier())  # True
# print('123'.isidentifier())  # False

"""
调用模块keyword中的方法iskeyword来判断这个字符串是否是关键字
"""

# import keyword
#
# print(keyword.iskeyword('if'))  # True
# print(keyword.iskeyword('iF'))  # False

"""
2.isspace 判断指定字符串是否全部由空白字符组成
"""

# print('\n   \r   \t'.isspace())  # True
# print('a  c'.isspace())  # False

"""
3.isalpha  判断字指定符串是否全部由字母组成
4.isdecimal 判断指定字符串是否全部由十进制的数字组成。
5.isnumeric 判断指定字符串是否全部由数字组成
6.isalnum 判断指定字符串是否全部由字母和数字组成
"""

# print('abc'.isalpha())  # True
# print('abc1'.isalpha())  # False
# print('123'.isdecimal())  # True
# print('123六VI'.isdecimal())  # False
# print('123六Ⅵ'.isnumeric())  # True
# print('123六Ⅵa'.isnumeric())  # False
# print('123六Ⅵa'.isalnum())  # True
# print('123六Ⅵa!'.isalnum())  # False

"""
去除字符串的前导字符串和后续字符串调用方法
1、lstrip：去除字符串的前导字符串
2、rstrip:去除字符串的后续字符串
3、strip：去除字符串的前导字符串和后续字符串调
默认去除空格字符串
"""

# a = '    123,1231241209,123124     '
# print(a.lstrip())  # 123,1231241209,123124
# print(a.strip())  # 123,1231241209,123124
# print(a.rstrip())  #     123,1231241209,123124

"""
前导字符串：从左边第一个字符开始依次往后，直到某个字符串不在指定的字符串中
后续字符串：从右边开始第一个字符开始一次往前，直到某个字符不在指定的字符串中
"""

# a = 'www.baidu.com'
# print(a.lstrip('cmow.'))  # baidu.com
# print(a.rstrip('cmow.'))  # www.baidu
# print(a.strip('cmow.'))  # baidu

"""
字典：
为什么需要字典
"""

# names = ['张三', '李四', '王五', '赵六']
# mobile = ['13333333333', '14444444444', '15555555555', '16666666666']
"""
如果想要找到某人的电话号码
先取到names的索引。
然后到mobile里面根据索引取到对应的电话号码
"""
# print(mobile[names.index('张三')])  # 13333333333

"""
    姓名和电话号码存储在一个数据结构中，指定姓名后直接得到对应的电话号码
"""

# a = {'张三': '13333333333', '李四': '14444444444', '王五': '15555555555', '赵六': '16666666666'}

# print(a['王五'])  # 15555555555

"""
字典的实现原理：
    和查字典类似。当我们在字典中查找某个字时，
    一种办法是从第一也开始往后翻，直到找到我们要查找的字为止，这种办法就是在列表中查找元素的办法，缺点：字典中的字数越多，效率越低
    第二种办法现在字典的索引表里（比如说部首表）超照这个字对应的页码，然后直接翻到这个字对应的页。优点：查找效率不会随着字典中字数的增加而降低
    无论查找哪个字，查找速度都非常快
字典的特点
    1.字典中所有元素都是key ： value  通过key 对应value   。字典中的key不可重复，value可以重复
    2.字典中的元素是无序的，顺序不重要，重要而是key和value的映射关系
    3.字典中的key是不可变对象，存取字典中的key-value对时，系统会调用内置函数hash根据指定的key计算出value的储存位置，也就是哈希值，对于指定的
    key，为了保证每次计算出的哈希值都是相同的，要求key必须是不可变对象，只有不可变对象才存在哈希值
    4.字典可以根据需要，动态伸缩
    系统会根据需要动态的分配和回收内存，因此在使用前无须预先声明字典的容量
    5.字典会浪费较大的内存，于列表相比，就是空间换取了时间
"""

"""
创建字典的方式
调用内置函数dict
"""

# print(dict({'name': 'dongdong', 'age': 18}))  # {'name': 'dongdong', 'age': 18}
# print(dict(name='dongdong', age=18))  # {'name': 'dongdong', 'age': 18}
# print(dict())  # {}
# print(dict([('name', 'dongdong'), ('age', 18)]))  # {'name': 'dongdong', 'age': 18}
# print(dict(zip(range(3), 'ABC')))  # {0: 'A', 1: 'B', 2: 'C'}   zip 用于将多个可迭代的对象进行打包压缩

"""
调用类dict方法fromKeys
调用方法fromKeys时，通过参数指定所有的key，所有的value值都为None
"""

# print(dict.fromkeys(['name', 'age']))  # {'name': None, 'age': None}
# print(dict.fromkeys(('name', 'age')))  # {'name': None, 'age': None}

"""
调用方法fromkeys时可以通过参数指定所有的value值
"""

# print(dict.fromkeys(['name', 'age'], ('hello', 'hi')))  # {'name': ('hello', 'hi'), 'age': ('hello', 'hi')}

"""
字典   查操作
1.使用中括号{}
2.调用方法get    如果方法中不包括指定的key，不报出KeyError，而是返回None
可以通过参数来设置默认的value，以便在字典中不存在指定的key值将其返回
"""

# a = {'name': 'DongDong', 'age': 18}
# print(a['name'])  # DongDong
#
# print(a.get('name'))  # DongDong
# print(a.get('hello'))  # None
# print(a.get('hello', 'hi'))  # hi

"""
可以使用运算符in来检查字典中是否存在指定的key & 使用not in 来检查字典中是否不存在指定的key
"""
# print('age' in a)  # True
# print('age' not in a)  # False

"""
字典的改操作
修改字典中指定的key对应的value
1.为已经存在的key赋予一个新的value值(一次只能修改一个key对应的value)
2.调用方法update（一次至少修改一个key对应的value）

"""

# a = {'name': 'jack', 'age': 18, 'gender': '男'}
#
# a['age'] = 20
# print(a)  # {'name': 'jack', 'age': 20, 'gender': '男'}
#
# a.update({'name': 'liu', 'age': 99})
# print(a)  # {'name': 'liu', 'age': 99, 'gender': '男'}
# a.update([('name', 'wang'), ('age', 21)])
# print(a)  # {'name': 'wang', 'age': 21, 'gender': '男'}
# a.update(name='z', age=10)
# print(a)  # {'name': 'z', 'age': 10, 'gender': '男'}

"""
字典中的增操作
增加的key不能是字典中存在的key
1.为不存在的key赋予一个value值   一次添加一个key-value对
2.调用方法update    一次至少增加一个key-value对
"""

# a = {'name': 'jack', 'age': 18, 'gender': '男'}
# a['class'] = 1
# print(a)  # {'name': 'jack', 'age': 18, 'gender': '男', 'class': 1}
#
# a.update({'score': 90, 'class': 1})
# print(a)  # {'name': 'jack', 'age': 18, 'gender': '男', 'class': 1, 'score': 90}
# a.update([('aaa', 'bbb'), ('ccc', 'ddd')])
# print(a)  # {'name': 'jack', 'age': 18, 'gender': '男', 'class': 1, 'score': 90, 'aaa': 'bbb', 'ccc': 'ddd'}
# a.update(aaac=1, bbbc=2)
# print(a)  # {'name': 'jack', 'age': 18, 'gender': '男', 'class': 1, 'score': 90,
# 'aaa': 'bbb', 'ccc': 'ddd', 'aaac': 1, 'bbbc': 2}

"""
字典的删除操作
调用方法pop用来返回指定key对应的value值-----一次只删除一个key-value对 
使用del语句删除key-value对-----一次只删除一个key-value对  
调用方法popitem来删除key-value对--该方法返回被删除的key-value对--一次删除任意一个key-value对 
调用方法clear清空字典 
"""
# a = {'name': 'jack', 'age': 18, 'gender': '男'}
# print(a.pop('name'))  # jack
# print(a)  # {'age': 18, 'gender': '男'}
#
# a = {'name': 'jack', 'age': 18, 'gender': '男'}
# del a['age']
# print(a)  # {'name': 'jack', 'gender': '男'}
#
# a = {'name': 'jack', 'age': 18, 'gender': '男'}
# print(a.popitem())  # ('gender', '男')
# print(a)  # {'name': 'jack', 'age': 18}
#
# a = {'name': 'jack', 'age': 18, 'gender': '男'}
# a.clear()
# print(a)  # print(a)

"""
为字典中的key设置默认的value值
为了确保字典中指定的key总是存在的，可以调用方法setdefault：
1.如果字典中存在指定的key，该方法返回指定key对应的value值，字典不发生变化
2.如果字典中不存在指定的key，该方法返回指定的默认value值，字典中增加一对key-value对,key为字典中不存在的key，value为指定的默认value值。
if ... not in 
"""

# a = {'name': 'liu'}
# print(a.setdefault('name', 'duck'))  # liu
# print(a)  # {'name': 'liu'}
# print(a.setdefault('age', 18))  # 18
# print(a)  # {'name': 'liu', 'age': 18}
# if 'name' not in a:
#     a['age'] = 18

"""
字典的视图
keys
values
items  
"""

# a = {'name': 'jack', 'age': 18, 'gender': '男'}
# print(a.keys())  # dict_keys(['name', 'age', 'gender'])
# print(list(a.keys()))  # ['name', 'age', 'gender']
# print(a.values())  # dict_values(['jack', 18, '男'])
# print(list(a.values()))  # ['jack', 18, '男']
# print(a.items())  # dict_items([('name', 'jack'), ('age', 18), ('gender', '男')])
# print(list(a.items()))  # [('name', 'jack'), ('age', 18), ('gender', '男')]

"""
视图会随着字典的变化而变化
"""

# a = {'name': 'jack', 'age': 18, 'gender': '男'}
# a.pop('name')
# print(a)  # {'age': 18, 'gender': '男'}
# print(a.items())  # dict_items([('age', 18), ('gender', '男')])
# a.update({'name': 'jack'})
# print(a)
# print(list(a.items()))  # [('age', 18), ('gender', '男'), ('name', 'jack')]

"""
借助字典创建格式化字符串

"""

# mobile = {'张三': 13333333333,
#           '李四': 14444444444,
#           '王五': 15555555555,
#           '赵六': 16666666666}
#
# print('王五的电话号码为 %s ，张三的电话号码为 %s' % (mobile['王五'], mobile['张三']))
# 不使用格式化字符串的办法
# 王五的电话号码为 15555555555 ，张三的电话号码为 13333333333

"""
当字符串中的占位符是百分号，并且占位符对应的实际值来自于某个字典的value时，可以把所有的实际值改写成为字典，勇士根绝字典的value对应的key在占位符%
的后面添加：（字典的key）。其中，字典的key挥别添加一堆对引号，因此，如果字典的key是字符串，需要去掉字典的key自带的引号。
"""

# print('张三的电话号是 %(张三)s ， 李四的电话号是 %(李四)s' % mobile)  # 张三的电话号是 13333333333 ， 李四的电话号是 14444444444

"""
使用花括号作为占位符
"""

# mobile = {'张三': 13333333333,
#           '李四': 14444444444,
#           '王五': 15555555555,
#           '赵六': 16666666666}
# print('王五的电话号码:{}, 李四的电话号码:{}'.format(mobile['王五'], mobile['李四']))  # 王五的电话号码:15555555555, 李四的电话号码:14444444444
"""
当定义的格式化字符串中的占位符是花括号，可以调用方法format_map并把该字典直接作为方法的参数，同时根据字典的value在花括号中指定对应的key：
{字典中的key}。其中字典的key会被添加一对引号，因此，如果字典的key是字符串，需要去掉字典的key自带的引号
"""
# print('张三的电话号码:{张三}, 王五的电话号码:{王五}'.format_map(mobile))  # 张三的电话号码:13333333333, 王五的电话号码:15555555555

"""
集合
除了列表，元组和字典，集合也是python提供的内置数据结构之一
可以把集合看成一个没有储存value的字典，
    集合中不可以存在重复的数据
    集合中的数据是无序的
    集合中的数据可以是任何不可变的类型，多种类型的数据可以混合存储在一个集合中
    集合可以根据需要动态伸缩，系统会根据需要动态的分配回收内存
    集合会浪费较大的内存，与列表相比，是用空间换取了时间。
"""

"""
创建方式
1.使用花括号
    将创建的集合赋值给变量时，变量名不要取名为set，因为set是集合对应的类名
2.
"""

# a = {2, 3, 45, 9, 11}
# print(a)  # {2, 3, 9, 11, 45}
#
# a = {2, 3, 45, 9, 11, 2, 3}
# print(a)  # {2, 3, 9, 11, 45}    >重复的数据会被去掉
# 不能直接使用{}来表示一个空集合

# print(type({}))  # <class 'dict'>  字典

"""
调用内置函数set
"""

# print(set(range(1, 6)))  # {1, 2, 3, 4, 5}
# print(set([3, 5, 6, 7]))  # {3, 5, 7, 9}
# print(set((1, 3, 5, 7, 9)))  # {1, 3, 5, 7, 9}
# print(set('13579'))  # {'9', '3', '7', '5', '1'}
# print(set({1, 3, 5, 7, 9}))  # {1, 3, 5, 7, 9}
#
# print(set())  # set() 空集合
#
# print(set({2, 3, 45, 9, 11, 2, 3}))  # {2, 3, 9, 11, 45}

"""
集合的关系
如何判断两个集合是否相等
    可以使用== 和！=进行判断
"""

# a = {1, 3, 4, 6}
# b = {3, 4, 1, 6}
# print(a == b)  # True
# print(a != b)  # False

"""
判断一个集合是否是另一个集合的子集
    调用方法issubset进行判读
"""

# a = {1, 3, 5, 7, 9, 11, 13}
# b = {1, 3, 4, 6, 7, 0}
# c = {1, 3, 5, 7, 9, 11}
#
# print(a.issubset(b))  # False  判断a是否是b的子集
# print(c.issubset(a))  # True   判断c是否是a的子集
# print(b.issubset(c))  # False  判断b是否是c的子集

# import time      时间戳

# a = time.time()
# print("当前的时间戳为 %.f" % a)

"""
    如何判断一个集合是否是另一个集合的超集
    调用方法issuperset进行判断
"""

# print(a.issuperset(c))  # True
# print(b.issuperset(c))  # True
# print(c.issuperset(a))  # False

"""
    如何判断两个集合是否没有交集
    调用方法isdisjoint
"""

# a = {1, 3, 5, 7, 9}
# b = {2, 3, 6, 8, 10}
# c = {2, 4, 6, 8, 10}
#
# print(a.isdisjoint(b))  # False
# print(a.isdisjoint(c))  # True
# print(b.isdisjoint(c))  # False

"""
两个集合的交集
调用方法intersection来查看两个集合的交集
使用 ' & ' 也可以查看两个集合的交集
使用两个方法 集合本身不发生变化

"""

# a = {1, 3, 5, 6, 7}
# b = {1, 4, 7, 3, 9}
# print(a.intersection(b))  # {1, 3, 7}
# print(a & b)  # {1, 3, 7}
# print(a)  # {1, 3, 5, 6, 7}
# print(b)  # {1, 3, 4, 7, 9}

"""
a.intersection_update(b)的执行结果
    使用 a.intersection(b)返回值更新a，  b不变
    方法intersection_update的返回值为None
"""

# print(a.intersection_update(b))  # None
# print(a)  # {1, 3, 7}
# print(b)  # {1, 3, 4, 7, 9}

# print(b.intersection_update(a))
# print(a)  # {1, 3, 5, 6, 7}
# print(b)  # {1, 3, 7}

"""
两个集合的并集
调用方法union来查看两个集合的并集
使用 ' | ' 也可以查看两个集合的并集
不存在方法union_update
且两个集合不发生变化
"""
# a = {1, 3, 5, 6, 7}
# b = {1, 4, 7, 3, 9}
# print(a.union(b))  # {1, 3, 4, 5, 6, 7, 9}
# print(a | b)  # {1, 3, 4, 5, 6, 7, 9}
# print(a)
# print(b)

"""
两个集合的差集
调用方法difference来查看两个集合的差集
使用 ' - ' 也可以查看两个集合的交集
做差级操作后生成一个新的集合，做差级操作的两个集合不变
"""
# a = {1, 3, 5, 6, 7}
# b = {1, 4, 7, 3, 9}
# print(a.difference(b))  # {5, 6}
# print(b.difference(a))  # {9, 4}
#
# print(a - b)  # {5, 6}
# print(a)
# print(b)

"""
difference_update
a.difference_update(b)的返回值为None
a集合生成了一个新的集合
b集合不变
"""

# print(a.difference_update(b))  # None
# print(a)  # {5, 6}
# print(b)  # {1, 3, 4, 7, 9}

"""
两个集合的对称差集
两个集合的并集去除两个集合的差集为两个集合的对称差集
调用方法symmetric_difference来查看两个集合的差集
使用 ' ^ ' 也可以查看两个集合的交集
使用对称差集操作后生成一个新的集合，做对称差集的两个集合不变
"""

# a = {1, 3, 5, 6, 7}
# b = {1, 4, 7, 3, 9}
#
# print(a.symmetric_difference(b))  # {4, 5, 6, 9}
# print(a ^ b)  # {4, 5, 6, 9}
# print(a)  # {1, 3, 5, 6, 7}
# print(b)  # {1, 3, 4, 7, 9}

"""
a.symmetric_difference_update(b)的返回值为None
a集合生成了一个新的集合
b集合不变
"""
# print(a.symmetric_difference_update(b))  # None
# print(a)  # {4, 5, 6, 9}
# print(b)  # {1, 3, 4, 7, 9}

"""
集合的查操作；
可以使用运算符in检查集合中是否存在指定的元素，或者使用not in来检查集合中是否不存在指定的元素
"""

# a = {3, 4, 5, 6, 7}
# print(5 in a)  # True
# print(8 in a)  # False
#
# print(5 not in a)  # False
# print(8 not in a)  # False

"""
集合的增操作
如果想要往集合里面添加元素，常见的方式有两种；
1.调用方法add,      一次添加一个元素。如果集合内存在指定的元素，则不会被添加  
2.调用方法update:   一次至少添加一个元素。如果集合内存在指定的元素，则不会被添加  
"""

# a = {1, 2, 3, 5, 6}
# a.add(7)
# print(a)  # {1, 2, 3, 5, 6, 7}
#
# a = {1, 2, 3, 5, 6}
# a.update({4, 7})  # {1, 2, 3, 4, 5, 6, 7}
# print(a)
#
# a.update([4, 7])
# print(a)  # {1, 2, 3, 4, 5, 6, 7}
#
# a.update((4, 7))
# print(a)  # {1, 2, 3, 4, 5, 6, 7}

"""
集合的删操作
1.调用方法remove    如果想要删除的元素不存在，则报错KeyError    一次只删除一个元素
2.调用方法discard   如果想要删除的元素不存在，不会报KeyError    一次只删除一个元素
3.调用方法pop       该方法返回被删除的元素，一次只删除一个任意的元素
4.调用方法clear     该方法用来清空集合
"""

# a = {3, 4, 5, 6, 7}
# a.remove(5)
# print(a)  # {3, 4, 6, 7}
#
# a = {3, 4, 5, 6, 7}
# a.discard(5)
# print(a)  # {3, 4, 6, 7}
#
# a.discard(8)
# print(a)  # {3, 4, 6, 7}
#
# a = {3, 4, 5, 6, 7}
# print(a.pop())  # 3
# print(a)  # {4, 5, 6, 7}
#
# a = {3, 4, 5, 6, 7}
# a.clear()
# print(a)  # set()

"""
不可变集合 frozenset     
    frozenset的意思是"被冻结的set"，也就是不可变的set
    frozenset之于set就好比tuole之于list
     因为frozenset是不可变类型，所以frozenset类型的对象：
1.存在哈希值（哈希值只有在不可变类型中存在）
2.可以作为字典的key
3.可以作为set中的元素
"""

"""
frozenset对象的创建
    可以调用内置函数frozenset来创建frozenset对象

"""

# print(frozenset())  # frozenset()
#
# print(frozenset(range(1, 6)))  # frozenset()
#
# print(frozenset([1, 3, 5, 6]))  # frozenset()
#
# print(frozenset((1, 3, 5)))  # frozenset({1, 3, 5})
#
# print(frozenset("35926"))  # frozenset({1, 3, 5})
#
# print(frozenset({3, 5, 9, 2, 6}))  # frozenset({1, 3, 5})

# 在程序中尽量使用不可变类型的对象，一旦创建不可变类型的对象，所有数据不会被修改，就不会导致修改数据产生的错误
# 在多任务环境下，同时操作对象时，不需要加锁。

"""
流程控制的概述
任何简单或者复杂的算法，都可以由：顺序结构，选择结构和循环结构三种节本结构组合而成
顺序结构   指的是程序从上到下顺序的执行代码。中间没有任何判断和跳转，直到程序结束
选择结构   if语句          程序根据判断条件的布尔值，选择执行部分代码
循环结构   while和for      程序根据循环条件反复执行某段代码，知道不满足循环条件为止。
"""

"""
条件表达式是包含if-else语句的表达式，类似于C语言中的三木条件运算符
语法格式：
x if 判断条件  else y
对应的运算规则：
    判断条件的布尔值为True，返回x
    否则返回y
"""

# score = 100
# result = '及格了' if score >= 60 else '没及格'
# print(result)  # 及格了
#
# if score >= 60:
#     result = '及格了'
# else:
#     result = '没及格'
# print(result)  # 及格了
#
# a = 6
# b = 4
# print('a大于b' if a > b else('a小于b' if a < b else 'a等于b'))   # 先判断a > b 如果a不大于b判断a小于等于b 然后从小于或者等于里面再次判断

"""
while 语句，
while 循环控制变量 循环条件：
    循环体
其中，循环体对应的代码块必须缩进。

1.初始化部分，用于设置循环初始条件，比如循环控制变量的初始值
2.循环条件，每次循环都要判断布尔值，以决定继续循环还是终止循环，
循环条件中通常包含循环控制变量
3.循环体：这是循环操作的主体内容，可以是一条语句，也可以是多条语句，
循环体中的某些词语用于改变循环控制变量的值，从而改变循环条件的布尔值
"""

# b = 0
# while b <= 1000:
#     print(b)
#     b += 1
# for a in range(1, 4):
#     print(a)

"""
for in语句
    专门用于遍历序列，字典，集合等类型的对象
    遍历：把对象所有的元素依次访问一遍，每访问一个元素，成为一次迭代，因此，可以使用for-in语句
遍历的对象又被称为可迭代对象。
    当迭代次数已知的时候，推荐使用for-in语句，
    当迭代次数未知的时候，推荐使用while语句，
"""

"""
使用for-in语句遍历range，列表，元祖和字符串等序列
"""

# for a in range(1, 4):
#     print(a)
#
# for _ in range(1, 4):
#     print("hello")
#
# for a in [1, 2, 3]:
#     print(a)
# for a in (1, 2, 3):
#     print(a)
# for a in "123":
#     print(a)
#
# words = ['Java', 'python', 'Kotlin', 'Swift', 'Go', 'remember']
# for word in words[:]:
#     if len(word) < 5:
#         words.remove(word)
# print(words)  # ['python', 'Kotlin', 'Swift', 'remember']  通过列表切片的方法去修改列表
#
# a = {2, 3, 1}
# for number in a:
#     print()
#
# s = {2, 3, 1}
# for number in s:
#     print(number)
# for number in sorted(s):
#     print(number)
#
# a = {'Fruits': 1, 'books': 121, 'ide': 111}
# for c in a:
#     print(c)  # 元素值指的是字典的key
# for c in a.values():
#     print(c)
# for c in a.items():
#     print(c)
# for c in sorted(a.items()):
#     print(c)  # 输入的值为key和value按顺序排序
# for c in sorted(a.values()):
#     print(c)
# for c in sorted(a.keys()):
#     print(c)

'''
带索引的序列遍历
如果在遍历序列的过程中需要访问元素的索引的方法：

'''
#  方法1
# a = ['java', 'python', 'C', 'C++']
# index = 0
# for c in a:
#     print('a[{}] = {}'.format(index, c))
#     index += 1
# # 方法2
# for index in range(len(a)):
#     print('a[{}] = {}'.format(index, a[index]))  # 因为index表示的为元素索引，循环列表a内的索引就对应的为a[0],a[1]...所以a[index]=对应索引的元素
# # 方法3
# index = 0
# while index < len(a):
#     print('a[{}] = {}'.format(index, a[index]))
#     index += 1
# 方法4 调用内置函数enumerate(类enumerate的构造方法)，将要遍历的序列转换为enumerate对象。
# print(enumerate(a))  # <enumerate object at 0x1076c63c0>
# print(list(enumerate(a)))  # [(0, 'java'), (1, 'python'), (2, 'C'), (3, 'C++')]
# # 调用方法enumera时，可以通过第二个参数指定指定索引的起始值。
# print(list(enumerate(a, 1)))  # [(1, 'java'), (2, 'python'), (3, 'C'), (4, 'C++')]
# for index, item in enumerate(a):
#     print('a[{}] = {}'.format(index, item))
# for index, item in list(enumerate(a)):
#     print('a[{}] = {}'.format(index, item))
# exit()

"""
    在执行while语句或者for-in语句时，如果循环正常结束，也就是说，如果没有执行循环体中的break语句从而提前退出循环，
有时可能在循环正常结束后执行某些操作
    为了判断循环是否正常，可以使用一个布尔变量，在循环开始前将布尔变量的值设置为False，如果执行了循环体中的break语句从而
提前退出循环，那就将布尔的值设置为True。
最后在while语句或者for-in语句的后面使用if语句判断布尔变量的值，以判断循环是否是正常结束的。

"""

# isBreak = False
# n = 0
# while n < 5:
#     if n == 6:
#         isBreak = True
#         break
#     n += 1
# if not isBreak:
#     print('循环正常结束，没有执行循环体中的break语句')
#
# isBreak = False
# for a in range(7):
#     if a == 8:
#         isBreak = True
#         break
# if isBreak is False:
#     print('循环正常结束，没有执行循环体中的break语句')

"""
解决方案2：
    python为循环语句提供了break-else结构，也就是说在while语句或者for-in语句的后面添加else从句，
这样如果没有执行循环体中的break语句，从而提前退出循环，就会执行else语句。
"""

# i = 0
# while i < 5:
#     i += 1
#     if i == 6:
#         break
#     else:
#         print("循环%s次" % i)
# else:
#     print('循环正常结束，没有执行循环体中的break语句')

# for i in range(5):
#     if i == 6:
#         break
# else:
#     print('循环正
#     常结束，没有执行循环体中的break语句')

"""
    在while语句或for-in
"""

# for i in range(1, 5):
#     if i == 3:
#         continue
#     print("i = ", i)
# for i in range(1, 5):
#     if i == 3:
#         break
#     print('i = ', i)
#
# for i in range(1, 5):
#     for n in range(1, 5):
#         if i == n:
#             continue
#         print('i = ', i, 'n = ', n)

# for i in range(1, 4):
#     for n in range(1, 4):
#         if i == n:
#             break
#         print('i = ', i, 'n = ', n)
# i =  2 n =  1
# i =  3 n =  1
# i =  3 n =  2

# for i in range(1, 4):
#     for n in range(1, 4):
#         if i == n:
#             continue
#         print('i = ', i, 'n = ', n)
# i =  1 n =  2
# i =  1 n =  3
# i =  2 n =  1
# i =  2 n =  3
# i =  3 n =  1
# i =  3 n =  2


# for i in range(1, 4):
#     for n in range(1, 4):
#         if i == n:
#             print('i = ', i, 'n = ', n)
#             break

"""
    遍历多个对象。使用zip进行遍历。
    遍历的过程可以理解为打包压缩
    使用*zip进行解压缩
    如果两个并行的列表长度不同，较长的列表会被截断。
"""

# names = ['jack', 'mike', 'tom']
# ages = [18, 19, 22, 33]
#
# for names, ages in zip(names, ages):
#     print(names, '的年龄是：', ages)


# a = [1, 2, 3]
# b = [4, 5, 6]
#
# print(list(zip(*zip(a, b))))  # [(1, 2, 3), (4, 5, 6)]
#
# print(list(zip(*zip(a, b))))  # [(1, 2, 3), (4, 5, 6)]
#
# a2, b2 = zip(*zip(a, b))  # 使用*zip进行解压缩
# print(list(a2))  # [1, 2, 3]
# print(list(b2))  # [4, 5, 6]


"""
    遍历可迭代对象的内置函数map
      第一个参数指定函数名，第二个指定可迭代对象。
      调用内置函数map后，会使用指定的函数名作用于指定可迭代对象的每个元素，然后生成新的可迭代对象。
"""

# result = map(ord, 'abcd')
# print(result)  # <map object at 0x1018affa0>
# print(list(result))  # [97, 98, 99, 100]

# str.upper表示str的方法upper，也就是字符串的方法upper

# result = map(str.upper, 'abcd')
# print(result)  # <map object at 0x1014edee0>
# print(list(result))  # ['A', 'B', 'C', 'D']
#
# result = map(str.upper, ['abcd', 'efgh'])
# print(result)  # <map object at 0x101ab95b0>
# print(list(result))   # ['ABCD', 'EFGH']

"""
    用于遍历可迭代对象的内置函数filter
        第一个参数指定函数名，第二个参数指定可迭代对象
        调用内置函数filter后，会使用指定的内置函数名作用于指定的可迭代对象的每个元素，过滤掉函数返回值为False的相关元素，
        然后生成新的可迭代对象。
"""

# result = filter(str.isalpha, '1234abc')  # isalpha判断是否是字母。
# print(result)  # <filter object at 0x10364e550>
# print(list(result))  # ['a', 'b', 'c']

"""
列表生成式
    如果想要生成列表[1, 4, 9, 16, 25, 36]
"""
# a = []
# for i in range(1, 7):
#     a.append(i * i)
#     print(a)

# 语法格式 [表示列表元素的表达式 for 自定义的变量 in 可迭代对象]
# 其中'表示列表元素的表达式'通常包含自定义的变量
# 凡是可以通过for-in循环来创建的列表，都可以使用列表生成式来创建

# a = [i * i for i in range(1, 7)]
# print(a)  # 表示列表元素的表达式
#
# a = [i * i for i in range(1, 10)]
# print(a)

"""
    在列表生成式可以使用if语句，
    可以在列表生成式的for-in循环后添加if语句


"""

# a = [i * i for i in range(1, 7) if not i % 2]
# print(a)  # [4, 16, 36]
#
# a = []
# for i in range(1, 7):
#     if not i % 2:
#         a.append(i * i)
# print(a)
#
# a = []
# for c in range(1, 4):
#     for d in range(1, 4):
#         a.append((c, d))
# print(a)
# [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]

"""
    列表生成式中使用双重循环
"""

# a = [(c, d)for c in range(1, 4) for d in range(1, 4)]
# print(a)
# # [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
#
# a = [(c, d)for c in range(1, 4) for d in range(1, 4) if c == d]
# print(a)  # [(1, 1), (2, 2), (3, 3)]

"""
列表生成式支持嵌套
    可以在一个列表生成式内嵌套另一个列表生成式
"""

# a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
#
# b = [[row[i] for row in a] for i in range(4)]  # row[i]取出一维列表i中对应索引的元素为i的元素
# print(b)  # [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
#
# a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# b = []
# for i in range(4):
#     b.append([row[i] for row in a])
# print(b)  # [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
#
# a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# c = []
# for i in range(4):
#     b = []
#     for row in a:
#         b.append(row[i])
#     c.append(b)
# print(c)

"""
集合生成式
    如果想要生成集合{1, 4, 9, 16, 25, 36},可以使用for-in循环
"""

# s = set()
# for i in range(1, 7):
#     s.add(i * i)
# print(s)  # {1, 4, 36, 9, 16, 25}
#
# s = {i * i for i in range(1, 7)}
# print(s)  # {1, 4, 36, 9, 16, 25}
#
# s = {i * i for i in range(1, 7) if i % 2}
# print(s)  # {1, 9, 25}
# s = {i * i for i in range(1, 7) if not i % 2}
# print(s)  # {16, 4, 36}
#
# s = set()
# for i in range(1, 7):
#     if not i % 2:
#         s.add(i * i)
# print(s)  # {16, 4, 36}

"""
    集合生成式中使用双重循环
"""

# s = {(i, c) for i in range(1, 4) for c in range(1, 4)}
# print(s)  # {(1, 2), (2, 1), (3, 1), (1, 1), (2, 3), (3, 3), (2, 2), (3, 2), (1, 3)}
#
# s = set()
# for i in range(1, 4):
#     for c in range(1, 4):
#         s.add((i, c))
# print(s)  # {(1, 2), (2, 1), (3, 1), (1, 1), (2, 3), (3, 3), (2, 2), (3, 2), (1, 3)}

"""
    集合生成式中使用双重循环&if语句
"""

# s = {(i, c) for i in range(1, 4) for c in range(1, 4) if i == c}
# print(s)  # {(1, 1), (3, 3), (2, 2)}
#
# s = {(i, c) for i in range(1, 4) for c in range(1, 4) if i != c}
# print(s)  # {(1, 2), (2, 1), (3, 1), (2, 3), (3, 2), (1, 3)}

"""
字典生成式

"""
# 使用 for-in循环
# a = ['iFruits', 'books', 'hello']
# b = [11, 22, 33]
# c = {}
# for a, b in zip(a, b):
#     c[a.upper()] = b
# print(c)  # {'IFRUITS': 11, 'BOOKS': 22, 'HELLO': 33}

# 字典生成式
# for 自定义的表示key的变量，自定义的表示value的变量 in 可迭代对象
# 其中，'表示字典key的表达式'中通常包含'自定义的表示key的变量'，'表示字典value的表达式'中通常包含'自定义的表示value的变量'。

# a = ['iFruits', 'books', 'hello']
# b = [11, 22, 33]
#
# c = {a.upper(): b for a, b in zip(a, b)}
# print(c)  # {'IFRUITS': 11, 'BOOKS': 22, 'HELLO': 33}

# 凡是可以通过for-in循环的字典都可以用字典生成式来创建、

"""
    字典生成式中使用if语句
        可以在字典生成式for-in循环后添加if语句
"""

# c = {a.upper(): b for a, b in zip(a, b)
#      if b > 20}
# print(c)  # c = {a.upper(): b for a, b in zip(a, b)}

"""
    字典表达上使用双重for-in循环
"""
# c = {a: b for a in range(1, 4) for b in range(1, 4)}
# print(c)  # {1: 3, 2: 3, 3: 3}   因为字典中的key是唯一的 所以 1：1 ，1：2被1：3 覆盖掉了
# #  2：1 ， 2：2 都被2：3 覆盖掉了 -- 3：1 ， 3：2 都被3：3覆盖了
# c = {}
# for a in range(1, 4):
#     for b in range(1, 4):
#         c[a] = b
# print(c)  # {1: 3, 2: 3, 3: 3}
#
# c = {a: b for a in range(1, 4) for b in range(1, 4) if a != b}
# print(c)  # {1: 3, 2: 3, 3: 2}
#
#
# c = {}
# for a in range(1, 4):
#     for b in range(1, 4):
#         if a != b:
#             c[a] = b
# print(c)  # {1: 3, 2: 3, 3: 2}

"""
函数
    函数就是个黑匣子，他接收输入（参数），然后执行特定任务以完成特定功能，以完成特定功能的输出。
    其中，输入（参数）、输出（返回值）都是可选的，也就是说，可以有也可以没有。
    函数就是执行特定任务已完成特定功能的一段代码，可以在程序中将某段代码定义成函数，并制定一个函数名及接收的输入，这样
    我们就可以在程序的其他地方通过函数名多次调用并执行该段代码了，每次调用执行后，都会根据接收的输入执行特定的任务以完成特定功能
    从而生成响应的输出，
    python已经定义了很多内置函数，我们可以在程序中直接调用这些内置函数，
复用代码
隐藏实现细节
    很多时候，无须关注函数的实现细节，只需要关注，其接收的输入，级生成的输出，
提高可维护性
    修改时，只需要在一个地方进行修改了，否则你需要找到这段代码多个不同的地方，
    每个地方都要进行同样的修改，费时费力。
提高可读性，便于调试。
    每个函数都对应一段完成特定功能的代码。这样就提高了程序的可读性，便于程序调试。
"""

# # 第一次调用函数id（），输入（整数）的是类型的字符串
# print(id(18))
# # 返回的是输出为（4444990288）为输入id（18）的唯一标识
# print(id('hello'))
# print(id([]))

"""
函数的定义和调用。
def 函数名([形式参数1， 形式参数2...形式参数n]):
    函数体
其中def是python定义的关键字

说明：
    函数名:每个函数都有一个函数名，用于函数调用函数名属于标识符，因此必须遵守标识符的命名规则，推荐遵守标识符的命名规范，
          此外，函数名最好是动宾格式，以表明完成的特定功能，例如： user_id 
    形式参数：简称形参，形参用于在调用函数的时候接收输入，也就是接收传递的实际参数（简称实参），形参用中括号表示，表示形参是可选的
            也就是说，可以定义也可以不定义。形参的本质是变量，，其作用域（起作用的范围）仅限于函数体
    函数体:函数体是用于执行特定任务已完成特定功能的主体代码，函数体对应的代码块必须缩进，如果函数需要有返回值，可以在函数体内通过return xxx进行
          返回。同时结束函数体的执行，如果函数不需要有输出（返回值），可以通过语句return直接结束函数体的执行，或者让函数体正常执行结束，
          其实，在这两种情况下，都是有返回值的，返回值都是None。函数体在调用函数时才会被执行，因此，定义函数并不会改变函数的执行流程。
"""

# def decide_args(arg1, arg2):
#     if arg1 and arg2:
#         return arg1, arg2
#     elif (not arg1) and (not arg2):  # 形参arg1和arg2都为False打印
#         return
#     else:
#         result = arg1 or arg2

"""
    定义函数后，就创建了一个函数对象，他的返回值为function
"""
# print(decide_args)  # <function decide_args at 0x101519040>
# print(type(decide_args))  # <function decide_args at 0x101519040>

"""
调用函数：
    调用函数时，每个实参都被用处初始化显影的形参，所有形参都被初始化后，函数体对应的代码块被执行，
程序的执行流会跳转到定义函数的函数体内，执行函数体对应的代码块，执行完函数体后，在跳回到调用函数的地方，继续执行下一条语句，
"""

# print(decide_args(18, 'hello'))  # (18, 'hello')
# print(decide_args({}, []))  # None
# print(decide_args([], 11))  # None

"""
函数的调用之位置实参：
调用函数时，可硬二局每个形参在所有形参中的位置传递对应位置的实参，从而用每个实参初始化，
"""

# def f(a, b, c):
#     print('a =', a, 'b =', b, 'c =', c)
#
#
# f(2, 5, 8)  # a = 2 b = 5 c = 8
# f(5, 8, 2)  # a = 5 b = 8 c = 2
# f(8, 5, 2)  # a = 8 b = 5 c = 2

"""
函数的调用之关键字实参
调用函数时，传递的实参形式可以为：形参名 = 实参值，从而用指定的实参值初始化指定名称的形参，这样的
实参成为关键字实参
由于关键字实参中指定看形参名，所以实参和形参的匹配关系更加清晰，而且每个关键字实参在所有
关键字实参中的位置可以是任意的
"""

# def f(a, b, c):
#     print('a =', a, 'b =', b, 'c =', c)
#
#
# f(a=2, b=5, c=8)  # a = 2 b = 5 c = 8
# f(b=5, c=8, a=2)  # a = 2 b = 5 c = 8
#
# # 调用函数的时候，可以组合使用位置实参和关键字实参。但是，位置实参必须位于关键字实参之前，否则，无法根据位置来匹配位置实参和对应的形参。
# f(2, 5, c=8)  # a = 2 b = 5 c = 8
# # f(2, c=8, 5)

"""
函数的调用之实参的传递
变量就相当于标签。对于赋值语句：变量 = 对象， 相当于给对象贴了个标签，标签名就是变量名。
    调用函数时把实参传递给形参，从而用实参初始化形参，本质上执行的赋值语句：形参 = 实参对象，
相当于给实参对象贴了个标签，标签名就是形参名。
    如果实参对象是可变类型的，在函数体内对形参对象的任何修改其实就是对实参对象的修改。
"""

# def f(age1, age2):
#     print('初始化形参后：age1 = ', age1, 'age2 = ', age2)  # 初始化形参后：age1 =  10 age2 =  [1, 2, 3]
#     age1 = age1 * 2
#     age2.append(4)
#     print('修改形参后：age1 =', age1, 'age2 =', age2)  # 修改形参后：age1 = 20 age2 = [1, 2, 3, 4]
#
#
# i = 10
# L = [1, 2, 3]
# print('调用函数前： i = ', i, 'L = ', L)  # 调用函数前： i =  10 L =  [1, 2, 3]
# f(i, L)
# print('调用函数后： i = ', i, 'L = ', L)  # 调用函数后： i =  10 L =  [1, 2, 3, 4]  因为实参L的对象是一个列表，为可变类型，所以修改形参L就相当于修改实参L。
#
# i = 10
# L = [1, 2, 3]
# print('调用函数前： i = ', i, 'L = ', L)  # 调用函数前： i =  10 L =  [1, 2, 3]
# f(i, L[:])
# print('调用函数后： i = ', i, 'L = ', L)  # 调用函数后： i =  10 L =  [1, 2, 3]

"""
    如果需要在调用函数后有多个返回值，可以在定义函数时在函数体内使用return语句返回多个值组成的元素
"""

# 打印单双数
# def classify_numbers(numbers):
#     odds = []
#     evens = []
#
#     for number in numbers:
#         if number % 2:
#             odds.append(number)
#         else:
#             evens.append(number)
#
#     return odds, evens


# print(classify_numbers([1, 3, 5, 2, 6, 8]))  # ([1, 3, 5], [2, 6, 8])

# 打印最大值和最小值

# def a(numbers):
#     if len(numbers) == 0:
#         return
#
#     min_number = numbers[0]
#     max_number = numbers[0]
#
#     for number in numbers[1: len(numbers)]:
#         if number < min_number:
#             min_number = number
#         if number > max_number:
#             max_number = number
#     return min_number, max_number
#
#
# print(a([1, 2, 32, 55, 62]))


"""
    函数的定义之带默认值的形参
定义函数时，可以给形参设置默认值，这样，调用函数时如果不传递对应的实参，就会使用设置的默认值初始化形参，
    给形参设置默认值的语法格式为：形参 = 默认值
"""

# def f1(a, b = 5):
#     print('a =', a, 'b = ', b)
#
#
# f1(2, 6)
# f1(2)
#
#
# def f2(a=2, b=5, c=8):
#
#     print('a =', a, 'b = ', b, 'c = ', c)
#
#
# f2(2, 6, 9)  # a = 2 b =  6 c =  9
# f2(1)  # a = 1 b =  5 c =  8
# f2()  # a = 2 b =  5 c =  8

"""
定义函数时，没有设置默认值的形参必须位于设置了默认值的形参之前，否则，无法根据位置来匹配位置实参和对应的形参
"""

# def f(b=5, a):  有默认值的形参必须要在后面
# 假设上面的定义可以使用，对于调用f(2)，你可能想把实参2传递给形参a，但是实参2是位置实参，因此实参2会传递给b，从而导致形参a存在实参缺失

"""
当函数有多个形参时，把变化大的形参放在前面，把变化小的形参放在后面，变化小的形参就可以设置默认值。

给形参设置默认值之后，调用函数时就存在多动调用方式
"""

# def fun(a, b=5):
#     print('a = ', a, 'b = ', b)


# fun(3)  # a =  3 b =  5  传入a的位置实参，使用b的默认实参
# fun(a=3)  # a =  3 b =  5  传入a的关键字实参，使用b的默认实参
# fun(3, 6)  # a =  3 b =  6  使用a的位置实参，使用b的位置实参
# fun(a=3, b=6)  # a =  3 b =  6  使用a和b的关键字实参
# fun(b=6, a=3)  # a =  3 b =  6  使用a和b的关键字实参
# fun(3, b=6)  # a =  3 b =  6  使用位置实参，和关键字实参。


"""
    定义函数时，给形参设置的默认值就被计算出来了，因此，如果给形参设置的默认值是可变类型的对象，
并且前一次调用函数时在函数体内修改了形参的默认值，那么修改后的值将作为下一次调用函数式形参的默认值。
    不要把形参的默认值设置为可变类型的对象
"""

# def fun(i=[]):
#     i.append(18)
#     print(i)
#
#
# fun()  # [18]
# fun()  # [18, 18]
# fun()  # [18, 18, 18]
#
#
# def fun(i=None):
#     if i is None:
#         i = []
#     i.append(18)
#     print(i)
#
#
# fun()  # [18]
# fun()  # [18]
# fun()  # [18]

"""
使用*定义关键字形参
定义函数时，可以在所有形参的某个位置添加一个 * 这样 * 后面的所有形参都被定义为只能接收关键字形参的关键字形参。
"""

#
# def f(a, b, *, c, d):
#     print('a =', a, 'b =', b, 'c =', c, 'd =', d)
#
#
# f(1, 2, c=3, d=4)  # a = 1 b = 2 c = 3 d = 4
# f(1, 2, 3, 4)   使用位置实参报错，


"""
使用*定义个数可变的位置形参
    定义函数时，可能无法事先确定传递的位置实参的个数，在这种情况下，可以在形参前添加一个*，
将形参定义为个数可变的位置形参，从而可以接收0个或任意多个位置实参，这些位置实参会将个数可变的位置形参初始化为一个元组
"""
#
#
# def f(*ages):
#
#     print(ages)
#
#
# f()  # ()
# f(1)  # (1,)
# f(1, 2, 3)  # (1, 2, 3)
#

"""
 定义函数时，最多只能定义一个个数可变的位置形参
 很多内置函数都定义了个数可变的位置形参，例如：内置函数print（）的定义为
    def print(self, *args, sep=' ', end='\n', file=None):
"""
# print(1)
# print(1, 2, 3)

"""
通常我们把个数可变的位置形参定义为最后一个形参，一边接受所有剩余位置的实参，
"""

# def fun1(a, b, *c):
#     print('a =', a, 'b =', b, 'c =', c)  # a = 1 b = 2 c = (3, 5, 6)
#
#
# fun1(1, 2, 3, 5, 6)


"""
    如果个数可变的位置形参不是最后一个形参，那么其后面的所有形参都被定义为只能接收关键字实参的关键字形参
如果向这些关键字形参传递位置实参，所有的位置实参都会被算作个数可变的，从而导致关键字实参的缺失，
"""

# def fun2(*a, b, c):
#     print('a =', a, 'b =', b, 'c =', c)  # a = (1, 2, 3) b = 2 c = 3
#
#
# fun2(1, 2, 3, b=2, c=3)

# TypeError: fun2() missing 2 required keyword-only arguments: 'b' and 'c'
# 形参b和c对应实参丢失，   =缺失b&c的关键字实参
# fun2(1, 2, 3, 4, 5)


"""
使用*将序列中的每个元素都转换为位置实参：
    调用函数时，可以在序列前面加一个*，从而将序列中的每一个元素都转换为一个单独的位置实参。
    注意：：：和个数可变的位置形参进行区分！！！
    个数可变的位置形参是在定义函数时使用，
    使用*将序列中的每个元素都转换为位置实参是在调用函数时使用。
"""

# def f(a, b, c):
#     print('a =', a, 'b =', b, 'c =', c)
#
#
# f(1, 2, 3)
# L = [1, 2, 3]
# # f(L)
# f(L[0], L[1], L[2])  # a = 1 b = 2 c = 3
# f(*L)  # a = 1 b = 2 c = 3
#
#
# def fun(*ages):
#     print(ages)


# 将列表L整体作为一个位置实参

# fun(L)  # ([1, 2, 3],)

# 现将列表里面的每一个元素都转换为一个单独的位置实参，然后使用转换出来的位置实参将个数可变的位置形参初始化为一个元组，
# fun(*L)  # (1, 2, 3)

"""
    定义函数时，最多只能定义一个个数可变的关键字形参。
"""

#
# def f(**ages):
#     print(ages)
#
#
# F = {1, 2, 3}
# f(a=1, b=2, c=3)  # {'a': 1, 'b': 2, 'c': 3}
# f(a=F, b=1, c=1)

"""
调用函数时，位置实参必须位于关键字形参之前，所以个数可变的位置形参必须位于关键字形参的后面
"""

#
# def f(hello, hi, **ages,):  # def f(*args, **ages,):
#     print('hello =', hello, 'hi =', hi, 'ages =', ages)
#
#
# f(1, 2, a=1, b=2, c=3)  # hello = 1 hi = 2 ages = {'a': 1, 'b': 2, 'c': 3}


"""
    很多内置函数都定义了一个可变的关键字形参，内置函数sorted（）的定义为：
def sorted(*args, **kwargs):    其中 *args表示个数可变的位置形参，**kwargs表示各市可变的关键字形参
"""

# a = ['python', 'java', 'swift']
# print(a)  # ['python', 'java', 'swift']
# print(sorted(a))  # ['java', 'python', 'swift']
# print(sorted(a, key=len))  # ['java', 'swift', 'python']    key=len 表示按照长度排序。
# print(sorted(a, key=len, reverse=True))  # ['python', 'swift', 'java']    其中key=len，reverse=True都表示可变的关键字形参，

"""
    函数的调用之使用**将字典中的每个键值对都转换为关键字实参。
"""

# def f(a, b, c):
#     print('a =', a, 'b =', b, 'c =', c)
#
#
# f(a=1, b=2, c=3)  # a = 1 b = 2 c = 3
#
# d = {'a': 1, 'b': 2, 'c': 3}
#
# # f(d)  # TypeError: f() missing 2 required positional arguments: 'b' and 'c'
#
# f(a=d['a'], b=d['b'], c=d['c'])  # a = 1 b = 2 c = 3

"""
    在调用函数时，可以在字典前面加**，从而将字典中的每一个键值对都转换为一个单独的关键字实参。
    
注意和个数可变的关键字形参进行区分，个数可变的关键字形参是在定义函数的时候使用，
使用**将字典中的每个舰队之都转换为关键字实参是在调用函数的时候用的
"""

# f(**d)  # a = 1 b = 2 c = 3
#
# d = {'a': 1, 'b': 2, 'c': 3}
#
#
# def fun(**kwargs):
#     print(kwargs)


# fun(**d)  # 先将字典d中的键值对转换为单独的关键字实参，然后再将单独的关键字实参转换为可变的关键字形参，因为可变的关键字形参被初始化后是一个字典所以打印结果为
# # {'a': 1, 'b': 2, 'c': 3}
#
#
# def f1(a, b=5, *args, **kwargs):  # *args 接收位置可变的位置形参，并将其转换为元组， **kwargs 接收位置可变的关键字形参，并将其转换为字典。
#     print('a =', a, 'b =', b, 'args =', args, 'kwargs =', kwargs)
#
#
# f1(2, 6, 7, 8, c=9)  # a = 2 b = 6 args = (7, 8) kwargs = {'c': 9}
# f1(2)  # a = 2 b = 5 args = () kwargs = {}     args 可以接收0个或多个位置实参，kwargs 可以收到一个或者多个关键字实参。
#
#
# def f2(a, b=5, *, c, **kwargs):  # a 位置形参， b 关键字形参 * 后面全都是关键字形参，c 关键字形参, kwargs 个数可变的关键字形参
#     print('a =', a, 'b =', b, 'c =', c, 'kwargs =', kwargs)
#
#
# # *(3, 6) *表示将后面所有实参都转为位置实参， **{'c': 8, 'd': 10} **表示将后面所有的实参都转换为关键字实参
# f2(*(3, 6), **{'c': 8, 'd': 10})  # a = 3 b = 6 c = 8 kwargs = {'d': 10}


"""
    pass语句什么都不做，他只是一个占位符，用在语法上需要语句的地方：
1.if语句的条件执行体
2.for-in语句的循环体
3.定义函数时的函数体
"""

# age = 23
# if age > 18:
#     pass
#
# for i in range(8):
#     pass
#
#
# def f(ages, kwargs):
#     pass


"""
一、什么是文档字符串
    对于函数，模块，类或方法，位于其第一行的字符串被称为文档字符串，通常用三个引号表示
    文档字符串用于函数，模块。类或方法进行解释说明
    之所以被称为"文档"字符串，是因为可以使用工具根据文档字符串自动的生成文档。
    
    通过属性_doc_可以访问文档字符串、
    调用内置函数help（）得到的帮助信息中会包含文档字符串。
"""

# print(len.__doc__)  # a = 3 b = 6 c = 8 kwargs = {'d': 10}
#
# print(help(len))

"""
二、函数的文档字符串的常见内容和格式约定。
    1.第一行是简明扼要的总结
    2.第一行的首字母要大写，第一行要以句号结尾
    3.如果文档字符包含多行，串第二行是个空行，从第三行开始才是详细的描述。
    
    更多关于文档字符串的约定，可以参考  PEP 257:https://www.python.org/dev/peps/pep-0257/
"""

# def form_complex(real=0.0, imag=0.0):
#     """Form a complex number
#
#     keyword arguments
#     real -- the real part(default 0.0)
#     imag -- the imaginary part(default 0.0)
#     """
#     pass

"""
    函数的注解：
"""

# def f1(a: 'string type', b: 'int') -> 'join a with b':
#     return a + str(b)
#
#
# print(f1('hello', 123))
# # 通过调用属性__annotations__来查看函数的注解
# print(f1.__annotations__)  # {'a': 'string type', 'b': 'int', 'return': 'join a with b'}
# print(help(f1))  # f1(a: 'string type', b: 'int') -> 'join a with b'


"""
1.递归函数
    在一个函数的函数体内，可以调用其它函数
    如果在一个函数的函数体内调用了函数本身，该函数就是递归函数
    
    递归函数包含了一种隐式的循环，因此，递归函数必须有一个明确的递归结束条件，也成为递归出口。
    
    能用递归来解决的问题必须满足两个条件
    1.可以通过递归调用来缩小递归的规模，并且新问题与原问题有着相同的形式。
    2.存在一种简单情景，可以使递归在简单情境下退出，
    
    递归函数的优点是定义简单，逻辑清晰。
"""

"""
    使用递归计算阶乘
    n！= 1 * 2 * 3 ... * n = n (n -1)! * n ,且1！= 1
    如果通函数fac(n)表示n!,那么fac(c) = fac(n -1) * n = n * fac(n -1)

"""

# def fac(n):
#     if n == 1:
#         return 1
#     return n * fac(n - 1)
#
#
# print('fac(6) =', fac(6))  # fac(6) = 720
# print(fac(1))  # 1

"""
    使用递归计算斐波那切数列
    F0 = 0 ，F1 = 1, Fn = F(n - 1) + F(n - 2)(n >= 2),
    如果用函数fib(n)表示Fn,那么fib(n) = fib(n - 1) + fib(n - 2),
    且fib(0) = 0, fib(1) = 1
"""

# def fib(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return fib(n - 1) + fib(n - 2)  # fib(6) = fib(6-1)+fib(6-2)
#
#
# print(fib(6))


# def fib(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     print("fib" + str(n) + "= fib" + str(n-1) + "+" + "fib" + str(n-2))
#     return fib(n - 1) + fib(n - 2)
#
#
# print(fib(6))

"""
问题描述：
    据说印度的舍罕王打算重赏一个宰相，问他有什么要求：
    这位宰相说："陛下，请您在这张棋盘上的第一个格子内给我一粒麦子，在第二格格子内，赏给我两粒麦子，以此类推
    一直到这棋盘的64个格子满了以后。"舍罕王听了以后，认为这赏金微不足道，于是点头答应
    问：共需要赏赐给这位宰相多少麦子
"""

# def wheats(n):
#
#     a = 1
#     b = 1
#     for _ in range(2, n):
#         a *= 2
#         b += a
#     return b
#
#
# print(wheats(65))
#
# # 使用列表生成式一行代码解决问题~
# print(sum([2 ** i for i in range(64)]))

"""
    0-9之间可以组成多少个不同的三位数
    思路：设置初始值sums=1，设三位数的百位，十位，个位 分别为a,b,c
    a的序列为[1, 10],b的序列为[0,10],c的序列为[0, 10]
    三重循环下三个数亮亮不相等的为循环一次。 sums自增一
"""

# sums = 0
# for a in range(1, 10):
#     for b in range(10):
#         for c in range(10):
#             if a != b and b != c and c != a:
#                 sums += 1
# print(sums)  # 648
#
# sums = 0
#
# for a in range(1, 10):
#     for b in range(10):
#         if a == b:
#             continue
#         for c in range(10):
#             if b != c and c != a:
#                 sums += 1
#
# print(sums)  # 648

"""
角谷猜想：日本的脚骨提出了一个猜想，猜想的内容是：对于任意的自然数，反复进行如下运算：
    1.若为技术，则乘以三后加1
    2.若为偶数，则除以2
    总可以得到自然数1
    给出任意的自然数，验证角谷猜想
思路：通过循环反复进行角谷猜想的两种运算，当运算结果为1的时候则退出循环
"""

# def jiaogu(n):
#
#     nc = n
#     while nc != 1:
#         nc = nc * 3 + 1 if nc % 2 else nc / 2
# # if nc % 2 如果nc对2取余结果返回值为Ture，说明nc为奇数，因为nc对2取余后结果为1，所以返回ture
#     print(n)
#
#
# jiaogu(9)


# def jiaogu(n):
#     nc = n
#     while nc != 1:
#         if nc % 2:
#             nc = nc * 3 + 1
#         else:
#             nc = nc / 2
#     print(n)
#
# jiaogu(5)


# n = int(input('请输入一个整数：'))
#
# while n != 1:
#     if n % 2 == 0:
#         a = n / 2
#         print('%d / 2 = %d' % (n, a))
#         n = a
#     else:
#         b = n * 3 + 1
#         print('%d * 3 + 1 = %d' % (n, b))
#         n = b


# def jiaogu(n):
#     while n != 1:
#         if n % 2:
#             a = n * 3 + 1
#             print('%d * 3 + 1 = %d' % (n, a))
#             n = a
#         else:
#             b = n / 2
#             print('%d / 2 = % d' % (n, b))
#             n = b
#
#
# jiaogu(9)


"""
    鸡兔同笼：
    在同一个笼子里有若干只鸡和兔，上面数有h个头，下面数有f只脚
    求笼子里🐔和🐰的个数
    设计思路：
    设鸡和兔的只数分别为x,y
    x + y = h
    2x + 4y = f
    由方程1可知，x的取值范围为[1, h-1]，且 y = h -x
"""


# def chicken_rabbit(h, f):
#
#     for x in range(1, h):
#         y = h - x
#         if 2 * x + 4 * y == f:
#             print('鸡的个数：%d只，兔的个数：%d只' % (x, y))
#             return
#
#
# chicken_rabbit(35, 94)  # 鸡的个数：23只，兔的个数：12只


"""
    百钱买百鸡：
    用100文钱买100只鸡，其中公鸡5文钱一只，母鸡三文钱一只。小鸡一文钱三只
    求各买了多少级公鸡、母鸡和小鸡
    设计思路：
    x + y + z = 100
    4x + 3y + z/3 = 100
"""

# for x in range(20):
#     for y in range(33):
#         for z in range(0, 101, 3):
#             if x + y + z == 100 and 5 * x + 3 * y + z / 3 == 100:
#                 print('公鸡：%d只，母鸡：%d只，小鸡：%d只' % (x, y, z))
#
#
# for x in range(20):
#     for y in range(33):
#         z = 100 - x - y
#         if z >= 0 and z % 3 == 0 and 5 * x + 3 * y + z / 3 == 100:
#             print('公鸡：{}只，母鸡：{}只，小鸡：{}只'.format(x, y, z))


"""
    问题描述：
    张家，王家，李家各有三个孩子，
    一天，三家的九个孩子在一起比赛跑步，规定：
    跑第一名得9分，第二名8分，第三名7分.....跑低九名得一分
    
    比赛结果如下：
    1.各家三个孩子的总分相同
    2.第一名是李家的孩子，第二名是王家的孩子
    3.所有孩子的名次没有并列的
    4.各家三个孩子的名词都没有相连的。
    求：最后一名的孩子是谁家的。
    
    设计思路：
    由1可知各家三个孩子的总分都是:(1+2+3+4+5+6+7+8+9)/3=15
    
    由2可知：
    因为第一名是李家的孩子所以可以设李家孩子的分数分别为 9, x, 15- (9 + x)，即9, x, 6 - x
    其中x的取值范围是[1, 5]
    因为第二名是王家的孩子，所以可设王家的孩子分别为：8, y, 15 - (8 + y)，即 8, y, 7 - y
    其中y的趋势范围是[1, 6]
    
    由3和4可知：x - (6 - x) > 1, y - (7 - y) > 1

    通过循环穷举李家三个孩子的份数和王家三个孩子的分数，
    在穷举的过程中，定义一个列表存放所有名词对应的分数，
    每穷举一次李家三个孩子的分数，就把李家三个孩子的分数从列表中删除，
    每穷举一次王家三个孩子的分数，就把王家三个孩子的分数从列表中删除，
    列表中剩余的元素即为张家三个孩子的分数，从大到小分别为zhang[2], zhang[1], zhang[0]
    因为张家三个孩子的名词没有相连的，所以zhang[2] - zhang[1] > 1 and zhang[1] - zhang[0] > 1

"""


# def slowest_child():
#     """求：最后一名的孩子是谁家的。"""
#     # 通过循环穷举李家三个孩子的份数和王家三个孩子的分数，
#
#     # 因为第一名是李家的孩子所以可以设李家孩子的分数分别为
#     # 9, x, 15 - (9 + x)，即9, x, 6 - x
#     # 其中x的取值范围是[1, 5]
#     # 由3和4可知：x - (6 - x) > 1
#     for li in [[9, x, 6 - x] for x in range(1, 6) if x - (6 - x) > 1]:
#         # 在穷举的过程中，定义一个列表存放所有名词对应的分数
#         scores = list(range(1, 10))
#         # 每穷举一次李家三个孩子的分数，就把李家三个孩子的分数从列表中删除
#         for score in li:
#             scores.remove(score)
#         # 因为第二名是王家的孩子，所以可设王家的孩子分别为：8, y, 15 - (8 + y)，即
#         # 8, y, 7 - y
#         # 其中y的趋势范围是[1, 6]
#         # 由3和4可知：y - (7 - y) > 1
#         for wang in [[8, y, 7 - y] for y in scores if 7 - y in scores and y - (7 - y) > 1]:
#             for score in wang:
#                 scores.remove(score)
#             # 列表中剩余的元素即为张家三个孩子的分数，从大到小分别为zhang[2], zhang[1], zhang[0]
#             zhang = scores
#             # 因为张家三个孩子的名词没有相连的，所以zhang[2] - zhang[1] > 1 and zhang[1] - zhang[0] > 1
#             if zhang[2] - zhang[1] > 1 and zhang[1] - zhang[0] > 1:
#                 print('李家三个孩子的分数', li)
#                 print('王家三个孩子的分数', wang)
#                 print('张家三个孩子的分数', zhang)
#
#
# slowest_child()


# def slowest_child():
#     for li in [[x, 9, 6 - x] for x in range(1, 6) if x - (6 - x) > 1]:
#         scores = list(range(1, 10))
#         for score in li:
#             scores.remove(score)
#         for wang in [[y, 8, 7 - y] for y in scores if 7 - y in scores and y - (7 - y) > 1]:
#             for score in wang:
#                 scores.remove(score)
#             zhang = scores
#             if zhang[2] - zhang[1] > 1 and zhang[1] - zhang[0] > 1:
#                 print('李家三个孩子的分数', li)
#                 print('王家三个孩子的分数', wang)
#                 print('张家三个孩子的分数', zhang)
#
# slowest_child()

"""
    杨辉三角
    特点 第i行有i个数
    
    
    假设要打印n行，
    对于特点2，则有：
    L[i][0] = L[i][i] = 1 (i = 0, 1, 2, 3......, n-1)
    对于特点三，则有：
    当j != 0且 j != i时，L[i][j] = L[i - 1][j - 1] + L[i - 1][j]
    
    首先初始化一个所有元素都为1的n行二维列表，第i行有i个数：
    然后，根数上述特点三的条件和公式更新二维列表，对杨辉三角中部位1的位置进行更新
    最后根据杨辉三角的格式打印二维列表。
          先打印一定数量的水平制表符，第i行打印n - i 个
          打印每行的内容时除最后一个数之外，每打印一个数之后打印两个水平制表符
          对于每行的最后一个数，打印之后换行，准备打印下一行
"""


# L = [[1],
#      [1, 1],
#      [1, 2, 1],
#      [1, 3, 3, 1],
#      [1, 4, 6, 4, 1],
#      [1, 5, 10, 10, 5, 1],
#      [1, 6, 15, 20, 15, 6, 1],
#      [1, 7, 21, 45, 45, 21, 7, 1],
#      [1, 8, 28, 66, 90, 66, 28, 8, 1]
#      ]
# 初始化一个所有元素都为1的n行二维列表，第i行有i个数：
L = [[1 for j in range(i + 1)] for i in range(9)]

#  然后，根数上述特点三的条件和公式更新二维列表，对杨辉三角中部位1的位置进行更新
for i in range(2, 9):
    for j in range(i + 1):
        if j != 0 and j != i:
            # print(i, j)
            L[i][j] = L[i - 1][j - 1] + L[i - 1][j]
            print('L[%d][%d] = L[%d - 1][%d - 1] + L[%d - 1][%d]' % (i, j, i, j, i, j))
# 最后根据杨辉三角的格式打印二维列表
for i in range(9):
    # 先打印一定数量的水平制表符，第i行打印n - i 个
    print('\t' * (8 - i), end='')
    # 打印每行内容时
    for j in range(i + 1):
        # 出最后一个数之外
        if j != i:
            # 每打印一个数之后打印两个水平制表符
            print('%d\t\t' % L[i][j], end='')
        # 对于每行的最后一个数
        else:
            # 打印之后换行，准备打印下一行
            print('%d' % L[i][j])

# L = [[1],
#      [1, 1],
#      [1, 2, 1],
#      [1, 3, 3, 1],
#      [1, 4, 6, 4, 1],
#      [1, 5, 10, 10, 5, 1],
#      [1, 6, 15, 20, 15, 6, 1],
#      [1, 7, 21, 45, 45, 21, 7, 1],
#      [1, 8, 28, 66, 90, 66, 28, 8, 1]
#      ]


# def method(max):
#     # 入口:n控制行数，用列表lst代表当前行
#     n, lst = 0, [1]
#     while n < max:
#         # 返回当前行
#         yield lst
#         # 从上一行下标为2的元素开始，与前一项相加，一次替换列表元素
#         lst = [lst[i] + lst[i-1] for i in range(1, len(lst))]
#         # 每行第一个元素为1
#         lst.insert(0, 1)
#         # 每行最后一个元素为1
#         lst.append(1)
#         n += 1
#
#
# for n in method(5):
#     print(n)

"""
    谁在说谎：
    张三说李四在说谎，李四说王五在说谎，王五说张三和李四都在说慌
    思路：
    张三说李四在说谎：说明要么张三说的是真话，李四说的假话，要么李四说的是真话，张三说的是假话
    李四说王五在说谎：说明要么李四说的是真话，王五说的假话，要么王五说的是真话，李四说的是假话
    王五说张三和李四都在说慌：说明要么王五说的是真话，张三和李四说的都是假话，要么王五说的是假话,张三和李四至少有一个说的是真话。
"""
a = [True, False]
for zhangsan in a:
    for lisi in a:
        for wangwu in a:
            if zhangsan == (not lisi) and lisi == (not wangwu) and wangwu == ((not zhangsan) and (not lisi)):
                print('zhangsan =', zhangsan, 'lisi =', lisi, 'wangwu =', wangwu)

                print('张三 = {zhang} , 李四 = {li} , 王五 = {wang}'.format(zhang='真话' if zhangsan == True else '假话',
                                                           li='真话' if lisi == True else '假话',
                                                           wang='真话' if wangwu == True else '假话'))

"""
问题描述：
    猴子第一天摘下若干个桃子，当即吃了一半，觉得不过瘾，又多吃了一个
    第二天将第一天剩下的桃子吃了一半，又多吃了一个
    以后每天早上都吃了前一天剩下的一半后又多吃了一个。
    到了第十天的时候，发现只剩下一个桃子了
    求猴子第一天摘了多少桃子。
    设计思路一：递推
            第一天的桃子数是第二天的桃子数加一后乘以2，第二天的桃子数是第三天的桃子数加一后的二倍
            ...一般的，第n天的桃子数是第n+1天的桃子数加一后的2倍
            设第n天的桃子数是L(n)，则有递推关系L(n)=(L(n+1)+1)*2,且初始条件为L(10)=1。
            根据地推关系和初始条件，L(10) --> L(9) --> L(8) -->.....--> L(1)。
"""


def monkey_peach1():
    """求猴子第一天摘了多少桃子。"""
    L = [None] * 11
    # 初始条件为L[10]=1
    L[10] = 1

    # 设第n天的桃子数是L(n)，则有递推关系L(n) = (L(n + 1) + 1) * 2, 且初始条件为L(10) = 1。
    # 根据地推关系和初始条件，L(10) --> L(9) --> L(8) -->..... --> L(1)。
    for n in range(9, 0, -1):
        L[n] = (L[n + 1] + 1) * 2

    return L[1]

print('猴子第一天摘了%d个桃子' % monkey_peach1())

"""
设计思路二：递归
    设计思路一递推关系可看做在一个函数体的内部有调用了该函数，
    设计思路一的初始条件可以看做递归结束条件（递归出口）

"""


def monkey_peach2(day):
    """求猴子第一天摘了多少桃子。"""
    # 递归结束条件（递归出口）：L(10)=1
    if day == 10:
        return 1
    else:
        # 递推关系L(n) = (L(n + 1) + 1) * 2可看做在一个函数体的内部又调用了该函数。
        return (monkey_peach2(day + 1) + 1) * 2


monkey_peach2(1)
print('猴子第一天摘了%d个桃子' % monkey_peach2(1))





















