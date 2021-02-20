import socket
import datetime

clientSocket = socket.socket (socket.AF_INET, socket.SOCK_DGRAM)
echoServerIP = input("Enter the IP address of the echo server")
echoServerPort = int(input("Enter the port number of the echo server"))
echoMSG = "echo message"
averageRTT = 0

for i in range (0,5):
    t1 = datetime.datetime.now()
    clientSocket.sendto(echoMSG.encode('utf-8'), (echoServerIP, echoServerPort))
    data, address = clientSocket.recvfrom(1024)
    t2 = datetime.datetime.now()
    averageRTT += (t2 - t1).microseconds
    print ("Round trip time ", i+1, " ", (t2-t1).microseconds, "microseconds")

averageRTT = averageRTT/5
print('Average RTT: ', averageRTT, " microseconds")
clientSocket.close()
