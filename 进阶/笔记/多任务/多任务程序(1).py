# 多任务（同一时间内执行多个任务）（可以以最大程度利用cpu资源）（并发、并行）
# 并发：在同一时间内交替完成任务
# 并行：真正同时执行多个任务
# Python中多任务分为进程、线程
# 进程（process）是资源分配的最小单位，每个程序至少有1个进程
# 程序开始运行系统会默认创建一个主进程
# 多进程除创建主进程外，还有不少于1个的子进程
def main():
    import threading  # 线程包
    import time

    #  定义多个方法
    def sing():
        """唱歌5秒钟"""
        for i in range(5):
            print("唱歌")
            time.sleep(1)

    def dance():
        """跳舞5秒"""
        for i in range(5):
            print("跳舞")
            time.sleep(1)

    #  利用线程同时执行两个方法
    xc1 = threading.Thread(target=sing)
    xc2 = threading.Thread(target=dance)
    xc1.start()
    xc2.start()


if __name__ == '__main__':
    main()
