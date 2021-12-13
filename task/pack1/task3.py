"""
1、定义一个列表[1, 2, 3]，并将列表中的头尾两个元素对调。对调后为[3, 2, 1]
"""
a = [1, 2, 3]
a[0], a[2] = a[2], a[0]
print(a)

"""
2、定义一个列表，并将列表中的指定位置的两个元素对调。对调第一个和第三个元素
列表如下：[23, 65, 19, 90] 
对调后结果：[19, 65, 23, 90]
"""
b = [23, 65, 19, 90]
b[0], b[2] = b[2], b[0]
print(b)

"""
3、对列表[10, 11, 12, 13, 14, 15]翻转，调整后为[15, 14, 13, 12, 11, 10]
"""
c = [10, 11, 12, 13, 14, 15]
# 列表翻转
c.reverse()
print(c)
# list.sort(reverse=True) 降序
c.sort(reverse=True)
print(c)

"""
4、判定6是否包含列表[ 1, 6, 3, 5, 3, 4 ]
"""
d = [1, 6, 3, 5, 3, 4]
print(6 in d)

"""
[ 1, 6, 3, 5, 3, 4 ]转换为元组
"""
e = [1, 6, 3, 5, 3, 4]
print(tuple(e))

"""
6、根据列表[ 1, 6, 3, 5, 3, 4 ]作为新字典的key,对应key的初始值为0，并打印新字典对象
"""
f1 = [1, 6, 3, 5, 3, 4]
f = {}
for i in f1:
    f[i] = 0
    if len(f) == len(set(f1)):
        print(f)

"""
7、循环打印出字典{'name':'aming','age':18,'school':'cema'}中的所有键和值， （不做）
"""
g = {'name': 'aming', 'age': 18, 'school': 'cema'}
for o in g:
    print('字典的key：%s，字典的值：%s' % (o, g[o]))

"""
8、{‘taobao’,'jingdong','alibaba','baidu','taobao'}对元素去重复  （不做）
"""
h = {'taobao', 'jingdong', 'alibaba', 'baidu', 'taobao'}
print(h)

"""
9、分别有两个集合{1,2,1,3,4,5,6,7}，{1,2,3,8,9,7,10}，求两个集合的差集、并集、交集（不做）
"""

j = {1, 2, 1, 3, 4, 5, 6, 7}
k = {1, 2, 3, 8, 9, 7, 10}
# 求两个集合的差集
print(j.difference(k))
print(j - k)
# 并集
print(j.union(k))
print(j | k)
# 交集
print(j & k)
print(j.intersection(k))

"""
10、判断9题中两个集合如果存在相同元素，则打印重复，否则打印无重复（不做）
"""

if j.intersection(k):
    print(j.intersection(k))
else:
    print("无重复")

"""
11、list7=[1,2,3,4,5]根据列表中的元素作为字典中的key,及初始值为0，打印这个新的字典，不用fromkey方法实现（不做）
"""

list7 = [1, 2, 3, 4, 5]
dic = {}
print()
for ii in list7:
    dic[ii] = 0
    if len(dic) == len(list7):
        print('-------', dic)
# print(dic.fromkeys(list7, 0))
# fromkeys方法 可以把一个序列里面的值转换为字典的key (list7, 0)指的是将0作为key对应的默认值

