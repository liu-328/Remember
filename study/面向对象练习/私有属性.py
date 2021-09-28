class Women:

    def __init__(self, name):

        self.name = name
        self.__age = 18

    def __secret(self):

        # 在对象的方法内部，是可以访问对象的私有属性的
        print("%s 的年龄是 %d" % (self.name, self.__age))


xiaomei = Women("小美")
# 私有属性不能被外界直接访问
# print(xiaomei.__age)
# 私有方法不能被外界直接访问
# xiaomei.__secret()


























