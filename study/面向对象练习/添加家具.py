# 定义一个家具类
class HostItem:

    def __init__(self, name, area):

        self.name = name
        self.area = area

    def __str__(self):

        return "家具的名称: %s, 家具的占地面积: %.2f m²" % (self.name, self.area)


# 创建家具
bed = HostItem("床", 4)
print(bed)
chest = HostItem("衣柜", 2)
print(chest)
table = HostItem("餐桌", 1.5)
print(table)


# 定义一个房子类
class Host:

    # 只有需要外部添加的参数，才需要把这些参数定义成初始化方法的形参
    def __init__(self, host_type, area):

        self.host_type = host_type
        self.area = area
        # 剩余面积

        self.free_area = area
        # 家具名称列表

        self.item_list = []

    def __str__(self):

        return "房子的户型是：%s，\n房子的占地面积是：%.2f m², \n房子的剩余面积是：%.2f m², \n房子内的家具有：%s" \
               % (self.host_type, self.area, self.free_area, self.item_list)

    def add_item(self, item):

        print("要添加的家具 %s" % item)
        # 1.判断家具的面积
        if item.area > self.free_area:

            print("家具[%s]占地面积太大，无法添加" % item.name)

            return
        # 2.将家具的名称添加到列表中
        self.item_list.append(item.name)
        # 3.计算剩余面积
        self.free_area = self.free_area - item.area


# 创建房子对象
new_host = Host("别墅", 200)

new_host.add_item(bed)
print(new_host)
# new_host.add_item(chest)
# new_host.add_item(table)
