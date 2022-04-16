# project name：BMI计算器
# time：2021/10/24/15/39/08
# write by Mark Melendez
# --------------------------begin-------------------------


# 导入需要的包
import PySimpleGUI as gui
import ctypes

# 定义
# 定义窗口的内容
# ZH-CN layout
cn = [[gui.Text('欢迎使用BMI计算器！！！')],
      [gui.Text('请输入您的身高（m）：'), gui.In('')],
      [gui.Text('请输入您的体重（kg）：'), gui.In('')],
      [gui.Text('什么是BMI？', enable_events=True)],
      [gui.Text('BMI计算标准', enable_events=True)],
      [gui.Text('BMI水平划分标准', enable_events=True)],
      [gui.Text('健身等特殊人群不适用！！！')],
      [gui.B('          切换至英文模式           ')],
      [gui.B('        确认      '), gui.Quit('      取消      ')]
      ]

# EN-US layout
en = [[gui.Text('Welcome to BMI calculator!!!')],
      [gui.Text('Please enter your height (m):'), gui.In('')],
      [gui.Text('Please enter your weight (kg):'), gui.In('')],
      [gui.Text('What is BMI?', enable_events=True)],
      [gui.Text('BMI calculation standard', enable_events=True)],
      [gui.Text('BMI level division standard', enable_events=True)],
      [gui.Text('Fitness and other special groups are not applicable!!!')],
      [gui.B('        Switch to Chinese mode        ')],
      [gui.B('        confirm      '), gui.Quit('      cancel      ')]
      ]


# 定义必要的方法
def jg(bmi, lx):
    gui.popup('您的BMI约为：', bmi, '属于', lx, '水平')
    gui.popup('感谢使用！！！')


# ZH-CN layout
def ZH():
    window = gui.Window('BMI计算器', cn)
    # 接收返回值
    event, values = window.read()
    if event is None:
        window.close()
    if event == '          切换至英文模式           ':
        window.close()
        US()
    elif event == 'BMI计算标准':
        gui.popup('BMI=体重/（身高*身高）')
    elif event == 'BMI水平划分标准':
        gui.popup('''
        偏轻 <18.5
        正常 18.5~23.9
        超重24.0~27.9
        肥胖>28.0
        ''')
    elif event == '什么是BMI？':
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
            jg(bmi, lx)
        elif 18.5 < bmi < 24:
            lx = '正常'
            jg(bmi, lx)
        elif 24 < bmi < 28:
            lx = '超重'
            jg(bmi, lx)
        else:
            lx = '过度肥胖'
            jg(bmi, lx)
    else:
        pass


def US():
    window = gui.Window('BMI Calculator', en)
    # 接收返回值
    event, values = window.read()
    if event is None:
        window.close()
    if event == '        Switch to Chinese mode        ':
        window.close()
        ZH()
    elif event == 'BMI calculation standard':
        gui.popup('BMI = weight / (height * height)')
    elif event == 'BMI level division standard':
        gui.popup('''
        Light < 18.5
        Normal 18.5 ~ 23.9
        Overweight 24.0 ~ 27.9
        Obesity > 28.0
        ''')
    elif event == 'What is BMI?':
        gui.popup(
            'BMI or body mass index is an ideal quick way to find out if you are overweight, underweight or overweight.')
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
            jg(bmi, lx)
        elif 18.5 < bmi < 24:
            lx = 'normal'
            jg(bmi, lx)
        elif 24 < bmi < 28:
            lx = 'overweight'
            jg(bmi, lx)
        else:
            lx = 'Obesity'
            jg(bmi, lx)
    else:
        pass


# 定义main函数
def main():
    # 系统语言获取
    dll_h = ctypes.windll.kernel32
    language = hex(dll_h.GetSystemDefaultUILanguage())
    # 中文
    if language == '0x804':
        ZH()
    # 其他
    else:
        US()


# 调用main函数
if __name__ == '__main__':
    main()
