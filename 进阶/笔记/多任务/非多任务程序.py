import time


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


sing()
dance()
