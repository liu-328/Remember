class Cat:

    def __init__(self, new_name):

        self.name = new_name

        print("%s 来了" % self.name)

    def __del__(self):

        print("%s 走了" % self.name)


# tom是一个全局变量
tom = Cat("tom")
print(tom.name)
# 在内存中删除tom对象
del tom

print("-" * 50)









