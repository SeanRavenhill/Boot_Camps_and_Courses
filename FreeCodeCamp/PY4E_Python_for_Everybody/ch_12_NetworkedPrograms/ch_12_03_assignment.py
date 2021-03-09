# See README.md for assignment briefs.

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
count = int(input('Enter count: '))
posistion = int(input('Enter posistion: '))

for i in range(count+1):
    print("Retrieving: ",url)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    addresses = list()
    for tag in tags:
        html = tag.get('href', None)
        addresses.append(html)
    for address in addresses:
        address = addresses[posistion-1]
    url = address
