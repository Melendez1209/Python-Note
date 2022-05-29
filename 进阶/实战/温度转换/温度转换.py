#!/
# _*_coding: utf-8 _*_
# @Time :  15:24
# @Author : Mark Melendez
# @File : 温度转换.py
# @desc :
# -----------------------------begin-------------------------------
# 导入依赖包
import logging

import PySimpleGUI as gui

# 定义必要变量（函数等）
main_layout = [
    [gui.T("欢迎使用温度转换器！！！")],
    [gui.B("℉——>℃"), gui.B("℃——>℉")]
]

Transforms_Layout = [
    [gui.T("请键入温度(无需单位):"), gui.In()],
    [gui.B("确定")]
]


def transforms(title):
    tlwindow = gui.Window(title, Transforms_Layout)
    tlevent, tlvalue = tlwindow.read()
    if tlevent is None:
        logging.error("换算窗口关闭")
        tlwindow.close()
    if tlevent == "确定":
        # 判断数据可否转换为浮点型
        try:
            tlvalue = float(tlvalue[0])
            # 判断新数值的类型
            if title == "℉——>℃":
                new_value = (tlvalue - 32) / 1.8
            else:
                new_value = tlvalue * 1.8 + 32

        except:
            gui.popup("您键入了错误的数据！！！")
        return new_value


# 定义mian函数
def main():
    main_gui = gui.Window("温度转换器", main_layout)
    event, value = main_gui.read()

    if event is None:
        logging.error("关闭主窗口")
        main_gui.close()
    elif event == "℉——>℃":
        logging.error("℉——>℃")
        new_value = transforms("℉——>℃")
        main_gui.close()
        gui.popup(new_value)
    elif event == "℃——>℉":
        logging.error("℃——>℉")
        new_value = transforms("℃——>℉")
        main_gui.close()
        gui.popup(new_value)

    else:
        pass


# 调用main函数
if __name__ == '__main__':
    main()
