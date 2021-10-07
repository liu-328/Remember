class MusicPlayer(object):

    # 重写父类方法__new__
    def __new__(cls, *args, **kwargs):

        # 创建对象时，new方法会被自动调用，如果调用时，没有设置返回的内存空间则打印对象时，
        # 返回一个None，也不会调用初始化方法__init__方法
        print("创建对象，分配空间")

        # 设置返回内存地址是用super()调用父类的（object内置）方法__new__设置返回地址
        # __new__方法是静态方法，调用时应该把cls传递进去
        # 要调用父类方法使用特殊的super()对象
        instance = super().__new__(cls)

        # 返回对象的引用
        return instance

    def __init__(self):

        print("播放器初始化")


# 创建对象
player = MusicPlayer()

print(player)

















