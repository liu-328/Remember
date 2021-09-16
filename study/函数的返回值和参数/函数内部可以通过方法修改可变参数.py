def demo(num_list, num_dict):

    print("函数内部的代码")

    # 使用方法修改列表内的内容
    num_list.append(9)
    num_dict.update({"name3": "小张"})

    print(num_list)
    print(num_dict)

    print("函数执行完成")


gl_list = [1, 2, 3]
gl_dict = {"name1": "小刘", "name2": "小妮"}
demo(gl_list, gl_dict)
print(gl_list)
print(gl_dict)

















