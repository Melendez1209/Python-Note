#!/
# _*_coding: utf-8 _*_
# @Time :  13:39
# @Author : Mark Melendez
# @File : 随机颜色.py
# @desc :
# -----------------------------begin-------------------------------
# 导入依赖包
import PySimpleGUI as gui

# 定义必要变量（函数等）
start_layout = [
    [gui.CB('透明度')],
    [gui.B('确定')]
]


# 定义mian函数
def main():
    start_window = gui.Window('随机颜色', start_layout)
    start_event, start_values = start_window.read()


# 调用main函数
if __name__ == '__main__':
    main()
