import json

# 把 Python 转换为 JSON
# 若有 Python 对象，则可以使用 json.dumps() 方法将其转换为 JSON 字符串。
a = {
    "name": "苏格",
    "age": 12,
    "city": "Beijing"
}
b = json.dumps(a)
print(b)
