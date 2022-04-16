# 文件读写
# mode用法
# w 只能操作写入  r 只能读取   a 向文件追加
# w+ 可读可写   r+可读可写    a+可读可追加
# w模式打开文件，如果而文件中有数据，再次写入内容，会把原来的覆盖掉
# wb 二进制
# 二进制读写使用wb关键字，其余一致

# 文件写入1
hello2 = open("hello.txt", mode="w", encoding="utf8")  # w：写入
hello2.write("人生苦短，我用python")
print(hello2)
hello2.close()

# 文件写入2（追加）
hello3 = open("hello.txt", mode="a+", encoding="utf8")  # w：写入
hello3.write("""
hello
我是苏格""")
