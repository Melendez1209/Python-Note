# project name：BMI计算器
# time：2021/10/24/15/39/08
# write by Mark Melendez
# Version：v2.0 Bata1
# --------------------------begin-------------------------
# 导入需要的包
import ctypes
import PySimpleGUI as gui

# 定义
# 定义布局
# ZH-CN layout
cn = [
    [gui.Text('欢迎使用BMI计算器！！！')],
    [gui.Text('请输入您的身高（m）：'), gui.In('')],
    [gui.Text('请输入您的体重（kg）：'), gui.In('')],
    [gui.T('更多信息', enable_events=True)],
    [gui.B('        确认      '), gui.Quit('      取消      ')]
]

cn_more = [
    [gui.Text('     什么是BMI？', enable_events=True)],
    [gui.Text('     BMI计算标准', enable_events=True)],
    [gui.Text('     BMI水平划分标准', enable_events=True)],
    [gui.Text('     健身等特殊人群不适用！！！')],
    [gui.B('           切换至英文模式            ')]
]

# EN-US layout
en = [
    [gui.Text('Welcome to BMI calculator!!!')],
    [gui.Text('Please enter your height (m):'), gui.In('')],
    [gui.Text('Please enter your weight (kg):'), gui.In('')],
    [gui.T('More about BMI', enable_events=True)],
    [gui.B('        confirm      '), gui.Quit('      cancel      ')]
]
en_more = [
    [gui.Text('What is BMI?', enable_events=True)],
    [gui.Text('BMI calculation standard', enable_events=True)],
    [gui.Text('BMI level division standard', enable_events=True)],
    [gui.Text('Fitness and other special groups are not applicable!!!')],
    [gui.B('        Switch to Chinese mode        ')]
]


# 定义必要的方法
def zh_show(bmi, lx):
    bmi_text = '您的BMI约为：', bmi, '属于', lx, '水平'
    zh_show_layout = [[gui.T(bmi_text)],
                      [gui.Quit('欢迎下次使用！！！')]]
    zh_show_win = gui.Window('BMI计算结果', zh_show_layout)
    event = zh_show_win.read()
    if event is None:
        zh_show_win.close()


def us_show(bmi, lx):
    bmi_text = 'Your BMI is：', bmi, 'in the ', lx, '.'
    en_show_layout = [[gui.T(bmi_text)],
                      [gui.Quit('See you next time!!!')]]
    en_show_win = gui.Window('BMI计算结果', en_show_layout)
    event = en_show_win.read()
    if event is None:
        en_show_win.close()


# ZH-CN layout
def zh():
    window = gui.Window('BMI计算器', cn)
    # 接收返回值
    event, values = window.read()
    # 关闭
    if event is None:
        window.close()
    # 更多
    elif event == '更多信息':
        cn_more_win = gui.Window('更多信息', cn_more)
        cn_more_event = cn_more_win.read()
        if cn_more_event == '           切换至英文模式            ':
            us()
            window.close()
        elif cn_more_event == '     BMI计算标准':
            gui.popup('BMI=体重/（身高*身高）')
        elif cn_more_event == '     BMI水平划分标准':
            gui.popup('''
            偏轻 <18.5
            正常 18.5~23.9
            超重24.0~27.9
            肥胖>28.0
            ''')
        elif cn_more_event == '     什么是BMI？':
            gui.popup('BMI或身体质量指数是找出您的体重是否超重、过轻或理想的快速方法。')
    elif event == '        确认      ':
        gui.popup('确认提交')
        values[0] = float(values[0])
        values[1] = float(values[1])
        # 使用用户返回的信息进行计算
        bmi = float(values[1]) / (float(values[0]) * float(values[0]))
        bmi = round(bmi, 1)  # 保留2位小数
        # 判断结果的类型
        if bmi < 18.5:
            lx = '偏轻'
            zh_show(bmi, lx)
        elif 18.5 < bmi < 24:
            lx = '正常'
            zh_show(bmi, lx)
        elif 24 < bmi < 28:
            lx = '超重'
            zh_show(bmi, lx)
        else:
            lx = '过度肥胖'
            zh_show(bmi, lx)
    else:
        pass


def us():
    window = gui.Window('BMI Calculator', en)
    # 接收返回值
    event, values = window.read()
    if event is None:
        window.close()
    # 更多
    elif event == 'More about BMI':
        us_more_win = gui.Window('More about BMI', en_more)
        us_more_event = us_more_win.read()
        if us_more_event == '        Switch to Chinese mode        ':
            window.close()
            zh()
        elif us_more_event == 'BMI calculation standard':
            gui.popup('BMI = weight / (height * height)')
        elif us_more_event == 'BMI level division standard':
            gui.popup('''
Light < 18.5
Normal 18.5 ~ 23.9
Overweight 24.0 ~ 27.9
Obesity > 28.0
            ''')
        elif us_more_event == 'What is BMI?':
            gui.popup(
                'BMI or body mass index is an ideal quick way to find out if you are overweight, underweight or '
                'overweight.')
    elif event == '        confirm      ':
        gui.popup('Confirm submission')
        values[0] = float(values[0])
        values[1] = float(values[1])
        # 使用用户返回的信息进行计算
        bmi = float(values[1]) / (float(values[0]) * float(values[0]))
        bmi = round(bmi, 1)  # 保留2位小数
        # 判断结果的类型
        if bmi < 18.5:
            lx = 'Lighter'
            us_show(bmi, lx)
        elif 18.5 < bmi < 24:
            lx = 'normal'
            us_show(bmi, lx)
        elif 24 < bmi < 28:
            lx = 'overweight'
            us_show(bmi, lx)
        else:
            lx = 'Obesity'
            us_show(bmi, lx)
    else:
        pass


# 定义main函数
def main():
    # 系统语言获取
    dll_h = ctypes.windll.kernel32
    language = hex(dll_h.GetSystemDefaultUILanguage())
    # 中文
    if language == '0x804':
        zh()
    # 其他
    else:
        us()


# 调用main函数
if __name__ == '__main__':
    main()
