# 实用内置模块
import os  # 系统模块

os.system("D:\Codes\Python\入门\笔记\实用内置模块\hi.txt")  # 打开这个文件
os.rename("D:\Codes\Python\入门\笔记\实用内置模块\hi.txt", "D:\Codes\Python\入门\笔记\实用内置模块\hello.txt")  # 更改文件名

import webbrowser as web  # 浏览器控制模块

web.open("www.baidu.com")  # 打开百度官网
