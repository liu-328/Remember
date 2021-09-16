def sum_number(num):

    print(sum)
    # 递归的出口，当满足某个条件时，不在执行函数。
    if num == 1:
        return

    sum_number(num - 1)


sum_number(3)
















