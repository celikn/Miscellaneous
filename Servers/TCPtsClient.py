#!/usr/bin/python3
#-------------------------------------------------------------------------------
# Source:Core Python Applications Programming-Networks
#              TCP Timestamp Client
# Author:      ncelik
#
# Created:     26.01.2016
# Copyright:   (c) ncelik 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from socket import *
from time import *

def main():
    HOST='localhost'
    PORT=21567
    BUFSIZ=1024
    ADDR=(HOST,PORT)
    tcpCliSock=socket(AF_INET,SOCK_STREAM) # Creates TCP/IP
    tcpCliSock.connect(ADDR)  #Bind adress(hostname, post number) to socket
    while True:
        data=input('>')
        if not data:
                break
        tcpCliSock.send(data.encode("utf-8"))
        data=tcpCliSock.recv(BUFSIZ).decode("utf-8")
        if not data:
            break
        print (data)
    tcpCliSock.close()


##tcpSock=socket.socket(socket.AF_INET,socket.SOCK_STREAM) # Creates TCP/IP
##udpSock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #Creates UDP/IP

if __name__ == '__main__':
    main()
