# geoxml.py - Edited Code

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

api_key = 42
serviceurl = 'http://py4e-data.dr-chuck.net/xml?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1 or address.lower() == 'done':
        print('Program ended. Thank you.')
        break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)

    data = uh.read()
    print('Retrieved', len(data), 'characters')
    tree = ET.fromstring(data)

    # Edits starts Here:

    address_comps = tree.findall('result/address_component')
    comps = address_comps[0:]
    country = False

    try:
        for parent in comps:
            types = parent.findall('.//type')
            for child in types:
                if child.text == 'country':
                    country = True
                    print('----------')
                    print("Country Code:", parent.find('short_name').text)
                    print('Location:', tree.findall('result/formatted_address')[0].text)
                    print('\n')
        if country == False:
            raise Exception
    except:
        print('----------')
        print('This location does not fall within continental borders.')
        print('Location:', tree.findall('result/formatted_address')[0].text)
        print('\n')
