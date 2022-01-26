"""
想要操作目录需要导入os模块
    1.文件重命名 os.rename("原文件name","新文件name")
    2.删除文件  os.remove("文件名")  只可以删除空目录
               shutil.rmtree("路径")  导入模块shutil删除非空目录
    3.查看当前目录下的内容 os.listdir(".")
    4.判断是文件还是文件夹 os.path.isdir("文件夹名字")
        判断是否是文件    os.path.isfile("文件名")
    5.创建目录 os.mkdir("目录名")
    6.删除目录 os.rmdir("目录名")  只可以删除空目录
    7.获取当前目录 os.getcwd()
    8.修改工作目录 os.chdir("目标目录")
    9.验证文件权限 os.access(path='路径', mode=os.F_OK)
        mode = os.F_OK(是否存在)、os.R_OK(可读)、os.W_OK(可写)、os.X_OK(可执行)
    10.改变文件的权限 os.chmod(path='路径',mode=stat.)
        mode = 详见chmod mode参数
    11.创建多级目录  os.makedirs("文件名")
    12.获取绝对路径  os.path.abspath("文件名")
    13.获取目录的路径  os.path.dirname("目录名")
    14.判断文件是否存在  os.path.lexists("目录名")
    15.路径分割  os.path.split("路径")
        返回值：("/Users/liushijia/Documents/git/Remember/study/文件", "os模块.py")
    16.路径拼接  os.path.join("路径1","路径2")
"""
import os
path = r"/Users/liushijia/Documents/git/Remember"
path1 = "study/文件/os模块.py"
print(os.path.split(path)[1])
print(os.path.join(path, path1))
# 读取文件夹内的文件名以列表的形式返回
print(os.listdir("/pytest_product/Commons"))


# 读取当前目录下的所有文件
def get_file(paths):

    for i in os.listdir(paths):
        i = os.path.join(paths, i)
        if os.path.isdir(i):
            get_file(i)

        else:
            print(i)


get_file(os.getcwd())
print(2 / 0.97)
print(22.33 - 2.06)