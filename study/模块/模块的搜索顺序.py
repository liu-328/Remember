import random


print(random.__file__)  # D:\Git\Remember\Remember\study\模块\random.py
# C:\Users\Administrator\AppData\Local\Programs\Python\Python39\lib\random.py
# 同级目录下如果存在random.py文件则会优先选择同级目录
rand = random.randint(1, 10)

print(rand)
