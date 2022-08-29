#!/
# _*_coding: utf-8 _*_
# @Time :  上午 9:30
# @Author : Mark Melendez
# @File : 剪切板操作.py
# @desc :
# -----------------------------begin-------------------------------
# 导入依赖包
import pyperclip


# 定义mian函数
def main():
    pyperclip.copy("Hello World")
    print("已将" + pyperclip.waitForPaste(1) + "添加到剪贴板")  # 等待1s，若剪切板仍为空，则抛出异常


# 调用main函数
if __name__ == '__main__':
    main()
