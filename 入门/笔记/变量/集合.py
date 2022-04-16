# 集合（set）（col）
n = {1, 2, 3, 4, 5, "上山打老虎"}
r = {4, 5, 6, 7}
print(n)
o = set([1, 2, 3, 4, 5])  # 只保留n集合中的1,2,3,4,5项目
print(n, o)
p = set(list1)  # 去除p列表中的重复部分，形成集合形式
print(p)
q = list(p)  # 还原p集合为列表
print(q)
print(n - r)  # 打印n集合与b集合的不同部分！！
