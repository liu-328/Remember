class Dog(object):

    def __init__(self, name):

        self.name = name

    def game(self):

        print("%s蹦蹦跳跳" % self.name)


class XiaoTianQuan(Dog):

    def game(self):

        print("%s飞天遁地" % self.name)


class Person(object):

    def __init__(self, name):

        self.name = name

    def game_with_dog(self, dog):

        print("%s 和 %s 玩" % (self.name, dog.name))

        # 让狗玩耍，让传递过来的dog参数调用狗类封装的game方法
        dog.game()


# 创建一个狗对象
hashiqi = Dog("哈士奇")
xiaotianquan = XiaoTianQuan("哮天犬")

# 创建一个小明对象
xiaoming = Person("小明")

# 小明调用和狗玩的方法
xiaoming.game_with_dog(hashiqi)

# 让不同的子类对象调用相同的子类方法，产生不同的结果。

"""
只需要让狗对象调用game方法，不需要关心是什么狗
game方法是在父类中定义的，在执行程序的时候，传入不同的狗对象，就会产生不同的结果
这就是多态
"""











