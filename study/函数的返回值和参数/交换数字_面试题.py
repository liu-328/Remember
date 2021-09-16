a = 6
b = 10

# 解法1：使用其他变量
# c = a
# a = b
# b = c

# 解法2不使用其他的变量
# a = a + b
# b = a - b
# a = a - b


# python专有
# a, b = (b, a)
# 等号右边是一个元组，只是把小括号省略了。
a, b = b, a
print(a, b)




