class Tool(object):

    # 使用赋值语句定义类属性，记录所有工具的对象数量
    count = 0

    # 定义类方法
    @classmethod
    def show_tool_count(cls):

        print("工具对象的数量 %s" % cls.count)

    def __init__(self, name):

        self.name = name

        # 让类的属性值+1
        Tool.count += 1


# 创建工具对象
tool1 = Tool("斧头")
tool2 = Tool("剪刀")

# 调用类方法
Tool.show_tool_count()






