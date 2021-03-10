# Exercise 1: Change the socket program socket1.py to prompt the user for the
# URL so it can read any web page. You can use split('/') to break the URL into
# its component parts so you can extract the host name for the socket connect
# call. Add error checking using try and except to handle the condition where
# the user enters an improperly formatted or non-existent URL.

# Orginal socket1.py program:

#import socket

#mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#mysock.connect(('data.pr4e.org', 80))
#cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
#mysock.send(cmd)

#while True:
    #data = mysock.recv(512)
    #if len(data) < 1:
        #break
    #print(data.decode(),end='')

#mysock.close()

# Modified Code of socket1.py:
# I'm using the URL of https://www.w3.org/Protocols/ for the purposes of
# this exercise.

import socket

geturl = input("Please enter a URL: ")

try:
    getsock = geturl.split('/')

    url = 'GET ' + geturl + ' HTTP/1.0\r\n\r\n'

    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((getsock[2], 80))
    cmd = url.encode()
    mysock.send(cmd)

    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        print(data.decode(),end='')

    mysock.close()

except:
    print('Error, improperly formatted or non-existent URL.')
