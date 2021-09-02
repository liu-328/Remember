# row = 1
# while row <= 5:
#     lie = 1
#     while lie <= row:
#         print('*', end='')
#         lie += 1
#
#     print('第%d行' % row)
#     row += 1
#
# row = 1
# while row <= 9:
#     lie = 1
#     while lie <= row:
#         print(lie, "*", row, "=", row * lie, end='  ')
#         lie += 1
#     print('')
#     row += 1

# for i in range(1, 10):
#     for j in range(1, i+1):
#         result = j * i
#         print("%d×%d=%d" % (j, i, result), end=' ')
#     print()

# for a in range(1, 10):
#     for b in range(1, a + 1):
#         # if b <= a:
#             print(b, a)
#             # print("%d*%d=%d\t" % (b, a, a * b), end="")
#     print("")
#
#
# name = '小明'


# def say_hello():
#     """哈哈哈"""
#
#     print('hello 1')
#     print('hello 2')
#     print('hello 3')
#
#
# print(name)
# # 只有调用了函数，函数才会主动执行。
# say_hello()
#
# print(name)


# 函数的参数和返回值

def sum_2_num(num1, num2):
    """对两个数字的求和"""

    result = num1 + num2
    # 可以使用return的返回值，告诉调用函数的一方的计算结果
    return result
    # 注意：return表示返回，下方的代码不会被执行到。
    # num = 1000


sum_result = sum_2_num(1, 1)
print('计算结果：%d' % sum_result)


def test1():

    print(1)


def test2():

    print(2)

    test1()


test2()


def test3():

    print(3)
    test1()
    test2()


test3()
# 2 1 3 1 2 1


def print_line(char, times):
    """打印单行分割线

    :param char:分隔字符
    :param times:分割次数
    """
    print(char * times)


def print_lines(char, times):
    """打印多行分割线

    :param char:分割线使用的分隔字符
    :param times:分割线重复次数
    """
    row = 1
    while row < 6:

        print_line(char, times)
        row += 1


print_lines('-', 20)


def lines(chars, number):

    row = 0
    while row < 5:
        print(chars * number)
        row += 1


lines('-', 10)






