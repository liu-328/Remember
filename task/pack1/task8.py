"""
一、定义名为MyTime的类，其中应有三个实例变量 时hour 分minute 秒second
1）为了给对象初始化赋值，编写构造方法，对时分秒附初始值
2）为了保证数据的安全性，这三个成员变量应声明为私有、
3）对三个属性分别定义封装get和set方法，定义一个main方法，创建一个MyTime类的对象并调用这六个方法。
"""


class MyTime:

    def __init__(self, __hour, __minute, __second):
        self.hour = __hour
        self.minute = __minute
        self.second = __second
        print(__hour, __minute, __second)

    def get(self):
        pass

    def set(self):
        pass

    def __main__(self):
        pass


user1 = MyTime(1, 1, 1)
user1.get()

