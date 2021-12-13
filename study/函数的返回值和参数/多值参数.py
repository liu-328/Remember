def demo(num, *nums, **person):

    print(num)
    print(nums)
    print(person)


# demo(1)
demo(1, 2, 3, 4, 5, name='小明', age=18)


# 命名关键字参数
def demo1(name, phone, *, age, nums):
    a = [name, phone, age, nums]
    c = ['name', 'phone', 'age', 'nums']
    print(name, phone, age, nums)
    b = {}
    for i in range(len(c)):
        b[c[i]] = a[i]
    print(b)


demo1('小刘', 123, age=18, nums=222)


def message(*, after: int, before: int, **kwargs):

    a = kwargs
    ranges = after - before
    print(ranges)
    print(a)


message(after=18000, before=10000, name='小刘', age=18, classroom=1)


def digui(n):

    if n == 1:
        return 1

    return n * digui((n - 1))


print(digui(5))


def fib(n):

    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


nums = []

for i in range(0, 10):
    nums.append(fib(i))

print(nums)



