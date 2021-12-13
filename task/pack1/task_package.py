# 操作界面
user_message = []


def Interface():

    print("-----------------------欢迎进入T666班学生管理系统-----------------------------")
    print('请选择系统功能：')
    print("0:显示所有学员信息")
    print("1:添加一个学员信息")
    print("2:删除一个学员信息")
    print("3:修改一个学员信息")
    print("4: 查询一个学员信息")
    print("exit:退出学生管理系统")


# 显示所有学生信息：
def see_message():

    print(user_message)


# 1 添加一个学生信息：
def add_message():

    add_student_message = input("请输入想要添加的学生信息：")
    user_message.append(add_student_message)
    print("%s 信息添加成功" % add_student_message)


# 2.删除学生信息
def remover_message():

    remove_student_message = input("请输入要删除的学生信息：")
    if remove_student_message in user_message:
        user_message.remove(remove_student_message)
        print(user_message)
    else:
        print("T666班没有这个学员>")
        remover_message()


# 3.修改一个学员信息

def change_message():

    will_student_message = input("请输入要修改学生的姓名：")
    if will_student_message in user_message:
        change_student_message = input("请输入修改后的学生姓名：")
        user_message.remove(will_student_message)
        user_message.append(change_student_message)
        print(user_message)

    else:
        print('T666班没有这个学员>')
        change_message()


# 4查询一个学生信息
def look_a_message():

    look_student_message = input("请输入要查询的学生姓名：")
    if look_student_message in user_message:

        print("%s在座位号在%d的位置"% (look_student_message, user_message.index(look_student_message)))

    else:
        print("T666班没有这个学员>")
        look_a_message()

