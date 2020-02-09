import requests

r = requests.get("http://xkcd.com/353/")
print(r)
print(dir(r))
#print(help(r))
print(r.text)
print(r.content)

##############
r1 = requests.get("https://images-na.ssl-images-amazon.com/images/I/71Mqh46ZpiL._AC_SL1500_.jpg")

with open ('picture.jpg','wb') as f:
    f.write(r1.content)

print("done")
