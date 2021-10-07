def demo1():
    return int(input("输入整数："))


def demo2():
    return demo1()


# 当某个函数或者方法执行出现异常，都会传递到调用函数或者方法的一方
# 如果想要捕获异常可以在调用函数/方法的位置捕获异常。
try:
    print(demo2())

except Exception as result:
    print("未知错误 %s" % result)












