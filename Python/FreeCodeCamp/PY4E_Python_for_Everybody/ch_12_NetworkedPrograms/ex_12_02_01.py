# Exercise 2: Change your socket program so that it counts the number of
# characters it has received and stops displaying any text after it has shown
# 3000 characters. The program should retrieve the entire document and count
# the total number of characters and display the count of the number of
# characters at the end of the document.

# This version of the program displays all received characters,
# including the header data.

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

    print(site[:3001].decode())
    print("\n")
    print('Total character count is:', count)

except:
    print('Error, improperly formatted or non-existent URL.')
