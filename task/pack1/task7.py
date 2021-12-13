"""
1、封装读取某个文件，读取指定长度内容，并返回读取的内容
"""


def file(file_name):

    # 打开
    file = open(file_name)
    test = file.read(5)
    print(test)
    file.close()


if __name__ == '__main__':
    file("readme.txt")

"""
2、封装函数读取某个文件的所有行的内容，并把每行的内容作为列表返回
"""


def return_lsit():

    with open('/Users/liushijia/Documents/git/Remember/task/pack1/readme.txt','r') as file:
        file1 = file.readlines()
        print(file1)


if __name__ == '__main__':
    return_lsit()
"""
3、封装操作追加内容写入文件的函数
"""


def w_file():

    with open('/Users/liushijia/Documents/git/Remember/task/pack1/readme.txt', 'r+', encoding='utf-8') as files:
        files.write('hello1\nhello2')


if __name__ == '__main__':
    w_file()


