# 使用多个键值对，存储描述一个 '物体' 的相关信息 ---描述更复杂的信息。
# 将 多个字典 放在一个列表中，再进行遍历
card_list = [
    {'name': '张三',
     'QQ': '12345',
     'phone': '10086'},
    {'name': '李四',
     'QQ': '54321',
     'phone': '10010'}
]
print(type(card_list))  # <class 'list'>

for card_info in card_list:

    print(card_info)











