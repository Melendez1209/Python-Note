# 定义必要变量
demo1 = [1, 3, 5, 7, 9]
demo2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]


# 定义必要方法
# 欧几里德距离
def euclidean(p, q):
    # 如果两组数目不同，计算两者之间对应有的数
    same = 0
    for i in p:
        if i in q:
            same += 1
    # 计算并将其标准化
    e = sum([(p[i] - q[i]) ** 2 for i in range(same)])
    return 1 / (1 + e ** .5)


# 定义mian函数
def main():
    print(euclidean(demo1, demo2))


# 调用main函数
if __name__ == '__main__':
    main()
