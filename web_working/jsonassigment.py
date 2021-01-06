import urllib.request, urllib.parse, urllib.error
import json

url = 'http://py4e-data.dr-chuck.net/comments_865892.json'

uh = urllib.request.urlopen(url)
data = uh#.read().decode() no aplicaba puesto que el json no debiua ser decodificado

js = json.load(data)

count = 0

for dic in js["comments"]:
     count += int(dic["count"])

print(count)

