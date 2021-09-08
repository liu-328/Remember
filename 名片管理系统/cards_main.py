#! C:\Users\Administrator\AppData\Local\Programs\Python\Python39

import cards_tools
# 无限循环，由用户决定什么时候退出循环。
while True:

    cards_tools.show_menu()
    action_str = input("请选择希望执行的操作：")

    print("您选择的操作是[%s]" % action_str)

    # 1,2,3 是针对名片的操作
    if action_str in ["1", "2", "3"]:

        # 新增名片
        if action_str == "1":
            cards_tools.new_card()

        # 显示全部
        elif action_str == "2":
            cards_tools.show_all()

        # 查询名片
        elif action_str == "3":
            cards_tools.search_card()

    # 0 退出
    elif action_str == "0":
        print("Goodbye~")

        break
    # 其他内容输入错误，需要提示用户
    else:
        print("输入错误，请重新输入：")
