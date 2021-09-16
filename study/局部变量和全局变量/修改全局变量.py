# 全局变量
num = 10


def demo1():

    # 希望修改全局变量 - 使用global 声明一下即可。
    # global 关键字会告诉解释器，后面的变量是一个全局变量。
    # 再使用赋值语句之后，就不会创建局部变量。

    print("demo1  ====> %d" % num)


def demo2():

    global num
    num = 99
    print("demo2  ====> %d" % num)


def demo3():

    print("demo3  ====> %d" % num)


demo1()
demo2()
demo3()





