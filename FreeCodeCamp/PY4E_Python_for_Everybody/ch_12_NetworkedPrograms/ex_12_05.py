# Exercise 5: (Advanced) Change the socket program so that it only shows data
# after the headers and a blank line have been received. Remember that recv
# receives characters (newlines and all), not lines.

import socket

geturl = input("Please enter a URL: ")

count = 0
site = b""

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
        count += len(data)
        site += data

    mysock.close()

    # Look for the end of the header (2 CRLF = \r\n\r\n)
    pos = site.find(b"\r\n\r\n")

    print(site[pos+4:].decode())


except:
    print('Error, improperly formatted or non-existent URL.')
