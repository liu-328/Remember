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
# print(a)  # {'name': 'jack', 'age': 18, 'gender': '男', 'class': 1, 'score': 90, 'aaa': 'bbb', 'ccc': 'ddd', 'aaac': 1, 'bbbc': 2}

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

a = {1, 3, 4, 6}
b = {3, 4, 1, 6}
print(a == b)  # True
print(a != b)  # False

"""
判断一个集合是否是另一个集合的子集
    调用方法issubset进行判读
"""

a = {1, 3, 5, 7, 9, 11, 13}
b = {1, 3, 4, 6, 7, 0}
c = {1, 3, 5, 7, 9, 11}

print(a.issubset(b))  # False  判断a是否是b的子集
print(c.issubset(a))  # True   判断c是否是a的子集
print(b.issubset(c))  # False  判断b是否是c的子集

# import time      时间戳

# a = time.time()
# print("当前的时间戳为 %.f" % a)

"""
    如何判断一个集合是否是另一个集合的超集
    调用方法issuperset进行判断
"""

print(a.issuperset(c))  # True
print(b.issuperset(c))  # True
print(c.issuperset(a))  # False

"""
    如何判断两个集合是否没有交集
    调用方法isdisjoint
"""

a = {1, 3, 5, 7, 9}
b = {2, 3, 6, 8, 10}
c = {2, 4, 6, 8, 10}

print(a.isdisjoint(b))  # False
print(a.isdisjoint(c))  # True
print(b.isdisjoint(c))  # False

"""
两个集合的交集
调用方法intersection来查看两个集合的交集
使用 ' & ' 也可以查看两个集合的交集
使用两个方法 集合本身不发生变化

"""

a = {1, 3, 5, 6, 7}
b = {1, 4, 7, 3, 9}
print(a.intersection(b))  # {1, 3, 7}
print(a & b)  # {1, 3, 7}
print(a)  # {1, 3, 5, 6, 7}
print(b)  # {1, 3, 4, 7, 9}

"""
a.intersection_update(b)的执行结果
    使用 a.intersection(b)返回值更新a，  b不变
    方法intersection_update的返回值为None
"""

# print(a.intersection_update(b))  # None
# print(a)  # {1, 3, 7}
# print(b)  # {1, 3, 4, 7, 9}

print(b.intersection_update(a))
print(a)  # {1, 3, 5, 6, 7}
print(b)  # {1, 3, 7}

"""
两个集合的并集
调用方法union来查看两个集合的并集
使用 ' | ' 也可以查看两个集合的并集
不存在方法union_update
且两个集合不发生变化
"""
a = {1, 3, 5, 6, 7}
b = {1, 4, 7, 3, 9}
print(a.union(b))  # {1, 3, 4, 5, 6, 7, 9}
print(a | b)  # {1, 3, 4, 5, 6, 7, 9}
print(a)
print(b)


"""
两个集合的差集
调用方法difference来查看两个集合的差集
使用 ' - ' 也可以查看两个集合的交集
做差级操作后生成一个新的集合，做差级操作的两个集合不变
"""
a = {1, 3, 5, 6, 7}
b = {1, 4, 7, 3, 9}
print(a.difference(b))  # {5, 6}
print(b.difference(a))  # {9, 4}

print(a - b)  # {5, 6}
print(a)
print(b)

"""
difference_update
a.difference_update(b)的返回值为None
a集合生成了一个新的集合
b集合不变
"""
print(a.difference_update(b))  # None
print(a)  # {5, 6}
print(b)  # {1, 3, 4, 7, 9}

"""
两个集合的对称差集
两个集合的并集去除两个集合的差集为两个集合的对称差集
调用方法symmetric_difference来查看两个集合的差集
使用 ' ^ ' 也可以查看两个集合的交集
使用对称差集操作后生成一个新的集合，做对称差集的两个集合不变
"""

a = {1, 3, 5, 6, 7}
b = {1, 4, 7, 3, 9}

print(a.symmetric_difference(b))  # {4, 5, 6, 9}
print(a ^ b)  # {4, 5, 6, 9}
print(a)  # {1, 3, 5, 6, 7}
print(b)  # {1, 3, 4, 7, 9}

"""
a.symmetric_difference_update(b)的返回值为None
a集合生成了一个新的集合
b集合不变
"""
print(a.symmetric_difference_update(b))  # None
print(a)  # {4, 5, 6, 9}
print(b)  # {1, 3, 4, 7, 9}

"""
集合的查操作；
可以使用运算符in检查集合中是否存在指定的元素，或者使用not in来检查集合中是否不存在指定的元素
"""

a = {3, 4, 5, 6, 7}
print(5 in a)  # True
print(8 in a)  # False

print(5 not in a)  # False
print(8 not in a)  # False

"""
集合的增操作
如果想要往集合里面添加元素，常见的方式有两种；
1.调用方法add,      一次添加一个元素。如果集合内存在指定的元素，则不会被添加  
2.调用方法update:   一次至少添加一个元素。如果集合内存在指定的元素，则不会被添加  
"""

a = {1, 2, 3, 5, 6}
a.add(7)
print(a)  # {1, 2, 3, 5, 6, 7}

a = {1, 2, 3, 5, 6}
a.update({4, 7})  # {1, 2, 3, 4, 5, 6, 7}
print(a)

a.update([4, 7])
print(a)  # {1, 2, 3, 4, 5, 6, 7}

a.update((4, 7))
print(a)  # {1, 2, 3, 4, 5, 6, 7}

"""
集合的删操作
1.调用方法remove    如果想要删除的元素不存在，则报错KeyError    一次只删除一个元素
2.调用方法discard   如果想要删除的元素不存在，不会报KeyError    一次只删除一个元素
3.调用方法pop       该方法返回被删除的元素，一次只删除一个任意的元素
4.调用方法clear     该方法用来清空集合
"""

a = {3, 4, 5, 6, 7}
a.remove(5)
print(a)  # {3, 4, 6, 7}

a = {3, 4, 5, 6, 7}
a.discard(5)
print(a)  # {3, 4, 6, 7}

a.discard(8)
print(a)  # {3, 4, 6, 7}

a = {3, 4, 5, 6, 7}
print(a.pop())  # 3
print(a)  # {4, 5, 6, 7}

a = {3, 4, 5, 6, 7}
a.clear()
print(a)  # set()

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

print(frozenset())  # frozenset()

print(frozenset(range(1, 6)))  # frozenset()

print(frozenset([1, 3, 5, 6]))  # frozenset()

print(frozenset((1, 3, 5)))  # frozenset({1, 3, 5})

print(frozenset("35926"))  # frozenset({1, 3, 5})

print(frozenset({3, 5, 9, 2, 6}))  # frozenset({1, 3, 5})

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
# print(a)  # {'name': 'jack', 'age': 18, 'gender': '男', 'class': 1, 'score': 90, 'aaa': 'bbb', 'ccc': 'ddd', 'aaac': 1, 'bbbc': 2}

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

a = {1, 3, 4, 6}
b = {3, 4, 1, 6}
print(a == b)  # True
print(a != b)  # False

"""
判断一个集合是否是另一个集合的子集
    调用方法issubset进行判读
"""

a = {1, 3, 5, 7, 9, 11, 13}
b = {1, 3, 4, 6, 7, 0}
c = {1, 3, 5, 7, 9, 11}

print(a.issubset(b))  # False  判断a是否是b的子集
print(c.issubset(a))  # True   判断c是否是a的子集
print(b.issubset(c))  # False  判断b是否是c的子集

# import time      时间戳

# a = time.time()
# print("当前的时间戳为 %.f" % a)

"""
    如何判断一个集合是否是另一个集合的超集
    调用方法issuperset进行判断
"""

print(a.issuperset(c))  # True
print(b.issuperset(c))  # True
print(c.issuperset(a))  # False

"""
    如何判断两个集合是否没有交集
    调用方法isdisjoint
"""

a = {1, 3, 5, 7, 9}
b = {2, 3, 6, 8, 10}
c = {2, 4, 6, 8, 10}

print(a.isdisjoint(b))  # False
print(a.isdisjoint(c))  # True
print(b.isdisjoint(c))  # False

"""
两个集合的交集
调用方法intersection来查看两个集合的交集
使用 ' & ' 也可以查看两个集合的交集
使用两个方法 集合本身不发生变化

"""

a = {1, 3, 5, 6, 7}
b = {1, 4, 7, 3, 9}
print(a.intersection(b))  # {1, 3, 7}
print(a & b)  # {1, 3, 7}
print(a)  # {1, 3, 5, 6, 7}
print(b)  # {1, 3, 4, 7, 9}

"""
a.intersection_update(b)的执行结果
    使用 a.intersection(b)返回值更新a，  b不变
    方法intersection_update的返回值为None
"""

# print(a.intersection_update(b))  # None
# print(a)  # {1, 3, 7}
# print(b)  # {1, 3, 4, 7, 9}

print(b.intersection_update(a))
print(a)  # {1, 3, 5, 6, 7}
print(b)  # {1, 3, 7}

"""
两个集合的并集
调用方法union来查看两个集合的并集
使用 ' | ' 也可以查看两个集合的并集
不存在方法union_update
且两个集合不发生变化
"""
a = {1, 3, 5, 6, 7}
b = {1, 4, 7, 3, 9}
print(a.union(b))  # {1, 3, 4, 5, 6, 7, 9}
print(a | b)  # {1, 3, 4, 5, 6, 7, 9}
print(a)
print(b)

"""
两个集合的差集
调用方法difference来查看两个集合的差集
使用 ' - ' 也可以查看两个集合的交集
做差级操作后生成一个新的集合，做差级操作的两个集合不变
"""
a = {1, 3, 5, 6, 7}
b = {1, 4, 7, 3, 9}
print(a.difference(b))  # {5, 6}
print(b.difference(a))  # {9, 4}

print(a - b)  # {5, 6}
print(a)
print(b)

"""
difference_update
a.difference_update(b)的返回值为None
a集合生成了一个新的集合
b集合不变
"""
print(a.difference_update(b))  # None
print(a)  # {5, 6}
print(b)  # {1, 3, 4, 7, 9}

"""
两个集合的对称差集
两个集合的并集去除两个集合的差集为两个集合的对称差集
调用方法symmetric_difference来查看两个集合的差集
使用 ' ^ ' 也可以查看两个集合的交集
使用对称差集操作后生成一个新的集合，做对称差集的两个集合不变
"""

a = {1, 3, 5, 6, 7}
b = {1, 4, 7, 3, 9}

print(a.symmetric_difference(b))  # {4, 5, 6, 9}
print(a ^ b)  # {4, 5, 6, 9}
print(a)  # {1, 3, 5, 6, 7}
print(b)  # {1, 3, 4, 7, 9}

"""
a.symmetric_difference_update(b)的返回值为None
a集合生成了一个新的集合
b集合不变
"""
print(a.symmetric_difference_update(b))  # None
print(a)  # {4, 5, 6, 9}
print(b)  # {1, 3, 4, 7, 9}

"""
集合的查操作；
可以使用运算符in检查集合中是否存在指定的元素，或者使用not in来检查集合中是否不存在指定的元素
"""

a = {3, 4, 5, 6, 7}
print(5 in a)  # True
print(8 in a)  # False

print(5 not in a)  # False
print(8 not in a)  # False

"""
集合的增操作
如果想要往集合里面添加元素，常见的方式有两种；
1.调用方法add,      一次添加一个元素。如果集合内存在指定的元素，则不会被添加  
2.调用方法update:   一次至少添加一个元素。如果集合内存在指定的元素，则不会被添加  
"""

a = {1, 2, 3, 5, 6}
a.add(7)
print(a)  # {1, 2, 3, 5, 6, 7}

a = {1, 2, 3, 5, 6}
a.update({4, 7})  # {1, 2, 3, 4, 5, 6, 7}
print(a)

a.update([4, 7])
print(a)  # {1, 2, 3, 4, 5, 6, 7}

a.update((4, 7))
print(a)  # {1, 2, 3, 4, 5, 6, 7}

"""
集合的删操作
1.调用方法remove    如果想要删除的元素不存在，则报错KeyError    一次只删除一个元素
2.调用方法discard   如果想要删除的元素不存在，不会报KeyError    一次只删除一个元素
3.调用方法pop       该方法返回被删除的元素，一次只删除一个任意的元素
4.调用方法clear     该方法用来清空集合
"""

a = {3, 4, 5, 6, 7}
a.remove(5)
print(a)  # {3, 4, 6, 7}

a = {3, 4, 5, 6, 7}
a.discard(5)
print(a)  # {3, 4, 6, 7}

a.discard(8)
print(a)  # {3, 4, 6, 7}

a = {3, 4, 5, 6, 7}
print(a.pop())  # 3
print(a)  # {4, 5, 6, 7}

a = {3, 4, 5, 6, 7}
a.clear()
print(a)  # set()

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

print(frozenset())  # frozenset()

print(frozenset(range(1, 6)))  # frozenset()

print(frozenset([1, 3, 5, 6]))  # frozenset()

print(frozenset((1, 3, 5)))  # frozenset({1, 3, 5})

print(frozenset("35926"))  # frozenset({1, 3, 5})

print(frozenset({3, 5, 9, 2, 6}))  # frozenset({1, 3, 5})

# 在程序中尽量使用不可变类型的对象，一旦创建不可变类型的对象，所有数据不会被修改，就不会导致修改数据产生的错误
# 在多任务环境下，同时操作对象时，不需要加锁。

"""
流程控制的概述
任何简单或者复杂的算法，都可以由：顺序结构，选择结构和循环结构三种节本结构组合而成
顺序结构   指的是程序从上到下顺序的执行代码。中间没有任何判断和跳转，直到程序结束
选择结构   if语句          程序根据判断条件的布尔值，选择执行部分代码
循环结构   while和for      程序根据循环条件反复执行某段代码，知道不满足循环条件为止。
"""














