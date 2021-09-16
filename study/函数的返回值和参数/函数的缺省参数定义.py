# 定义函数的时候带有默认值的参数，应该放在没有缺省参数的后面
def print_info(name, tittle='', gender=True):
    """

    :param tittle: 职位
    :param name: 班上用血的姓名
    :param gender:Ture，表示男， False 为女
    """

    gender_test = "男生"

    if not gender:
        gender_test = '女生'

    print("[%s]%s 是 %s" % (tittle, name, gender_test))


# 假设班上的同学男生居多
# 提示：在指定缺省参数的默认值时，应该使用最常见的值作为默认值。
print_info("小明")
print_info("老王")
# 调用多个缺省函数的参数时候，如果需要指定参数名需要跟上等号，等号后面跟上具体的实参
print_info("小妮", gender=False)















