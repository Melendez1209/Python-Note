#!/
# _*_coding: utf-8 _*_
# @Time :  13:39
# @Author : Mark Melendez
# @File : 随机颜色.py
# @desc :
# -----------------------------begin-------------------------------
# 导入依赖包
import logging
import random

import PySimpleGUI as Gui

# 定义必要变量（函数等）

start_layout = [
    [Gui.CB('透明度')],
    [Gui.B('确定'), Gui.T('更多', enable_events=True)]
]


def creat_showwindow(color):
    show_layout = [[Gui.In(color)].copy()]
    return show_layout


# 随机选取颜色
def randomcolor(alpha):
    colorArr = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    color = ""
    if alpha:
        time = 8
    else:
        time = 6
    for i in range(time):
        color += colorArr[random.randint(0, 14)]
    return "#" + color


# 定义mian函数
def main():
    # 开始窗口
    start_window = Gui.Window('随机颜色', start_layout)
    start_event, start_values = start_window.read()
    # 窗口关闭
    if start_event is None:
        start_window.close()
        logging.error('start_window 关闭')
    # 随机随机选取颜色
    elif start_event == '确定':
        show_layout = creat_showwindow(randomcolor(start_values[0]))
        logging.error(start_values[0])
        show_windows = Gui.Window("最终颜色", show_layout)
        show_event, show_values = start_window.read()
        logging.error("show_windwo 打开")
        if show_event is None:
            show_windows.close()
        else:
            pass

        # start_window.close()
        # logging.error('start_window 关闭')
    else:
        Gui.Popup('本程序可用于，随机生成2进制颜色')


# 调用main函数
if __name__ == '__main__':
    main()
