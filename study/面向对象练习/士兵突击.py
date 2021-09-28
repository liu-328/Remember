class Gun:

    def __init__(self, model):

        # 定义枪的子弹数量 初始值为0
        self.bullet_count = 0
        # 定义枪的类型属性
        self.model = model

    def add_bullet(self, count):

        # 添加子弹
        self.bullet_count += count

    def shoot(self):

        # 判断枪内的子弹数量
        if self.bullet_count <= 0:

            print("[%s]没有子弹了....." % self.model)

            return

        # 开枪子弹-1
        self.bullet_count -= 1

        print("手持[%s]哒哒哒~~~  [%s]" % (self.model, self.bullet_count))


class Soldier:

    def __init__(self, name):

        self.name = name
        # 定义属性时，如果不知道设置什么属性，可以把属性设置为None
        self.gun = None

    def fire(self):

        # 1.判断士兵是否有枪
        if self.gun is None:

            print("没有枪")

            return
        # 2.让枪装填子弹
        # 调用其他类里面的方法 一个对象的属性可以是另外一个类创建的对象。
        self.gun.add_bullet(40)
        print("冲啊！！！ [%s]" % self.name)
        # 3.让枪发射子弹
        self.gun.shoot()


# 创建枪对象
AK = Gun("AK-47")
# AK.add_bullet(40)
# AK.shoot()

# 创建张佳伟
jiawei = Soldier("张佳伟")
jiawei.gun = AK
jiawei.fire()

print(jiawei.gun)








