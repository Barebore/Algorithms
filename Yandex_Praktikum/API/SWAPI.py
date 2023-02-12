from pprint import pprint

import requests

# Ваш код здесь.
params = {'name':'luke', }
response = requests.get('https://swapi.dev/api/people/', params=params)
characters = response.json()
response = requests.get(characters['results'][0]['homeworld'])
print(response.json()['diameter'])