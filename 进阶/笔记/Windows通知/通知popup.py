# 导入
from win10toast_click import ToastNotifier

# 弹出通知
toast1 = ToastNotifier()
toast1.show_toast('Python', '人生苦短我用Python', icon_path='D:\耿一铭\其他\开发\Python\python.ico', duration=5)
# 从左至右依次为：标题/内容/图标/时间
