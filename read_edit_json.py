import requests
import json

req = requests.get('https://swapi.dev/api/people/1/')
person = req.json()
# print(person)
# json.loads is not needed since we are receiving data in json
# person = json.loads(person)
person['name'] = 'Ciaran'
person_str = json.dumps(person)
print(person_str)
