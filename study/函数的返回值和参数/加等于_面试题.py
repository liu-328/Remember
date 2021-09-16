def demo(num, num_list):

    print("函数开始")

    # num = num + num
    # 相加再赋值。
    num += num
    # 列表变量使用+=不会做相加再赋值的操作
    # num_list = num_list + num_list
    # 本质上是在调用列表的 extend 方法。调用方法就会影响到外部参数
    num_list += num_list
    # num_list.extend(num_list)

    print(num)
    print(num_list)

    print('函数结束')


gl_list = [1, 2, 3]
gl_num = 9
demo(gl_num, gl_list)
print(gl_num)
print(gl_list)















