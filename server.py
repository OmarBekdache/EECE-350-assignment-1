import socket
import datetime

serverSocket = socket.socket (socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind ( ('127.0.0.1' , 12345) )

while True:
    data, address = serverSocket.recvfrom(1024)
    time = datetime.datetime.now()
    print('Request received on', time)
    serverSocket.sendto(data, address)




