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


class Cat(Animal):

    def catch(self):

        print("抓老鼠")


# 创建一个哮天犬对象.
xtq = XiaoTianQuan()
xtq.fly()
xtq.dock()
xtq.eat()

# xtq.catch()
























