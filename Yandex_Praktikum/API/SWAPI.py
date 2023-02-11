import requests

response = requests.get('https://swapi.dev/api/starships/9/')
response = response.text
print(response)
print(type(response))