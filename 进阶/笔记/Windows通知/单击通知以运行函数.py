# 导入
from win10toast_click import ToastNotifier
from PySimpleGUI import popup


def p():
    popup('hello')


# 弹出通知
toast1 = ToastNotifier()
toast1.show_toast(title='Python', msg='人生苦短我用Python', icon_path='D:\Codes\Python\python.ico', duration=5,
                  threaded=True,
                  callback_on_click=p)
