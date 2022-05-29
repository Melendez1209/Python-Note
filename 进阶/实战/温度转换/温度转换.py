#!/
# _*_coding: utf-8 _*_
# @Time :  15:24
# @Author : Mark Melendez
# @File : 温度转换.py
# @desc :
# -----------------------------begin-------------------------------
# 导入依赖包
import PySimpleGUI as gui

# 定义必要变量（函数等）
main_layout = [
    [gui.T("欢迎使用温度转换器！！！")],
    [gui.B("℉——>℃"), gui.B("℃——>℉")]
]


# 定义mian函数
def main():
    main_gui = gui.Window("温度转换器", main_layout)
    event, values = main_gui.read()
    if event is None:
        main_gui.close()


# 调用main函数
if __name__ == '__main__':
    main()
