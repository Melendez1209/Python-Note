import time

# card：卡  mima：密码  ye：余额
# 定义已注册银行卡
# 卡1信息
card1 = "1001"
mima1 = "123456"
ye1 = 1000
# 卡2信息
card2 = "1002"
mima2 = "147852"
ye2 = 1050
# 卡3信息
card3 = "1003"
mima3 = "120973"
ye3 = 1200
# 运行代码
print("欢迎使用苏格银行网上业务处理器")
cwcs = 1  # 错误次数
while True:
    # 信息输入请求
    card = input("请输入您的银行卡号：")
    mima = input("请输入您的银行卡密码：")
    # 判断信息归属
    ye = 0
    # 输入正确
    if card == card1 and mima == mima1:
        ye = ye1
    elif card == card2 and mima == mima2:
        ye = ye2
    elif card == card3 and mima == mima3:
        ye = ye3
    # 输入有误
    else:

        cwcs = cwcs + 1
        if cwcs >= 3:
            print("您已连续错误输入3次，请联系客服或服务人员进行处理！")
            break
        else:
            print("您的卡号或密码输入错误，请重新输入！")
            continue
    # 系统提示
    while True:
        yw = input("请输入您所需办理的业务（01：存款 02：取款 03：账户余额查询 04：取出银行卡 ）：")  # 业务输入请求
        # 判断业务类型，并执行
        if yw == "01":
            cun = float(input("请输入存款金额："))
            if cun <= 0:
                print("存款金额输入有误！")
                time.sleep(1)
                continue
            else:
                ye = ye + cun
                print("存款成功！账户余额", ye, "元！")
        elif yw == "02":
            qu = float(input("请输入取款金额："))
            if qu < ye:
                print("余额不足，即将返回！")
                time.sleep(1)
                continue
            else:
                ye = ye - qu
                print("取款成功！账户余额", ye, "元！")
        elif yw == "03":
            print(ye, "元")
        elif yw == "04":
            print("请保存好银行卡，欢迎下次使用！")
            break
        else:
            print("输入有误！")
            continue
