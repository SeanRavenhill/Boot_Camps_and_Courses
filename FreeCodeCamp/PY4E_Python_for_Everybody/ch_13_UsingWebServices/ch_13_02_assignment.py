# See README.md for assignment briefs.

import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

counts = 0

while True:
    url = input('Enter JSON URL: ')
    print('\n')
    if url.lower() == 'done':
        print("Program Ended. Thank You.")
        break
    elif len(url) < 1 or '.json' not in url:
        print('Please enter a valid url with an .json suffix')
        print('\n')
        continue

    else:
        print('Retrieving', url)
        uh = urllib.request.urlopen(url, context=ctx)
        data = uh.read()
        print('Retrieved', len(data), 'characters')
        info = json.loads(data)


        for a, b in info.items():
            if a == 'comments':
                data = b
                for item in data:
                    counts += int(item['count'])

        print(counts)

        break
