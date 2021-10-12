import message


message.send_message.send("hello")
# receive函数内有返回值，需要变量接受才可以打印
test = message.receive_message.receive()
print(test)

