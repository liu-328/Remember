# 定义一个函数 sum_number
# 能够接收num的整数参数
# 计算1+2....num 的结果

def sum_number(num):
    # 定义出口
    if num == 1:
        return 1

    # 数字的累加，num + (1...num - 1)
    # 定义一个变量来接收每一次递归返回的值。
    temp = sum_number(num - 1)
    print('num = ', num, 'temp = ', temp)
    return num + temp


result = sum_number(3)
print(result)





















