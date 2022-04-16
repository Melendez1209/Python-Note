# 导入需要的包
import random  # 导入随机包
import time

daan = random.randint(0, 100)  # 使用随机包生成一个0至100的数值
cishu = 0  # 定义次数
print("猜数字小游戏已开始，(您共有10次机会)祝您好运！！！")
# 提示
for cishu in range(10):
    caice = int(input("请输入0至100的一个整数"))  # 输入请求
    if caice > daan:  # 过大
        print("您的猜测过大！！！")
        print("机会-1，还剩", 10 - (cishu + 1), "次，祝您好运！！！")
    elif caice < daan:  # 过小
        print("您的猜测过小！！！")
        print("机会-1，还剩", 10 - (cishu + 1), "次，祝您好运！！！")
    else:  # 正确
        print("您猜对了！！！")
        time.sleep(3)
        break  # 终止循环
if cishu >= 10:
    print("您的10次机会用光了，游戏结束！！！")
