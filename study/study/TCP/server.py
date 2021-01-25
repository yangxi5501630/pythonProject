import socket

tcpserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpserver.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) #地址重复使用
tcpserver.bind(('127.0.0.1', 8080))
tcpserver.listen(5)
tcpclient, tcpclientaddr = tcpserver.accept()

while True:
    data = tcpclient.recv(1024)
    print("客户端说:",data.decode('utf-8'))
    msg = input("请输入回应信息:")
    tcpclient.send(msg.encode('utf-8'))
