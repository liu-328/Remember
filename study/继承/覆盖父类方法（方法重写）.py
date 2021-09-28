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

    def dock(self):

        print("汪汪叫")


class XiaoTianQuan(Dog):

    def fly(self):

        print("飞飞飞~")

    def dock(self):

        print("嗷嗷叫")


xtq = XiaoTianQuan()
# 如果在子类中重写了父类方法
# 在使用子类调用方法时，会调用子类中重写的方法。
xtq.dock()












