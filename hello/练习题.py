# 打印99乘法表
for i in range(1, 10):
    for a in range(1, i + 1):
        print(a, '*', i, '=', i * a, end=' ')
    print('')

a = 1
while a < 10:
    i = 1
    while i < a + 1:
        print(a, '*', i, '=', a * i, end=' ')
        i += 1
    a += 1
    print('')

# 冒泡排序

def maopao(a):

    n = len(a)

    for i in range(n):
        for j in range(0, n - i - 1):

            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]


a = [1, 4, 5, 6, 8, 9, 3, 2, 7]

maopao(a)

for i in range(len(a)):
    print("%d" % a[i])
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :CH_Test
# @File     :tuzi
# @Date     :2021/9/29 23:41
# @Author   :Stark
# @Email    :274808208@qq.com
# @Software :PyCharm
-------------------------------------------------
"""
# 一个兔子从第四年开始每年可以生一只兔子，20年后一共有多少只兔子？

def shengtuzi(nian,longzi):

    for i in range(nian):

        for j in range(len(longzi)):

            longzi[j] += 1

            if longzi[j] >= 4:
                longzi.append(0)
    return longzi

longzi = [0]
nian = 4
longzi = shengtuzi(nian, longzi)
print(longzi)
print(len(longzi))



# 一个兔子从第四年开始每年可以生一只兔子，20年后一共有多少只兔子？
def shengtuzi(nian,longzi):
    for i in range(nian):  # 年份循环
        for j in range(len(longzi)):  # 遍历笼子中的兔子
            longzi[j] += 1  # 兔子年龄加1
            if longzi[j] >= 4:  # 判断兔子年龄是否大于等于4，满足条件则笼子里加入一只年龄为0的小兔子
                longzi.append(0)
    return(longzi)

longzi = [0]  # 装兔子的笼子，数值代表每只兔子的年龄
nian = 20  # 需要计算的年份
longzi = shengtuzi(nian, longzi)
print(longzi)
print(len(longzi))















