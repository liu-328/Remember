# 1、用print函数打印多个值
from math import ceil
import random

a = 1
b = 2
print(a, b)

# 2、用print函数不换行打印
print('hello world', end='---')
print('hello hello')

"""
3、导入模块的方式有哪些
import os
from time import sleep
from turtle import *
"""

"""
4、python有哪六种数据类型？不可变数据类型有哪些？可变数据类型有哪些？
list tuple dict set number(int, float, ) str 
不可变：number str tuple 
当该数据类型的对应变量的值发生了改变，对应的内存地址也会发生改变
可变：dict set list
当该数据类型的对应变量的值发生了改变，对应的内存地址不会发生改变
"""
# 为什么是不可变类型
a = 1
print(id(a), type(a))
a = 2
print(id(a), type(a))

b = 'hello'
print(id(b), type(b))
b = 'hi'
print(id(b), type(b))

c1 = [1, 2, 3]
c = ('hello', c1)
print(id(c), type(c))
c1[1] = 3
print(id(c), type(c))

# 为什么是可变类型
d = {'name': '小刘'}
print(id(d), type(d))
d['name'] = '小张'
print(id(d), type(d))

e = {1, 2, 3}
print(id(e), type(e))
e.remove(3)
print(id(e), type(e))

f = [1, 2, 3]
print(id(f), type(f))
f[0] = 4
print(id(f), type(f))

"""
6、判断变量类型有哪些方式，分别可以用哪些函数？
type()
"""

"""
7、分别对49.698作如下打印
    1）四舍五入，保留两位小数
    2）向上入取整
    3）向下舍取整
    4）计算8除以5返回整型
    5）求4的2次幂
    6）返回一个（1,100）随机整数
"""
print('%.2f' % 49.689)
print(round(49.698, 2))
print(ceil(49.698))
print(int(49.1))
print(8//5)
print(4**2)
print(random.randint(1, 100))

"""
8、依次对变量a,b,c赋值为1,2,3
"""

a, b, c = 1, 2, 3

"""
9、截取某字符串中从2索引位置到最后的字符子串
"""
string = 'hello world'
print(string[2:])

"""
10、对字符串“testcode”做如下处理：
    1）翻转字符串
    2）首字母大写
    3）查找是否包含code子串，并返回索引值
    4）判断字符串的长度
    5）从头部截取4个长度字符串
    6）把code替换为123
    7）把“test code”字符串中的两个单词转换为列表中的元素，并打印处理
    8）把['test','code']把list变量中的元素连接起来
"""
str1 = 'testcode'
print(str1[::-1])
print(str1.capitalize())
print(str1.index('code'))
print(str1.find('code'))
print(len(str1))
print(str1[0:4])
print(str1.replace('code', '123'))
str2 = 'test code'
print(str2.split())
str3 = ['test', 'code']
print(''.join(str3))

"""
11、如何打印出字符串“test\ncode”
"""
print(r'test\ncode')

"""
12、如何创建一个空元组
"""
tup = ()
print(type(tup))

"""
13、创建一个只包含元素1的元组，并打印出该变量的类型
"""
tup1 = (1,)
print(type(tup1))

"""
14、元组中元素可以修改？如何更新元组中的元素？
不可以修改 
"""
aa = (1, 2)
bb = (3, 4)
print(aa + bb)

"""
15、对元组（1,2,3,4,5)做如下操作：
    1）取倒数第二个元素
    2）截取前三个元组元素
    3）依次打印出元组中所有元素
"""
tup3 = (1, 2, 3, 4, 5)
print(tup3[-2])
print(tup3[0:3])
for i in tup3:
    print(i)

"""
16、把元组(1,2,3,4,5,6)元素格式化成字符串
"""

tup4 = (1, 2, 3, 4, 5, 6)
print("{}".format(tup4))

