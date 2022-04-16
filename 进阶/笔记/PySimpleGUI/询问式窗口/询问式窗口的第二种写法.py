# 导入需要的包
import PySimpleGUI as tc

# 用变量记录窗口中要显示的文字
wz = [
    [tc.Text('请输入基本信息！！！')],
    [tc.Text('姓名：', enable_events=True), tc.In('张某某')],  # enable_events=True（打开了对于此项的事件）
    [tc.Text('年龄：'), tc.In('12')],
    [tc.Text('身高（cm）：'), tc.In('165')],
    [tc.Text('体重（kg）：'), tc.In('51')],
    [tc.Text('感谢您的配合！！！')],
    [tc.B('确认'), tc.B('取消')],
    [tc.B('确认2'), tc.B('2取消')]
]


# 创建main函数
def main():
    # 创建窗口
    window = tc.Window('Python', wz)  # Window（窗口中询问）
    # 事件循环
    while True:
        # 获取
        event, valuse = window.read()
        # 判断事件
        if event.endswith('取消'):  # endswith（结尾一致）
            tc.popup('您执行了取消的相关选项！！！')
            break
        elif event.startswith('确认'):  # startswith(开头一致)
            tc.popup('您执行了确认的相关选项！！！')
            print(valuse)
        elif event == '姓名':
            tc.Text('请输入您的姓名！！！')
        else:
            break
    window.close()


if __name__ == '__main__':
    main()
