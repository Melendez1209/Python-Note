# 导入需要的包
import turtle
from time import sleep

# 定义
# 画布
turtle.screensize(1000, 2000, 'pink')  # 长800，宽600 ，底色：粉
# 画笔
turtle.pensize(5)  # 宽度
turtle.pencolor('red')  # 颜色
turtle.speed(5)  # 速度（1-10）


# 使用main函数绘画五角星
def main():
    for tc in range(5):
        turtle.forward(200)  # 移动200像素
        turtle.right(144)  # 顺时针旋转画笔144度
    sleep(3)


if __name__ == '__main__':
    main()
