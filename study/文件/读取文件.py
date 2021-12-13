# -*- coding: utf-8 -*-

# 1.打开文件
# 文件编码 encoding="utf-8"
file = open("readme", encoding="utf-8")

# 2.读取文件内容
# read方法在默认的情况下返回文件的所有内容
# read()内添加数字表示读取一个单位的长度
test = file.read(1)
print(test)
#
# # 3.关闭文件
file.close()


# 分行读取文件
def read_1():
    with open('readme', 'r') as file:

        # 读取文件内的所有内容以列表的形式返回
        a = file.readlines()
        print(a)


read_1()


with open('readme', 'rb+') as file1:

    # 显示当前指针位置
    print(file1.tell())
    a = file1.read(2)
    print('a', a)
    # 指针偏移1个字节
    # 必须要以二进制的方式打开文件，否则会报错，
    # 第一个参数表示要移动的字节数，第二个参数表示开始移动字节的参考位置
    # 0为文件开头，1为当前位置，2为文件末尾
    file1.seek(1, 1)
    b = file1.readline(2)
    print('b', b)
    # 打印文件的访问模式，和文件名称，返回文件是否被关闭
    print(file1.mode, file1.name, file1.closed)
    # 读取下一行
    for index in range(3):
        line = next(file1)
        print(f'第{index}行', line)

