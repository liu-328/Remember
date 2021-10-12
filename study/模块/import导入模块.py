import 测试模块1
# 起别名
import 测试模块2 as Test

测试模块1.say_hello()
Test.say_hello()

dog = 测试模块1.Dog()
print(dog)

cat = Test.Cat()
print(cat)
























