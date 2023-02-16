from telegram import Bot
import requests



bot = Bot(token=token)

URL = 'https://api.thecatapi.com/v1/images/search'
response = requests.get(URL).json()
random_cat_url = response[0].get('url')
# print(response)
# print(type(response))
# print(len(response))
# print(response[0])

# print(type(response[0]))
# print(response[0]['url'])

chat_id = 222240659
text = 'Вам телеграмма!'
# Отправка сообщения
bot.send_message(chat_id, text)
# Отправка изображения
bot.send_photo(chat_id, random_cat_url)