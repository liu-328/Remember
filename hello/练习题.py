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

