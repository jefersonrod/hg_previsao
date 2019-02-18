import requests
import json

urlapi = "https://api.hgbrasil.com/weather/?format=json&woeid="
woeid = "455822"
filejson = "ctba.json"

url = urlapi+woeid

response = requests.get(url)
data = response.text
r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
headers = {'user-agent': 'my-app/0.0.1'}
r = requests.get(url, headers=headers)
headers = {'user-agent': 'my-app/0.0.1'}
r = requests.get(url, headers=headers)
print("status_code : "+ str(response.status_code))
print("Content type : "+ response.headers['content-type'])
print("Encoding : "+ response.encoding)
print("Text : " + response.text)
print("JSON : " + str(response.json))
print("Python JSON : " + str(response.json()))

datatxt = response.text
data = response.json()
#print(data['results']['forecast'][0])

for v in data:
    print(v)

print ("---")

for key, value in data.items():
    print (key)
    print (value)

print ("---")

for element in data['results']['forecast']:
    
    #vlr = element['results']['forecast']

    data = ((element['date']))
    dia = ((element['weekday']))
    max = ((element['max']))
    min = ((element['min']))

    if "19/02" in data:
        print("Dia: "+data+" | "+dia+" = Maxima: "+max+" / Minima: "+min)

print ("---")
data = response.json()
for key, value in data.items():
    print (str(key) + " = " + str(value))

print ("---")

print(datatxt)
f = open(filejson,"w")
f.write(str(datatxt))
