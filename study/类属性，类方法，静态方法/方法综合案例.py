class Game(object):

    # 类属性，历史最高分
    top_score = 0

    def __init__(self, play_name):

        # 实例属性，游戏玩家姓名
        self.play_name = play_name

    # 静态方法：显示游戏帮助信息
    @staticmethod
    def show_help(test):

        print("帮助信息是啥我也不知道-.-！")

        # 静态方法内部调用类方法
        Game.show_top_score()

        # 对象内部是否可以调用实例方法,
        # 把对象以实参的方式传递到静态方法内部，静态方法内部调用实例方法。
        test.start_game()

    # 类方法，显示历史记录最高分
    @classmethod
    def show_top_score(cls):

        print("历史最高分为 %d" % cls.top_score)

    # 实例方法，开始当前玩家的游戏
    def start_game(self):

        print("%s 开始游戏了" % self.play_name)
        # 在实例方法内部使用---类名.类属性来访问类属性
        print("历史最高分为 %d" % Game.top_score)
        print("-------")


# 1.查看游戏帮助信息
test_player = Game("测试玩家")
Game.show_help(test_player)

# 2.查看历史最高分
Game.show_top_score()
# 3.创建游戏对象---对象的实例方法创建需要先创建一个对象
game = Game("小刘")
game.start_game()

# 1.如果创建的方法中需要访问对象的实例属性，实例方法
# 2.如果创建的方法内部只需要访问的类的类属性或者只需要调用类方法，类方法
# 3.如果创建的方法内部不需要访问实例属性，也不需要访问类属性，静态方法
# 4.如果定义的方法需要类属性，也需要实例属性，实例方法（在实例方法内部使用---类名.类属性来访问类属性）








