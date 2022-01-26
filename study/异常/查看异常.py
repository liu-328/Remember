import traceback


def num(num1, num2):

    try:
        num = num1 + num2
        print(num)

    except Exception:
        #
        traceback.print_exc(file=open('error.text', 'w+'))
        # 返回异常信息输出到控制台
        print(traceback.format_exc())


num(1, "a")
