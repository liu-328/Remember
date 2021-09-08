# 假设：以下内容是从网络上抓取来的
# 要求：顺序且居中对其输出以下内容

poem = ["\t\n登鹳雀楼",
        "王之涣",
        "白日依山尽\t\n",
        "黄河入海流",
        "欲穷千里目",
        "更上一层楼"]

for poem_str in poem:

    # 先使用strip方法去除左右两边的空白字符
    # 再使用center方法居中对齐
    print("|%s|" % poem_str.strip().center(10, " "))


# for i in poem:
#
#     print("|%s|" % i.rjust(10, " "))  # ljust右对齐




















