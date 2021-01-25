import socket

#AF_INET:IPV4
udpserver = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpserver.bind(('127.0.0.1', 8080))
while True:
    data, addr = udpserver.recvfrom(1024)
    print("客户端说:", data.decode('utf-8'))

