# -*- coding: utf-8 -*-

# 1.打开文件
# 文件编码 encoding="utf-8"
file = open("readme", encoding="utf-8")

# 2.读取文件内容
# read方法在默认的情况下返回文件的所有内容
test = file.read()
print(test)

# 3.关闭文件
file.close()







