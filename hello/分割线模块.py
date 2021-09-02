def print_line(char, times):
    """打印单行分割线

    :param char:分隔字符
    :param times:分割次数
    """
    print(char * times)


def print_lines(char, times):
    """打印多行分割线

    :param char:分割线使用的分隔字符
    :param times:分割线重复次数
    """
    row = 1
    while row < 6:

        print_line(char, times)

        row += 1


name = '刘诗佳'
