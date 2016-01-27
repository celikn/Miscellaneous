#!/usr/bin/python3
#-------------------------------------------------------------------------------
# Source:http://stackoverflow.com/questions/2218066/python-retrieving-only-
#               pop3-message-text-no-headers
#              POP
# Author:      ncelik
#
# Created:     27.01.2016
# Copyright:   (c) ncelik 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import poplib

def main():
    host = "*.*.*.*"
    mail = poplib.POP3_SSL(host)
    print (mail.getwelcome())
    print (mail.user("*"))
    print (mail.pass_("*"))
    print (mail.stat())
    print (mail.list())
    print ("")

    if mail.stat()[1] > 0:
        print ("You have new mail.")
    else:
        print ("No new mail.")

    print ("")

    #Get the number of mail messages
    numMessages = len(mail.list()[1])

    #List the subject line of each message
    for mList in range(numMessages) :
        for msg in mail.retr(mList+1)[1]:
            if msg.decode('iso-8859-9').startswith('Subject'):
                print ('\t' +msg.decode('iso-8859-9'))
                break
    mail.quit()

if __name__ == '__main__':
    main()
