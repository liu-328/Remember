gl_num = 10
gl_title = '小刘'
gl_name = "小妮"


def demo():

    # 如果局部变量和全局变量的名字相同，
    # pycharm会在局部变量下方展示一个灰色的虚线。
    num = 99

    print("{}".format(gl_num))
    print("%s" % gl_title)
    print("%s" % gl_name)


demo()


