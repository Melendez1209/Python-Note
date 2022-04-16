# 类（在里面定义函数并在全局使用，第一个要用__init__(self)初始化）
class diyigelei(object):  # class:创建一个类跟类的名字 object：父类
    def __init__(self, name, age):
        self._name = name  # self:初始化
        self._age = age

    # 类的封装
    def _name_age(self):  # 封装方法
        return "name:%s,age:%s"  # 封装完成


# 类的继承
# 若没有指令类的父类，则为object类
class a:
    pass


class b:
    pass


class c(a, b):
    pass


print(a.__bases__)  # 打印出a的所有父类
print(c.__bases__)  # 打印出c的所有父类
print(c.__base__)  # 只打印出c的一个父类（定义多个时的第一个）
