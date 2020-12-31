import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'http://py4e-data.dr-chuck.net/json?'

# for i in range(99999):
#     while True: 
#         address = 'University of Dallas' # static to save time
#         key = i
#         if len(address) <1: break

#         url = serviceurl + urllib.parse.urlencode({'key': key,'address' : address})
#         #print('Retriving', url)
#         uh = urllib.request.urlopen(url)
#         data = uh.read().decode()
#         #print('Retriving', len(data), 'characters')

#         try:
#             js = json.loads(data)
#         except:
#             js = None
#             #print('error')
            
#         if not js:
#             #print(data)
#             break
#         print(i)
#         print(js)
#         place_id = js["place_id"]
#         print('the place id is {}'.format(place_id))

while True: 
        address = 'University of Dallas' # static to save time
        key = 42
        if len(address) <1: break

        url = serviceurl + urllib.parse.urlencode({'key': key,'address' : address})
        #print('Retriving', url)
        uh = urllib.request.urlopen(url)
        data = uh.read().decode()
        #print('Retriving', len(data), 'characters')

        try:
            js = json.loads(data)
        except:
            js = None
            #print('error')
            
        if not js:
            #print(data)
            break

        place_id = js["results"][0]["place_id"]
        print('the place id is {}'.format(place_id))