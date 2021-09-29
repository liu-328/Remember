class A:

    def __init__(self):

        self.num1 = 100
        self.__num2 = 200

    def test(self):

        print("公有方法")

    def __test(self):

        print("私有方法")


class B(A):

    def demo(self):

        # 1.在子类对象方法中，不能直接调用父类的私有属性
        # print(self.__num1)
        # 2.在子类对象方法中，不能直接调用父类的私有方法
        # self.__test
        pass


b = B()
print(b)

#  再外界不能访问对象的私有属性/私有方法
# print(b.__num2)
# b.__tset()





















