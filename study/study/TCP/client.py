import socket

tcpclient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpclient.connect(('127.0.0.1', 8080))

while True:
    data = input("请输入要发送的数据:")
    tcpclient.send(data.encode('utf-8'))
    info = tcpclient.recv(1024)
    print("服务器说:",info.decode('utf-8'))
