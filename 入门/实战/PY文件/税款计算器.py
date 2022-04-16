print("欢迎使用苏格个人所得税问题计算器")
print("税收类型：个人所得税")
sqgz = float(input("请输入您的税前收入："))  # 税前收入
shebao = float(input("请输入您的各项社会保险费用："))  # 社保
qzd = 5000
print("起征点：", qzd, "元")
sk = 0  # 税金
ynse = sqgz - shebao - qzd  # 到手工资
if ynse <= 3000 and ynse > 0:
    sk = ynse * 0.03 - 0
elif ynse <= 12000:
    sk = ynse * 0.1 - 210
elif ynse <= 25000:
    sk = ynse * 0.2 - 1410
elif ynse <= 35000:
    sk = ynse * 0.25 - 2660
elif ynse <= 55000:
    sk = ynse * 0.3 - 4410
elif ynse <= 80000:
    sk = ynse * 0.35 - 7160
elif ynse > 80000:
    sk = ynse * 0.45 - 15160
print("您的应纳税额：", sk, "元")
print("您的到手工资：", sqgz - shebao - sk, "元")
