class Person:

    def __init__(self, name, weight):

        self.name = name
        self.weight = weight

    def __str__(self):

        return "%s 的体重为 %.2f kg" % (self.name, self.weight)

    def run(self):

        print("%s 爱跑步" % self.name)

        self.weight -= 0.5

    def eat(self):

        # 在对象的方法内部，是可以直接访问对象的属性的
        print("%s 是吃货，不吃饱哪有力气减肥" % self.name)

        self.weight += 1


xiaoliu = Person("小刘", 50)
xiaoliu.run()
xiaoliu.eat()
print(xiaoliu)

xiaomei = Person("小美", 45)
xiaomei.eat()
xiaomei.run()

print(xiaomei)

# 在同一个类中创建的对象，多个对象之间的属性是互不干扰的
print(xiaoliu)

















