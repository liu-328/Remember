"""
1、根据列表[ 1, 6, 3, 5, 3, 4 ]作为新字典的key,对应key的初始值为0，并打印新字典对象
"""
a = [1, 6, 3, 5, 3, 4]
b = {}
for i in a:
    b[i] = 0
    if len(b) == len(set(a)):
        print(b)

"""
2、循环打印出字典{'name':'aming','age':18,'school':'cema'}中的所有键和值，
"""

c = {'name': 'aming', 'age': 18, 'school': 'cema'}
for key in c:
    print("字典中的key为：%s，value为：%s" % (key, c[key]))

"""
3、{‘taobao’,'jingdong','alibaba','baidu','taobao'}对元素去重复
"""
d = {'taobao', 'jingdong', 'alibaba', 'baidu', 'taobao'}
print(d)

"""
4、分别有两个集合{1,2,1,3,4,5,6,7}，{1,2,3,8,9,7,10}，求两个集合的差集、并集、交集
"""

e = {1, 2, 1, 3, 4, 5, 6, 7}
f = {1, 2, 3, 8, 9, 7, 10}
print(e.difference(f))
print(e - f)
print(f - e)
print(e.union(f))
print(e | f)
print(e.intersection(f))
print(e & f)

"""
5、判断9题中两个集合如果存在相同元素，则打印重复，否则打印无重复
"""
if not e.isdisjoint(f):
    print(e.intersection(f))
else:
    print("无重复")

"""
6、info=['姓名','所在城市','毕业年限','目前薪资','期望薪资','班级']
每个学员都基于列表中的字段存储对应的信息数，基于字典来进行存储，如何初始化定义每个学员的信息数据？（基于字典来存储这些数据信息）
"""
info = ['姓名', '所在城市', '毕业年限', '目前薪资', '期望薪资', '班级']
dic = {}
print(dic.fromkeys(info))

"""
7、a={'name':'AA','age':18} 获取a变量的classname的值,如果该key不存在，则添加该key，并设置默认值为'212'
"""
dict1 = {'name': 'AA', 'age': 18}
dict1["classname"] = 212
print(dict1)
