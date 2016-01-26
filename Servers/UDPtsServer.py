#!/usr/bin/python3
#-------------------------------------------------------------------------------
# Source:Core Python Applications Programming-Networks
#              UDP Timestamp Server
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
    udpSerSock=socket(AF_INET,SOCK_DGRAM) # Creates UDP/IP
    udpSerSock.bind(ADDR)  
    while True:
            print ('waiting for message..')
            data,addr=udpSerSock.recvfrom(BUFSIZ)
            udpSerSock.sendto(data,addr)
            #udpSerSock.sendto(ctime().encode('utf-8'),ADDR)
            print (data,"..received from and returned to :",addr)
        
    udpSerSock.close

if __name__ == '__main__':
    main()
