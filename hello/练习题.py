# 打印99乘法表
for i in range(1, 10):
    for a in range(1, i + 1):
        print(a, '*', i, '=', i * a, end=' ')
    print('')

a = 1
while a < 10:
    i = 1
    while i < a + 1:
        print(a, '*', i, '=', a * i, end=' ')
        i += 1
    a += 1
    print('')

# 冒泡排序

def maopao(a):

    n = len(a)

    for i in range(n):
        for j in range(0, n - i - 1):

            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]


a = [1, 4, 5, 6, 8, 9, 3, 2, 7]

maopao(a)

for i in range(len(a)):
    print("%d" % a[i])