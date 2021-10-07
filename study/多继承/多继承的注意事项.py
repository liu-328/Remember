class A:

    def test(self):

        print("A.test方法")

    def demo(self):

        print("A.demo方法")


class B:

    def tset(self):

        print("B.test方法")

    def demo(self):

        print("B.demo方法")


class C(B, A):

    pass


c = C()
# 不同的父类对象中存在同名的方法时，应避免使用多继承
c.test()
c.demo()

print(C.__mro__)

b = B()
# 使用dir函数来查看b对象中包含哪些内置属性和方法。
print(dir(b))












