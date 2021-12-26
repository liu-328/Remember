import os

path = "/Users/liushijia/Documents/git/Remember/pytest_produt/logs"


# 清空logs文件夹
def get_file(paths):
    len_mkdir = []
    for i in os.listdir(paths):
        i = os.path.join(paths, i)
        if os.path.isdir(i):
            len_mkdir.append(i)
        else:
            len_mkdir.append(i)
    index = len_mkdir.index('/Users/liushijia/Documents/git/Remember/pytest_produt/logs/__init__.py')
    len_mkdir.pop(index)
    if len(len_mkdir) > 100:
        for file in len_mkdir:
            os.remove(file)


if __name__ == '__main__':
    get_file(path)