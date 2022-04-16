# while循环
ah = 0
for ai in range(101):
    ah = ah + ai  # 为ah自己赋值
print(ah)
# 使用for循环取列表最大值
aj = [3090, 4399, 7723]  # 要求的列表
ak = aj[0]  # 假设最大值为aj中的第一个
al = 0
while al < 100:  # while循环不会自动停止，除非不满足条件
    print(al)
    al = al + 10
    if al == 90:
        print("中场休息")

yuefen = 1
gongzi = 0
while yuefen <= 12:
    tian = 1
    print(yuefen, "月到了")
    if yuefen == 2:
        print("本月失业，无收入")
        yuefen = yuefen + 1
        continue  # 结束本次循环，直接开始下一次（本行后面代码皆不执行（仅限本次））
    while tian <= 30:
        gongzi = gongzi + 0.04
        print("第", yuefen, "月""第", tian, "天""支付工资1.2万元，已累计支付工资", round(gongzi, 2), "元")  # roound对gongzi保留小数1（计算机语言写2）位
        tian = tian + 1
yuefen = 1
gongzi = 0
while yuefen <= 12:
    tian = 1
    print(yuefen, "月到了")
    if yuefen == 2:
        print("本月失业，无收入")
        yuefen = yuefen + 1
        break  # 结束循环
    while tian <= 30:
        gongzi = gongzi + 0.04
        print("第", yuefen, "月""第", tian, "天""支付工资1.2万元，已累计支付工资", round(gongzi, 2), "元")  # roound对gongzi保留小数1（计算机语言写2）位
        tian = tian + 1
