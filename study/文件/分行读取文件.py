# 1.打开文件
import os

file = open("readme")

# 2.读取文件
while True:

    test = file.readline()

    # 判断是否读取到内容
    if not test:
        break

    print(test, end='')
# 3.关闭文件
file.close()



os.mkdir(os.getcwd()+'a')







