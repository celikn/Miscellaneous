#!/usr/bin/python3
#-------------------------------------------------------------------------------
# Source:Core Python Applications Programming-Networks
#              UDP Timestamp Client
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
    udpCliSock=socket(AF_INET,SOCK_DGRAM) # Creates udp/IP
    while True:
        data=input('>')
        if not data:
            break
        udpCliSock.sendto(data.encode("utf-8"),ADDR)
        data,ADDR=udpCliSock.recvfrom(BUFSIZ)
        if not data:
            break
        print (data)
    udpCliSock.close()

if __name__ == '__main__':
    main()
