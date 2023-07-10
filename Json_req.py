import requests

req = requests.get('https://swapi.dev/api/people/1/')
person = req.json()
# print(person)
print(f'name is\t\t{person["name"]}')
print(f'height is\t{person["height"]} cm')
print(f'mass is\t\t{person["mass"]} kg')
print(f'hair_color is\t{person["hair_color"]}')
print('films are:')
for film in person['films']:
    req = requests.get(film)
    film = req.json()
    print(film['title'])
