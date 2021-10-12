# 注意事项
# 首先在模块1导入say_hello,第二次导入模块2的say_hello会被覆盖
# 如果想用模块1的函数是用起别名的方式去调用
from 测试模块1 import say_hello as say_hello1
from 测试模块2 import say_hello


say_hello()
say_hello1()




