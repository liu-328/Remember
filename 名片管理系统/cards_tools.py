card_list = []


def show_menu():

    """显示菜单"""
    print("-" * 50)
    print("欢迎使用[名片管理系统] V 1.0")
    print("")
    print("1.增加名片")
    print("2.显示全部")
    print("3.搜索名片")
    print("")
    print("-" * 50)
    print("输入0退出")


def new_card():

    """新增名片"""
    print("-" * 50)
    print("新增名片")

    # 1.提示用户输入名片的详细信息
    name_str = input("请输入姓名：")
    phone_str = input("请输入电话号码：")
    gender_str = input("请输入性别：")
    wechat_str = input("请输入你的微信号：")
    # 2.使用用户输入的信息建立一个字典
    card_dict = {"name": name_str,
                 "phone": phone_str,
                 "gender": gender_str,
                 "wechat": wechat_str}
    # 3.将名片字典添加到字典中
    card_list.append(card_dict)

    # print(card_list)
    # 4.提示添加成功
    print("添加%s的名片成功" % name_str)


def show_all():

    """显示所有名片"""
    print("-" * 50)
    print("显示所有名片")

    # 判断是否存在名片记录，如果没有，提示用户返回
    if len(card_list) == 0:

        print("当前没有任何名片记录，请使用新增功能增加名片")

        # return 可以返回一个函数的结果
        # 下方的代码不会被执行。
        # 如果return 后面没有任何的内容，表示会返回到调用函数的位置
        return

    # 打印表头
    for name in ["姓名", "电话", "性别", "微信号"]:
        print(name, end="\t\t\t")

    print("")
    # 打印分割线
    print("=" * 50)

    # 遍历名片列表依次输出信息
    for card_dict in card_list:

        print("%s\t\t\t%s\t\t\t%s\t\t\t%s\t\t\t" % (card_dict["name"],
                                                    card_dict["phone"],
                                                    card_dict["gender"],
                                                    card_dict["wechat"]))


def search_card():

    """搜索名片"""
    print("-" * 50)
    print("搜索名片")

    # 1.提示用户输入要搜索的姓名
    find_name = input("请输入要搜索的姓名：")

    # 2.遍历名片列表查询要输入的内容，如果没有找到需提示用户
    for card_dict in card_list:

        if card_dict['name'] == find_name:

            print("姓名\t\t\t电话\t\t\t性别\t\t\t微信号")
            print("*" * 50)
            print("%s\t\t\t%s\t\t\t%s\t\t\t%s\t\t\t" % (card_dict["name"],
                                                        card_dict["phone"],
                                                        card_dict["gender"],
                                                        card_dict["wechat"]))
            # 针对找到的名片记录执行修改和删除的操作
            deal_card(card_dict)
            break
    else:
        print("sorry，没有找到%s" % find_name)


def deal_card(find_dict):
    """
    处理查找到的名片
    :param find_dict:查找到的名片
    """
    # print(find_dict)

    action_str = input("请选择要执行的操作：[1]修改 | [2]删除 | [0]返回上级菜单：")

    if action_str == "1":

        find_dict['name'] = input_card_info(find_dict['name'], "修改姓名[输入回车不修改]：")
        find_dict['phone'] = input_card_info(find_dict['phone'], "修改电话[输入回车不修改]：")
        find_dict['gender'] = input_card_info(find_dict['gender'], "修改性别[输入回车不修改]：")
        find_dict['wechat'] = input_card_info(find_dict['wechat'], "修改微信[输入回车不修改]：")

        print("修改名片成功")

    elif action_str == "2":

        card_list.remove(find_dict)

        print("删除名片成功")


def input_card_info(dict_value, tip_message):
    """
    输入名片信息
    :param dict_value: 字典中原有的值
    :param tip_message:输入的提示文字
    :return:如果用户输入了内容就返回内容。否则返回字典中原有的值
    """

    # 1.提示用户输入内容
    result_str = input(tip_message)
    # 2.针对用户输入内容进行判断，如果输入了内容，直接返回结果
    if len(result_str) > 0:

        return result_str
    # 3.如果用户没有输入内容，返回字典中原有的值
    else:
        return dict_value















