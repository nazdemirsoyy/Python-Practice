import urllib.request
import json

url = input("Enter location: ")
if len(url) < 1:
    url = "http://py4e-data.dr-chuck.net/comments_2107098.json" 
print("Retrieving", url)


uh = urllib.request.urlopen(url)
data = uh.read()
print("Retrieved", len(data), "characters")


info = json.loads(data)


comments = info['comments']
nums = [item['count'] for item in comments]


print("Count:", len(nums))
print("Sum:", sum(nums))
