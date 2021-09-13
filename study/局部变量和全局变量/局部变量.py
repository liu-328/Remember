def demo1():

    # 定义一个局部变量
    # 1> 出生：执行了下方的代码才会被创建。
    # 2> 死亡：函数执行完成之后。
    num = 10
    print("在demo1函数内部的变量是: ", num)


def demo2():

    # 在函数内容定义的变量，不能在其他函数内使用
    # print(num)
    pass


demo1()
demo2()




















