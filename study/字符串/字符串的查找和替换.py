hello_str = "hello hello"

# 1.判断字符串是否以指定字符串开始
print(hello_str.startswith("hello"))

# 2.判断字符串是否以指定字符串结束
print(hello_str.endswith("world"))

# 3.查找指定字符串
# index 同样可以查找指定的字符串在大字符串中的索引
print(hello_str.find("llo"))
print(hello_str.find('abc'))  # -1

# index方法如果指定字符串不存在会报错
# find方法指定字符串不存在会返回-1

# 4.替换字符串
# replace 方法执行完成后，会生成一个新的字符串。
# 注意：不会修改原有字符串中的内容
print(hello_str.replace("hello", "world"))
print(hello_str)










