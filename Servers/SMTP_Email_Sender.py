#!/usr/bin/python3
#-------------------------------------------------------------------------------
# Source:https://recalll.co/
#             SMTP Email Sender
# Author:      ncelik
#
# Created:     26.01.2016
#-------------------------------------------------------------------------------
import smtplib
import datetime

def main(option):

 if option==1:
    ###Gmail EXample
    # Specifying the from and to addresses
    fromaddr = 'from@gmail.com'
    toaddrs  = 'to@email.com'
    # Writing the message (this message will appear in the email)
    msg = 'This is the email'
    # Gmail Login
    username = '*'
    password = '*'
    # Sending the mail
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username,password)
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()
 else:
    ##Some Exchange Server
    # Specifying the from and to addresses
    fromaddr = 'from@email.com'
    toaddrs  = 'to@email.com'
    # Writing the message (this message will appear in the email)
    msg = 'This is the email'
    # Gmail Login
    username = '*'
    password = '*'
    # Sending the mail
    server = smtplib.SMTP('mapinlb.*.*.*:587')
    server.starttls()
    server.login(username,password)
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()

if __name__ == '__main__':
    main(1)
