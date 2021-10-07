class MusicPlayer(object):

    # 定义类属性，保存第一个被创建对象的引用
    instance = None

    def __new__(cls, *args, **kwargs):

        # 1. 判断类属性是否是一个空对象
        if cls.instance is None:

            # 2. 如果对象没有被创建，调用类方法，为对象分配一个空间
            cls.instance = super().__new__(cls)
        # 3.返回类属性保存的对象引用
        return cls.instance


# 创建多个对象
player1 = MusicPlayer()
print(player1)

player2 = MusicPlayer()
print(player2)














