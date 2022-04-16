# 文件读写
# mode用法
# w 只能操作写入  r 只能读取   a 向文件追加
# w+ 可读可写   r+可读可写    a+可读可追加
# w模式打开文件，如果而文件中有数据，再次写入内容，会把原来的覆盖掉
# wb 二进制

# 文件读取
hello = open("hello.txt", mode="r", encoding="utf8")  # r:读取 encoding:编码（后输入对应格式）
print(hello.read())
hello.close()  # 关闭文件（为了方便）
