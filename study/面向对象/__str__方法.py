class Cat:

    def __init__(self, new_name):

        self.name = new_name

        print("%s 来了" % self.name)

    def __del__(self):

        print("%s 走了" % self.name)

    def __str__(self):

        # 如果希望print输出对象的时候输入一个自己想要的内容，需要使用__str__方法，自定义一个返回值
        # 必须返回一个字符串
        return "我是小猫[{}]".format(self.name)


# tom是一个全局变量
tom = Cat("tom")

print(tom)




