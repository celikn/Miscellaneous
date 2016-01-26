#!/usr/bin/python3
#-------------------------------------------------------------------------------
# Source:Core Python Applications Programming-Networks
#              TCP Timestamp Server
# Author:      ncelik
#
# Created:     26.01.2016
# Copyright:   (c) ncelik 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from socket import *
from time import *

def main():
    HOST=''
    PORT=21567
    BUFSIZ=1024
    ADDR=(HOST,PORT)
    tcpSerSock=socket(AF_INET,SOCK_STREAM) # Creates TCP/IP
    tcpSerSock.bind(ADDR)  #Bind adress(hostname, post number) to socket
    tcpSerSock.listen(5) #Set up and start TCP listener
    while True:
        print ('waiting for connection..')
        tcpCliSock,addr=tcpSerSock.accept()  #Passively accept TCP client connection
        #, waiting until connection arrive
        print ('connected from:',addr)
        while True:
            data=tcpCliSock.recv(BUFSIZ).decode("utf-8")  #receive TCP message with 1024B-1K
            if not data:
                break
            #tcpCliSock.send("[%s] %s" .format(ctime().encode("utf-8"),data.encode("utf-8")))
            tcpCliSock.send(bytes(data.encode("utf-8")))
            tcpCliSock.send(bytes(ctime().encode("utf-8")))
            print (data)
        tcpCliSock.close()
    tcpSerSock.close

##tcpSock=socket.socket(socket.AF_INET,socket.SOCK_STREAM) # Creates TCP/IP
##udpSock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #Creates UDP/IP

if __name__ == '__main__':
    main()
