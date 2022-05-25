# RegEx 或正则表达式是形成搜索模式的字符序列。
# RegEx 可用于检查字符串是否包含指定的搜索模式。
import re

txt = "China is a great country"
jieguo = re.search("^China.*country$", txt)  # 检索字符串以查看它是否以 "China" 开头并以 "country" 结尾

if jieguo:
    print("Yes")
else:
    print("No")
