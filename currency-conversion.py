import json
from urllib.request import urlopen

with urlopen("http://google.com") as response:
    source = response.read()

print(source)