class MusicPlayer(object):

    # 定义类属性，保存第一个被创建对象的引用
    instance = None
    # 记录是否执行过__init__方法
    init_flog = False

    def __new__(cls, *args, **kwargs):

        # 1. 判断类属性是否是一个空对象
        if cls.instance is None:

            # 2. 如果对象没有被创建，调用类方法，为对象分配一个空间
            cls.instance = super().__new__(cls)
        # 3.返回类属性保存的对象引用
        return cls.instance

    def __init__(self):

        # 判断是否执行过初始化动作
        # 调用类属性init_flog时需要使用类名.init_flog的方式调用，而不是self.
        if MusicPlayer.init_flog is False:

            # 如果没有执行，则执行
            print("播放器初始化")

            # 执行过后让初始化动作init_flog为True，之后就不会被执行了
            MusicPlayer.init_flog = True


# 创建多个对象
player1 = MusicPlayer()
print(player1)

player2 = MusicPlayer()
print(player2)


