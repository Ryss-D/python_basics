import urllib.request
import urllib.parse
import urllib.error

# that do not print the headers, but we can request for it probably with some attribute
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')#we can also read html


for line in fhand:
    print(line.decode().strip())
 #then we have a url to use like a file