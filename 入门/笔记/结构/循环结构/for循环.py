# for循环适用于知道循环次数的循环
for aa in range(10):  # 设变量为aa，循环为10次，aa为0 1 2 3 4 5 6 7 8 9
    print("第", aa + 1, "次打印hello world")
for ab in range(5, 10):  # 取5至10
    print("第", ab + 1, "次打印hello world")
for ac in range(5, 10, 2):  # 2为步长，每取一个值+2
    print(ac)

ad = (1, 2, 3)
for ae in ad:  # 除字典外，所有容器适用
    print(ae)
    print(ae + 1)
af = {"name": "jastin"}
for ag in af:  # 除字典外，所有容器适用
    print(ag)
    print(af[ag])
