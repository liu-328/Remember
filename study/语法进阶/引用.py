def test(num):

    print("在函数内部 %d 对应的内存地址为 %d" % (num, id(num)))

    # 1> 定义一个字符串变量
    result = 'hello'

    print("函数将要返回的内存地址是 %d" % id(result))
    # 2> 将字符串变量返回,返回的是数据的引用，而不是数据本身
    # 如果不指定返回值result，默认返回结果为None
    return result

# 1.定义一个数字的变量
a = 10

# 数字的地址本质上就是一个数字
print("a 变量保存数据的内存地址是 %d" % id(a))

# 2.调用test函数
# 注意：如果函数有返回值，但是没有定义变量的接收
# 程序不会报错，但是无法获得返回结果
r = test(a)

print("%s 函数的内存地址是 %d" % (r, id(r)))

print(id(None))

a = [1, 2, 3]
print(id(a))
b = [1, 2, 3]
print(id(b))

print(a == b)  # True  ==运算符是判断变量引用的参数是否相等
print(a is b)  # False  is 运算符是判断变量引用的参数的内存地址是否相等








