
input_str = input("请输入算术题:")

# 把一个字符串传递给eval函数，eval函数会把传入内容当做python的代码去执行
print(eval(input_str))

# 在开发时不要使用eval直接转换input的转换结果，否则
# 用户输入__import__("os").system("touch xxx")命令可以操作文件目录

