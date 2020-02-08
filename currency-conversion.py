import json
from urllib.request import urlopen

with urlopen("http://finance.yahoo.com/webservices/v1/symbols/allcurrencies/quote?format=json") as response:
    source = response.read()

print(source)