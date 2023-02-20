import requests

from pprint import pprint

url = 'https://practicum.yandex.ru/api/user_api/homework_statuses/'
headers = {'Authorization': 'OAuth y0_AgAAAABiiCwLAAYckQAAAADcZ9Zwh5d_DiNnQq-6jpUALffXIOL9ePQ'}
payload = {'from_date': 0}

# Делаем GET-запрос к эндпоинту url с заголовком headers и параметрами params
homework_statuses = requests.get(url, headers=headers, params=payload)

# Печатаем ответ API в формате JSON
# print(homework_statuses.text)

# А можно ответ в формате JSON привести к типам данных Python и напечатать и его
pprint(homework_statuses.json())
print(homework_statuses)
print(type(homework_statuses))
print()
homework = homework_statuses.json().get('homeworks')[0]
status = homework.get('status')
print(status)
if  not isinstance(homework, dict):
    print('lol')
else:
    print('olo')
homework1 = (homework_statuses.json().get('homeworks')[:1])
print(type(homework1))