"""
1.写函数，接收两个数字参数，返回最大值
例如：
传入：10,20
返回：20
"""


def fun1(min_number, max_number):

    print(max(max_number, min_number))


fun1(10, 20)

"""
2.写函数，获取传入列表的所有奇数位索引对应的元素，并将其作为新列表返回。
例如：
传入：[34,23,52,352,352,3523,5]
返回：[23,352,3523]
"""


def fun2(list1):

    for i in list1:
        if i % 2 == 0:
            list1.remove(i)
    print(list1)


fun2([34, 23, 52, 352, 352, 3523, 5])

"""
3.写函数，判断用户传入的对象（列表）长度是否大于5，如果大于5，那么仅保留前五个长度的内容并返回。不大于5返回本身。
例如：
传入1：[34,23,52,352,666,3523,5]   	返回1：[34,23,52,352,666]
传入2：[34,23,52]     
"""


def fun3(list3):

    if len(list3) > 5:
        list4 = list3[:5]
        print(list4)
    else:
        print(list3)


fun3([34, 23, 52, 352, 666, 3523, 5])
fun3([34, 23, 52])

"""
4.写函数，检查传入的字符串是否含有空字符串，返回结果，包含空字符串返回True，不包含返回False
例如：
传入："hello world"
返回：True
"""


def fun4(str1):

    a = []
    b = []
    for i in str1:
        if i.isspace():
            a.append(i)
        else:
            b.append(i)
    if len(a) == 1:
        return True
    else:
        if len(b) < len(str1):
            return False


print(fun4("hello world"))

"""
5.写函数，接收n个数字，求这些数字的和
"""


def fun5(*args):

    c = 0
    for cc in args:
        c += cc
    print(c)


fun5(1, 2, 5, 3)

"""
6.定义一个函数,实现两个数四则运算,要注意有3个参数,分别是运算符和两个运算的数字.
例如：
传入：10,*,20
返回：200
"""


def fun6(*args):

    str(args)
    aa = str(args[0]) + str(args[1]) + str(args[2])

    print(eval(aa))


fun6(10, '/', 20)
print(4.8+2.8+22.9)

"""
名片管理系统
"""
import task_package

while True:

    task_package.Interface()
    user = input("请输入想要执行的操作:")
    print("用户执行的操作", user)

    if user in ['0', '1', '2', '3', '4', 'exit']:

        if user == "0":

            task_package.see_message()

        elif user == "1":

            task_package.add_message()

        elif user == "2":

            task_package.remover_message()

        elif user == "3":

            task_package.change_message()

        elif user == "4":

            task_package.look_a_message()

    elif user == 'exit':

        print('进程结束')
        break

    else:

        print('输入错误请重新输入：')
