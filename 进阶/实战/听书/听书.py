# project name：听书
# time：2021/10/24/15/39/08
# write by Mark Melendez
# --------------------------begin-------------------------
# 导入需要的包
import PySimpleGUI as gui
import pyttsx3 as say  # 语音包

# 定义参数
# 窗口

start = [[gui.T('欢迎使用听书APP！！！')],
         [gui.T('请您设置语速（最小值1 建议值130)：')],
         [gui.In('')],
         [gui.T('请您设置循环次数：')], [gui.In('')],
         [gui.T('请将您的听书原文复制到下方！！！')],
         [gui.In('')],
         [gui.T('请调整好音量，您的听书之旅即将开始！！！')],
         [gui.T('祝您听书愉快！！！')],
         [gui.B('          确定          ')], [gui.B('          取消          ')],
         ]

# 语音
engine = say.init()  # 初始化
rate = engine.getProperty('rate')  # 语速属性获取


# 定义main函数
def main():
    # 窗口
    window = gui.Window('听书', start)
    event, values = window.read()
    # 窗口返回值判断
    # 软件关闭
    if event is None or event == '          取消          ':
        window.close()
        gui.popup('欢迎您下次使用！！！')
        # 语速输入错误
    elif values[0] is None:
        values[0] = 130
    elif event == '          确定          ':
        cs = int(values[1])
        ys = int(values[0])
        window.close()
        if ys < 1:
            engine.say('您的语速输入有误，软件自动关闭')
            window.close()
            # 软件正常运行
            # 朗读
        else:
            engine.say('进入屏保可停止程序运行，现在您的听书之旅开始了')
            engine.setProperty('rate', ys)  # 语速设定
            for a in range(cs):
                engine.say(values[2])
                engine.runAndWait()
                window.close()
    else:
        pass


# 调用main函数
if __name__ == '__main__':
    main()
