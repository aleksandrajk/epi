import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else:
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1:
        break

    parms = dict()
    parms['address'] = address
    if api_key is not False:
        parms['key'] = api_key
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

    # Extract the two-character country code
    country_code = None
    for component in js['results'][0]['address_components']:
        if 'country' in component['types']:
            country_code = component['short_name']
            break

    if country_code:
        print('Country Code:', country_code)
    else:
        print('Country code not found.')


# Enter location: London
# Retrieving http://py4e-data.dr-chuck.net/json?address=London&key=42
# Retrieved 2369 characters
# Country Code: GB

# Enter location: Warsaw
# Retrieving http://py4e-data.dr-chuck.net/json?address=warsaw&key=42
# Retrieved 2397 characters
# Country Code: PL

# Enter location: Singapore
# Retrieving http://py4e-data.dr-chuck.net/json?address=Singapore&key=42
# Retrieved 1396 characters
# Country Code: SG
