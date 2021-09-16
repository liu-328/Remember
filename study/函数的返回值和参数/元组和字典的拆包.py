def demo(*args, **kwargs):

    print(args)
    print(kwargs)


# 元组变量/字典变量
gl_nums = (1, 2, 3)
gl_list = {'name': '小刘', 'age': 18}

# 拆包语法，简化元组和列表的传递。
demo(*gl_nums, **gl_list)

# demo(gl_nums, gl_list)
# demo(1, 2, 3, 'name': '小刘', 'age': 18)


