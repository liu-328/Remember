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


# 2.输出工具对象的总数
print(Tool.count)

# 向上查找机制，如果tool3对象内部属性含有count属性则直接输出count，如果没有就向上查找（查找创建这个对象的类）
# 如果类属性内不包含count属性，则报错
print("工具对象的总数 %d" % tool1.count)
print("工具对象的总数 %d" % tool2.count)
print("工具对象的总数 %d" % tool3.count)















