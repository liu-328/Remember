import time
import datetime

print('时间戳：', time.time())
print('时间元组：', time.localtime())

# 时间戳转换成时间元祖
times = time.localtime(1638365156)

# 时间元祖转换为时间戳
print(time.mktime(times))

# 时间转换为时间元祖
# '%Y-%m-%d %H:%M:%S'
print(time.strptime('2021-12-01 20:30:30', '%Y-%m-%d %H:%M:%S'))

# 时间元祖转换为字符串
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))

"""
-------------------------------------------------------------
"""
# 获取当天的时间
print(datetime.date.today())

# 获取当天的准确时间
print(datetime.datetime.today())
print(datetime.datetime.now())

# 时间戳转换为日期
print(datetime.datetime.fromtimestamp(time.time()))

# 日期转时间戳
print(datetime.datetime.now().timestamp())

