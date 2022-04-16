import time

while 1 == 1:
    print("欢迎使用苏格快递价格计算器")
    kuaidizhongliang = int(input("请输入快递重量（kg）"))
    mudidi = input("请输入目的地（01.国内；02.国外）")
    jiage = 0
    if kuaidizhongliang >= 3:
        if mudidi == "01":
            p = 12
        else:
            p = 20
    elif kuaidizhongliang < 3:
        if mudidi == "01":
            p = 4
        else:
            p = 6
    elif kuaidizhongliang == 0:
        print("您的输入有误")
    print("您好，此件包裹价格为", p, "元。")
    time.sleep(1)
