from distutils.core import setup


setup(name="message",  # 包名
      version="1.0",  # 版本
      description="发送和接收消息模块",  # 描述信息
      long_description="完整的发送和接收消息模块",  # 完整的描述信息
      author="小刘",  # 作者
      url="主页暂无",  # 主页
      py_modules=["message.send_message",
                  "message.receive_message"])
