# 1.打开文件
file_read = open("readme")
# 只写文件
file_write = open("readme[附件]", "w")
# 2.读写文件
test = file_read.read()
# 只写文件调用写入方法，传入读到的文件
file_write.write(test)

# 3.关闭文件
file_read.close()
file_write.close()












