#!/
# _*_coding: utf-8 _*_
# @Time :  下午 12:39
# @Author : Mark Melendez
# @File : 拼音转换器.py
# @desc :
# -----------------------------begin-------------------------------
# 导入依赖包
import time

import PySimpleGUI as Gui
import pyperclip
from xpinyin import Pinyin

# 定义必要变量（函数等）
p = Pinyin()

MainPage = [
    [Gui.T("欢迎使用拼音转换器~")],
    [Gui.T("在这里输入要转换的内容："), Gui.In()],
    [Gui.B("确定")]
]


# 定义mian函数
def main():
    # 创建窗口
    MainWindow = Gui.Window("拼音转换器", MainPage)
    event, value = MainWindow.read()
    # 窗口事件处理
    if event is None:
        MainWindow.close()
    elif event == "确定":
        if value[0] == "":
            Gui.popup("您输入了不可转换的数据类型")
        else:

            try:

                result = p.get_pinyin(value[0], " ")
                pyperclip.copy(result)

                ResultPage = [
                    [Gui.T(result)],
                    [Gui.T("该结果已复制到您的剪贴板")]
                ]
                ResultWindow = Gui.Window("转换结果页", ResultPage)
                ResultEvent, ResultValue = ResultWindow.read()
                if ResultEvent is None:
                    ResultWindow.close()
                else:
                    pass

            except:
                Gui.popup("您输入了不可转换的数据类型")
            MainWindow.close()
    else:
        pass


# 调用main函数
if __name__ == '__main__':
    main()
