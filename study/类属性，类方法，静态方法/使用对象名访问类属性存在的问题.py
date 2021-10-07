class Tool(object):

    # 使用赋值语句定义类属性，记录所有工具的对象数量
    count = 0

    def __init__(self, name):

        self.name = name

        # 让类的属性值+1
        Tool.count += 1


# 1.创建工具对象
tool1 = Tool("斧头")
tool2 = Tool("榔头")
tool3 = Tool("水桶")

# tool3.count = 99 是设置值语句，在执行赋值语句的时候会在tool3变量（对象）中查找count属性，
# 如果没有会给tool3这个类添加一个count属性
tool3.count = 99
print("工具对象的总数 %d" % tool3.count)
