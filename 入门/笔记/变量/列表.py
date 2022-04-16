# 列表(list)
k = [2, 3, 9, 8, 6, 0, 1]  # 定义一个列表
print(k)  # 打印h这个列表
print(k[3])  # 打印h这个列表中的第4个项目
print(k[0:4])  # 打印h列表中的第1至4第个项目
print(k[-4:-1])  # 打印倒数第2至倒数第4个项目
print(k[-4])  # 打印倒数第4个项目
k.append("hello world")  # 在h列表中最后位置添加一个项目为hello world
print(k)
k.remove(3)  # 删除h列表中的3这个项目
print(k)
del k[2]  # 删除h列表中的第3个项目
print(k)
k.pop(4)  # 删除h列表中的第5个项目
print(k)
list1 = [1, 1]
p = set(list1)  # 去除p列表中的重复部分，形成集合形式
print(p)
q = list(p)  # 还原p集合为列表
print(q)
