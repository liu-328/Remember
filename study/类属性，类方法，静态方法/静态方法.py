class Dog(object):

    @staticmethod
    def run():

        # 如果方法内部不访问实例（对象）属性，也不需要访问类属性时，就可以使用静态方法
        print("跑跑跑...")


# 不需要创建对象，通过类名+方法名调用静态方法
Dog.run()

