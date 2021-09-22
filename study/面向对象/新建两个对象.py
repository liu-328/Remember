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

# 在创建一个对象
lazy_cat = Cat()

lazy_cat.drink()
lazy_cat.eat()

print(lazy_cat)

lazy_cat2 = lazy_cat
print(lazy_cat2)
# 使用同一个类再创建出来的一个对象，并不是同一个对象。
# 类可以只有一个，使用相同的类可以创建多个不同的对象。
















