# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
count = int(input('Enter count: ')) 
position = int(input('Enter position: ')) 

print("Retrieving:", url)


for i in range(count):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all anchor tags
    tags = soup('a')
    if len(tags) >= position:
        # Get the URL at the specified position
        url = tags[position - 1].get('href', None)
        print("Retrieving:", url)
    else:
        print("Position exceeds the number of links on the page.")
        break

name = url.split('_')[-1].split('.')[0]
print("Last name in sequence:", name)