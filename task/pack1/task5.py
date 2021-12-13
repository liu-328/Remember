"""
1、打印如下结果：
1*5=5
2*10=20
3*15=45
...
10*50=500
"""
import json
import time

i = 0
for j in range(1, 51):
    if j % 5 == 0:
        i += 1
        print(i, '*', j, '=', (i * j))

"""
2、本金10000元存入银行，年利率是千分之三，每过1年，将本金和利息相加作为新的本金。计算5年后，获得的本金是多少？
"""

sum = 10000
year = 1
while year < 6:
    sum = sum + sum * 0.003
    year += 1

print(sum)

"""
3、计算1900年1月1日到今天(如：2019年12月20日)相距多少天。
"""


def sum_day():
    years = int(time.strftime('%Y'))
    months = int(time.strftime('%m'))
    days = int(time.strftime('%d'))
    print(type(years), type(months), type(days))
    run_days = []
    month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
    total_months_days = 0
    for all_years in range(1900, years + 1):
        if all_years % 4 == 0 and all_years % 100 != 0 or all_years % 400 == 0:
            run_days.append(0)
    total_years_days = len(run_days) + (years - 1900) * 365
    for m in month_days[0: months]:
        total_months_days += m
    if years % 4 == 0 and years % 100 != 0 or years % 400 == 0:
        run_months_days = total_months_days + 1
        print(run_months_days + total_years_days + days)
    else:
        print(total_months_days + total_years_days + days)


sum_day()

"""
4、打印如下图案：
*
**
***
****
*****
"""

for i in range(1, 6):
    print('*' * i)

"""
5、打印如下图案：
*
***
*****
*******
*********
"""

for v in range(0, 10):
    if v % 2 != 0:
        print('*' * v)

"""
6、打印如下图案：
#####*
####***
###*****
##*******
#*********
"""
c = 6
for v in range(0, 10):
    if v % 2 != 0:
        c -= 1
        print(('#' * c) + ('*' * v))

"""
7、打印如下图案：
     *
    ***
   *****
  *******
 *********
  *******
   *****
    ***
     *
"""

a = []
for g in range(0, 10):
    if g % 2 != 0:
        print(str('*' * g).center(10, ' '))
for h in range(0, 8):
    if h % 2 != 0:
        a.append(h)
        a.sort(reverse=True)
for l in a:
    print(str('*' * l).center(10, ' '))

"""
8、打印99乘法表
"""

for aa in range(1, 10):
    for cc in range(1, aa + 1):
        print("%d * %d = %d" % (cc, aa, aa * cc), end=' ')
    print("")

"""
9、定义一个List，任意输入10个数字保存到List，然后按从小到大排序。（冒泡排序）
"""


def maopao(x):
    for i in range(len(x)):
        for ii in range(0, len(x) - i - 1):
            if a[ii] > a[ii + 1]:
                a[ii], a[ii + 1] = a[ii + 1], a[ii]
    print(x)


a = [5, 21, 23, 123, 64, 12, 1, 3, 54, 1]
maopao(a)


