
class Cat:

    def eat(self):

        # 哪个对象调用方法，self就是哪个对象的引用
        print("%s 爱吃鱼" % self.name)

    def drink(self):

        print("%s 要喝水" % self.name)


# 创建猫对象
tom = Cat()

# 给对象创建一个属性只需要 .+属性名  利用赋值语句赋值就可以了。
# 不推荐使用
tom.name = "汤姆"

# 对象 + .调用方法
tom.eat()
tom.drink()
print(tom)

# 在创建一个对象
lazy_cat = Cat()

lazy_cat.name = "懒猫"

lazy_cat.drink()
lazy_cat.eat()

print(lazy_cat)

lazy_cat2 = lazy_cat
print(lazy_cat2)






















