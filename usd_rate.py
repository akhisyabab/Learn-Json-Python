import requests, json

r = requests.get('http://www.floatrates.com/daily/usd.json').json()

for i in r:
    print(i)
print('----------------')
for i in r['idr']:
    print(i)
print('----------------')
print(r['idr']['name'])



#print(r.json())
