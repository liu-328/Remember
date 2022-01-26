class Module:
    """
    这是一个类
    """
    count = 0

    def __init__(self, name):
        self.name = name
        Module.count += 1

    def test(self):
        print(f'我的名字叫{self.name}')

    @staticmethod
    def test1():
        print('这是一个静态方法')

    @classmethod
    def cls_metod(cls):
        print(cls.count)

    # def __getattribute__(self, item):
    #     print(item, '===============')
    #     if item == 'count':
    #         print('类属性count被调用')

    def __del__(self):
        print('释放对象的内存地址')

    def __str__(self):
        return "hello world"


# 返回类的名称
print(Module.__name__)
# 如果类在当前模块 返回值为__main__
# 如果类是外部导入模块，返回值为类的名称
print(Module.__module__)
print(__name__ == '__main__')
print(__name__)

# 返回类的文档字符串
print(Module.__doc__)
# 返回一个字典，包含类里面的各个数据
print(Module.__dict__)
# 查看类的父类
print(Module.__bases__)

test_obj1 = Module('对象1')
test_obj2 = Module('对象2')

# 类方法可以被类调用，也可以被对象调用
Module.cls_metod()
test_obj1.cls_metod()

# 静态方法可以被类调用，也可以被对象调用

test_obj1.test1()
Module.test1()

# 类属性可以被类调用，也可以被对象调用
print(test_obj1.count)
print(Module.count)

# 实例属性只可以被对象调用，不可以被类调用
print(test_obj1.name)
# Module对象内没有属性name，不可以被类去调用
# print(Module.name)

# 实例方法可以被对象调用，也可以被类调用，
test_obj1.test()
# 实例方法在被类调用的时候，需要在调用方法的时候传入一个self参数
# self参数表示为自己 ==> 对象
Module.test(test_obj2)

