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
import pyperclip
import webbrowser as web

import PySimpleGUI as Gui

# 定义必要变量（函数等）

Start_Layout = [
    [Gui.CB('透明度（勾选后将失去颜色参考SK选项）')],
    [Gui.B('确定'), Gui.T('更多', enable_events=True)]
]


def Creat_Showwindow(color, alpha):
    if alpha:
        Show_Layout = [
            [Gui.T(color), Gui.T("该结果已复制到您的剪贴板")],
            [Gui.B("复制到剪切板并关闭")]
        ]
    else:
        Show_Layout = [
            [Gui.T(color), Gui.T("该结果已复制到您的剪贴板")],
            [Gui.B("复制到剪切板并关闭"), Gui.B("了解更多关于此颜色的信息")]
        ]
    return Show_Layout


# 随机选取颜色
def RandomColor(alpha):
    ColorList = ["0", '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    color = ""
    if alpha:
        Number = 8
    else:
        Number = 6
    color = random.sample(ColorList, Number)
    result = "#" + "".join(color)
    return result


# 定义mian函数
def main():
    # 开始窗口
    Start_Window = Gui.Window('随机颜色', Start_Layout)
    Start_Event, Start_Values = Start_Window.read()
    # 窗口关闭
    if Start_Event is None:
        Start_Window.close()
        logging.error('start_window 关闭')
    # 随机随机选取颜色
    elif Start_Event == '确定':
        Result = RandomColor(Start_Values[0])
        Show_Layout = Creat_Showwindow(Result, Start_Values[0])
        logging.error(Start_Values[0])
        Show_Window = Gui.Window("最终颜色", Show_Layout)
        Show_Event, Show_Values = Show_Window.read()  # Show_Values没用，只是为了正确读取Show_Event
        logging.error("Show_Windwo 打开")

        if Show_Event is None:
            Show_Window.close()
            logging.error("Show_Window 关闭")
        elif Show_Event == "复制到剪切板并关闭":
            # 复制到剪切板
            pyperclip.copy(Result)
            logging.error("颜色已复制到剪贴板")
        elif Show_Event == "了解更多关于此颜色的信息":
            Url = "https://www.color-hex.com/color/" + Result[1:]
            web.open(Url)
            logging.error("已打开网页")

    else:
        Gui.Popup('本程序可用于，随机生成2进制颜色')


# 调用main函数
if __name__ == '__main__':
    main()
