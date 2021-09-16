# 全局变量
num = 10


def demo1():

    # 希望修改全局变量的值；
    # 在python中不允许在函数内部直接修改全局变量的值；
    # 如果使用赋值语句，只会在函数内部定义一个局部变量。
    num = 99

    print("demo1  ====> %d" % num)


def demo2():

    print("demo2  ====> %d" % num)


demo1()
demo2()






