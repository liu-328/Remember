class Animal:

    def eat(self):

        print("吃---")

    def drink(self):

        print("喝---")

    def run(self):

        print("跑---")

    def sleep(self):

        print("睡---")


class Dog(Animal):

    def bark(self):

        print("汪汪叫")


class XiaoTianQuan(Dog):

    def fly(self):

        print("飞飞飞~")

    def bark(self):

        # 针对子类特有的需求编写代码
        print("嗷嗷叫")

        # 使用super().调用原本在父类中封装的方法。
        super().bark()

        # 使用父类名.方法名(self) 不推荐   
        # Dog.bark(self)

        # 注意，如果使用子类调用方法，会出现递归  · 死循环
        # XiaoTianQuan.bark(self)

        # 增加其他子类的代码
        print("@@#$%^&**#$%^&*&^%$")


xtq = XiaoTianQuan()
# 如果在子类中重写了父类方法
# 在使用子类调用方法时，会调用子类中重写的方法。
xtq.bark()