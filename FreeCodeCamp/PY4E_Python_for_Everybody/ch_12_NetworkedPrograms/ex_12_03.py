# Exercise 3: Use urllib to replicate the previous exercise of (1) retrieving
# the document from a URL, (2) displaying up to 3000 characters, and (3)
# counting the overall number of characters in the document. Don’t worry about
# the headers for this exercise, simply show the first 3000 characters
# of the document contents.

import urllib.request, urllib.parse, urllib.error

geturl = input("Please enter a URL: ")

try:
    fhand = urllib.request.urlopen(geturl)

    count = 0
    site = ""

    for line in fhand:
        site += line.decode()
        words = line.decode().split()
        for word in words:
            for char in word:
                count += 1

    print(site[0:3001])
    print("\n")
    print('Total character count is:', count)

except:
    print('Error, improperly formatted or non-existent URL.')
