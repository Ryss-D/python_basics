import urllib.request, urllib.parse, urllib.error
import ssl
import xml.etree.ElementTree as ET 


#ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_865891.xml'
html = urllib.request.urlopen(url, context=ctx)
data = html.read()
#xml = html.decode()
stuff = ET.fromstring(data)
lst = stuff.findall('.//count')

count = 0
for item in lst:
    count += int(item.text)

print(count)
