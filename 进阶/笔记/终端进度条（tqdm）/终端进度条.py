#!/
# _*_coding: utf-8 _*_
# @Time :  10:19
# @Author : Mark Melendez
# @File : 终端进度条.py
# @desc :
# -----------------------------begin-------------------------------
# 导入依赖包
from time import sleep

import tqdm


# 定义mian函数
def main():
    # 创建进度条
    bar = tqdm.tqdm(total=100)
    # 添加进度条
    for i in range(100):
        bar.update(1)
        sleep(0.1)
    # 关闭进度条
    bar.close()


# 调用main函数
if __name__ == '__main__':
    main()
