# 以utf-8的编码格式执行以下代码
# *-* coding:utf-8 *-*

hello_str = u"hello世界"

# 使用python2解释器执行会报错，Non-ASCII Character,“hello世界”不是ASCII编码
print(hello_str)

# 如果在python2中循环遍历字符串，一个汉字会出现三小问号
# 字符串前增加u告诉解释器这是一个utf-8编码格式的字符串
for c in hello_str:

    print(c)










