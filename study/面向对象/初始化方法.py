class Cat:

    # 定义默认属性
    def __init__(self, new_name):

        print("这是一个初始化方法")

        # self.属性名 = 属性的初始值
        # self.name = 'tom'
        self.name = new_name

    def eat(self):

        print('%s 爱吃鱼' % self.name)


# 使用类名()创建对象的时候，会自动调用初始化方法__init__
tom = Cat('tom')

print(tom.name)

lazy_name = Cat('懒猫')
lazy_name.eat()




















