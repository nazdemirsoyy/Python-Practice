import urllib.request, urllib.parse
import json, ssl

serviceurl = 'https://py4e-data.dr-chuck.net/opengeo?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    # Prepare the query
    address = address.strip()
    parms = dict()
    parms['q'] = address

    # Construct the URL
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        # Parse the JSON data
        js = json.loads(data)
    except:
        js = None

    if not js or 'features' not in js:
        print('==== Download error ===')
        print(data)
        break

    if len(js['features']) == 0:
        print('==== Object not found ====')
        print(data)
        break

    # Extract latitude, longitude, formatted address, and plus_code
    lat = js['features'][0]['properties']['lat']
    lon = js['features'][0]['properties']['lon']
    location = js['features'][0]['properties']['formatted']
    plus_code = js['features'][0]['properties'].get('plus_code', 'N/A')

    # Print the extracted data
    print('lat:', lat, 'lon:', lon)
    print('Location:', location)
    print('Plus code:', plus_code)
