# 需求：
# 小猫爱吃鱼，小猫要喝水
class Cat:

    def eat(self):

        print("小猫爱吃鱼")

    def drink(self):

        print("小猫要喝水")


# 创建猫对象
tom = Cat()

tom.eat()
tom.drink()
print(tom)
addr = id(tom)
# %d 可以输出10进制
# %x 可以输出16进制
print('%x' % addr)












