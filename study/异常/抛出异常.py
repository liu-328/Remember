def input_password():

    # 1. 提示用户输入密码
    kwd = input("请输入密码：")
    # 2.判断密码长度
    if len(kwd) >= 8:
        return kwd
    # 3. 如果小于8。抛出异常
    print("主动抛出异常")

    # 创建异常对象 - 可以使用错误信息字符串作为参数
    ex = Exception("密码长度不足")

    # 抛出异常
    raise ex


# 捕获异常
try:
    print(input_password())

except Exception as result:
    print(result)














