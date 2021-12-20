# 1.判断空白字符
space_str = "\t\r\n"

print(space_str.isspace())

# 2.判断字符串中是否只包含数字
# 都不能判断小数。
# num_str = "1.1"

# unicode 字符串
# num_str = "①"
# num_str = "\u00b2"

num_str = "一千零一"
print(num_str)
print(num_str.isdecimal())
print(num_str.isdigit())
print(num_str.isnumeric())

num_str.isdigit()  # 判断所有字符都是数字（整形）

num_str.isalnum()  # 判断所有字符都是数字或者字母

num_str.isalpha()  # 判断所有字符都是字母

num_str.islower()  # 判断所有字符都是小写

num_str.isupper()  # 判断所有字符都是大写

num_str.istitle()  # 判断所有单词都是首字母大写


def isfloat(str_num):
    s = str_num.split('.')
    if len(s) > 2:
        return False
    else:
        for int_str in s:
            if int_str.isdigit() is False:
                return False
        return True


a = '3.12a'
print(isfloat(a))