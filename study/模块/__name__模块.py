# 全局变量、函数、类、注意：直接执行的代码不是向外界提供的工具！

def say_hello():

    print("hello，hello")


# 如果直接执行模块，控制台输出一个固定的__main__
# 测试模块，其他文件导入的时候，不会在导入的文件内被执行
if __name__ == "__main__":
    print(__name__)

# 文件被导入时，能够直接执行的代码不需要被执行。
print("你好呀！我是赛利亚")

say_hello()
