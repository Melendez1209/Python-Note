# 选择结构（if结构）
cunkuan = int(input("请输入您的存款金额"))  # 接受用户的键盘输入
zizhu = int(input("请输入亲友对您的资助金额"))
if cunkuan > 1000000:  # 如果cunkuan大于1000000
    print("去买宝马")
    if zizhu >= 500000:  # 在满足上一个条件下zizhu大于或等于500000
        print("买宝马五系")
    elif zizhu >= 300000:  # 在满足上一个条件下zizhu大于或等于300000
        print("买宝马三系")
    else:
        print("还是去买二手的吧")
else:  # 否则
    print("不去买宝马！")
if cunkuan <= 1000000 and cunkuan > 500000:  # 如果cunkuan小于或等于1000000并等于500000
    print("去买丰田！")
elif cunkuan > 1000000:  # 多选项使用elif
    print("去买宝马！")
elif cunkuan > 500000:
    print("去买丰田！")

    if True:
        pass  # 选择结构中无需执行任务
