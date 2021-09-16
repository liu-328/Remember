def demo(num, num_list):

    print("函数内容的代码")

    # 在函数中，针对参数使用赋值语句，不会修改到外部的实参变量
    # 形参置灰时，不会修改到外部实参，因为此时的num,num_list相当于是局部变量，
    # 并不会影响全局变量的参数。
    num = 100
    num_list = [1, 2, 3]

    print(num)
    print(num_list)
    print("函数执行完成")


gl_num = 99
gl_list = [4, 5, 6]
demo(gl_num, gl_list)
print(gl_num)
print(gl_list)







