import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter -')
headers = {'User-Agent':'Mozilla/5.0'}
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

#retrieve all of anchor tags
tags = soup('a')
print(soup)

with open('wplay.html', 'w', encoding= 'utf-8') as crawled:
    crawled.write(str(soup))
    crawled.close()
# for tag in tags:
#     print(tag.get('href', None))
# print(tags)

# from bs4 import BeautifulSoup


# url = "https://www.codere.com.co/"
# headers = {'User-Agent':'Mozilla/5.0'}
# page = urllib.request.urlopen(url)
# soup = BeautifulSoup(page.text, "html.parser")

# print(soup)
