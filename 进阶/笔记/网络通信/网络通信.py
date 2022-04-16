# 网络通信（常用两种为：udp、tcp）
# ip地址用来标记网络上的一台设备（不重复)（dest ip:目标ip）（src ip：源ip）
# 端口号：用来标记一台设备上的进程（dest port：目标端口号）（src port：源端口号）（端口号<1023的端口都是知名端口）（端口最大65535）（非知名端口为动态端口，随便用）
# socket（接口）只有通过socket才可以实现网络通信
# 发送
import socket

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # 创建接口 AF_INET(ipv4协议) SOCK_STREAM（tcp）SOCK_DGRAM（udp）
# 收送数据
udp.sendto(b"haha haha", ("192.168.137.1", 7788))  # 向192.168.137.1的7788端口发送hahahaha，b为发送形式
# 关闭接口
udp.close()

# 接收
js = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 固定端口号并接收
dz = ('', 7788)  # ip和端口，ip自动获取（不写)
js.bind(dz)
shuju = js.recvfrom(1024)  # recvfrom(接收)（接受到的是元组，里边有发送方的ip和端口） 1024（接受的最大字节数）
# 存储发送内容
nr = shuju[0]
# 存储发送地址
dz = shuju[1]
# 打印接收到的数据
print("%s%s" % (str(dz), nr.decode("gbk")))  # "%s%s"(打印格式) decode（解码）gbk（Windows默认编码格式）
# 关闭套接字
js.close()
