# geojson.py - Edited Code

import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = 42
serviceurl = 'http://py4e-data.dr-chuck.net/json?'

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
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    # Edits starts Here:

    results = js['results'][0]
    comps = results['address_components']
    country = False

    try:
        for i in comps:
            types = i['types']
            if types == ["country", "political"]:
                country = True
                print('----------')
                print("Country Code:", i["short_name"])
                print('Location:', results['formatted_address'])
                print('\n')
        if country == False:
            raise Exception

    except:
        print('----------')
        print('This location does not fall within continental borders.')
        print('Location:', results['formatted_address'])
        print('\n')
