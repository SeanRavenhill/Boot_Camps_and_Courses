# See README.md for assignment briefs.

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

counts = 0

while True:
    url = input('Enter XML URL: ')
    print('\n')
    if url.lower() == 'done':
        print("Program Ended. Thank You.")
        break
    elif len(url) < 1 or '.xml' not in url:
        print('Please enter a valid url with an .xml suffix')
        print('\n')
        continue

    else:
        print('Retrieving', url)
        uh = urllib.request.urlopen(url, context=ctx)

        data = uh.read()
        print('Retrieved', len(data), 'characters')
        tree = ET.fromstring(data)

        lst = tree.findall('.//count')

        for child in lst:
            counts += int(child.text)

        print('\n')
        print(counts)

        break
