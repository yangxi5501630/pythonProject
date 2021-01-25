import socket

udpclient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    data = input("请输入发送的数据:")
    udpclient.sendto(data.encode('utf-8'), ('127.0.0.1', 8080))