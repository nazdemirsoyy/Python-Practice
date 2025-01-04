import urllib.request
import xml.etree.ElementTree as ET

url = input('Enter location: ')
if len(url) < 1 : 
    url = 'http://py4e-data.dr-chuck.net/comments_2107097.xml'

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved',len(data),'characters')
tree = ET.fromstring(data)

counts = tree.findall('.//count')
nums = [int(count.text) for count in counts]
for result in counts:
    # Debug print the data :)
    print(result.text)

print('Count:', len(nums))
print('Sum:', sum(nums))