class A:

    def __init__(self):

        self.num1 = 100
        self.__num2 = 200

    def __test(self):

        print("私有方法")

    def test(self):

        print("公有方法")
        print(self.num1)
        self.__test()


class B(A):

    def demo(self):

        # 1.在子类对象方法中，不能直接调用父类的私有属性
        # print(self.__num1)
        # 2.在子类对象方法中，不能直接调用父类的私有方法
        # self.__test
        # 3.访问父类的公有属性和公有方法
        print(self.num1)
        self.test()
        pass


b = B()
print(b)

# 在外界访问父类的共有属性或调用父类的公有方法
# print(b.num1)
# b.test()
#  再外界不能访问对象的私有属性/私有方法
# print(b.__num2)
# b.__tset()
b.demo()


# 验证通过类调用对象内部的方法获取对象内部的私有属性。
class Q:

    def __init__(self):

        self.a = 1
        self.__a = 2

    def tt(self):

        print("共有属性")
        print(self.__a)
        self.__tt()

    def __tt(self):

        print("私有属性")


class W:

    def h(self, name):

        print(type(name))


q = Q()
w = W()

w.h(q.tt())












