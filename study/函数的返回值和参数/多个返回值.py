def measure():
    """测量湿度和温度"""

    print("测量开始...")
    temp = 39
    wetness = 50
    print("测量结束...")

    # 元组可以包含多个函数，因此可以让函数一次返回多个值
    # 如果返回值是一个元组，小括号可以省略
    return temp, wetness


# 元组
result = measure()
print(result)

# 需要单独处理温度或者湿度 - 不方便
print("温度为 %s" % result[0])
print("湿度为 %s" % result[1])

# 如果函数的返回类型为元组，同时希望单个处理元组中的元组
# 可以使用多个变量，一次接收函数的返回结果
# 注意：使用多个变量接收结果时，变量的个数要跟元组内元素的个数保持一致
gl_temp, gl_wetness = measure()

print(gl_temp)
print(gl_wetness)




a = 100
b = 6
c = b
b = a
a = c

print(a, b)
















