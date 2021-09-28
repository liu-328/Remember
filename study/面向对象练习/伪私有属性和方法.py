class Women:

    def __init__(self, name):

        self.name = name
        self.__age = 18

    def __secret(self):

        # 在对象的方法内部，是可以访问对象的私有属性的
        print("%s 的年龄是 %d" % (self.name, self.__age))


xiaomei = Women("小美")
# 伪私有属性
print(xiaomei._Women__age)
# 伪私有方法
xiaomei._Women__secret()
# 在python中并没有真正意义的私有，在给属性和方法命名时，实际就是对名称做了一些特殊处理，使外界无法获取到。



















