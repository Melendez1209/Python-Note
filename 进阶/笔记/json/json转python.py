# JSON 是用于存储和交换数据的语法。
# JSON 是用 JavaScript 对象表示法（JavaScript object notation）编写的文本。
import json

# 若有 JSON 字符串，则可以使用 json.loads() 方法对其进行解析。

x = '{"name": "苏格", "age": 12, "city": "Beijing"}'
y = json.loads(x)
print(y["age"])
