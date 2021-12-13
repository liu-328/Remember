# 1.打开文件
# 文件编码 encoding="utf-8"
file = open("readme", encoding="utf-8")

# 2.读取文件内容
# read方法在默认的情况下返回文件的所有内容
test = file.read()
print(test)
print(len(test))

print("-" * 50)

# 读取完文件后，read指针会移动到文件末尾，之后再次调用read方法就不会输出内容了。
test = file.read()
print(test)
print(len(test))
# 3.关闭文件
file.close()
