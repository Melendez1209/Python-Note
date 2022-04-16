# 导入需要的包
import socket
import time


def fasong(udp):
    """发送消息"""
    # 询问对方ip、port
    df_ip = input("请输入对方的ip地址：")
    df_port = int(input("请输入对方的固定端口："))
    # 询问要发送的信息
    xx = input("请输入您要想对方发送的信息：")
    # 实现发信息
    udp.sendto(xx.encode("gbk"), (df_ip, df_port))


def shou(udp):
    """接收消息"""
    # 实现收信息
    jieshou = udp.recvfrom(10240)
    # 打印收到的信息
    print("%s:%s" % (str(jieshou[1]), jieshou[0].decode("gbk")))


def main():
    # 欢迎使用
    print("欢迎使用苏格聊天APP！！！")
    # 创建套接字
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 绑定端口
    udp.bind(("", 8080))
    # 使用循环实现收发信息
    while True:
        # 欢迎使用
        print("-------欢迎使用苏格聊天器-------")
        # 判断需求
        print("1.接收消息")
        print("2.发送消息")
        print("0.退出应用")
        xq = int(input("请输入您的需求"))

        if xq == 1:
            shou(udp)
        elif xq == 2:
            fasong(udp)
        elif xq == 0:
            print("---------欢迎下次使用苏格聊天器！！！---------")
            time.sleep(3)
            break
        else:
            print("您的输入有误！！！")
            print("请重新输入...")
        # 关闭套接字
        udp.close()


if __name__ == '__main__':
    main()
