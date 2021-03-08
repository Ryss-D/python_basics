
import requests

response = requests.get('https://www.google.com')

print(response.text[:300])

response = requests.get('https://www.google.com', stream=True)
print(response.raw.read()[:100])

response.request.headers['Accept-Encoding']
response.headers['Content-Encoding']

response.ok #returns a boolean True if response was good and False if it wasnt
response.status_code

## example of usege
response = requests.get(url)
if not response.ok:
    raise Exception("GET failed with status code {}".format(response.status_code))

response = requests.get(url)
response.raise_for_status()# it will return a exceptsion with http status if response.ok return false

## how to use library to pass the parameter of url query

p = {"serach":"gre kitten", "max results":15}
response = requests.get("https://example.com/path/to/api", params = p)
response.request.url
#'https://example.com/path/to/api?search=grey+kitten&max_results=15'

p = {"description": "white kitten",
"name": "Snowball",
"age_months": 6}
response = requests.post("https://example.com/path/to/api", data=p)
response.request.url
##'https://example.com/path/to/api'
response.request.body
##'description=white+kitten&name=Snowball&age_months=6'

