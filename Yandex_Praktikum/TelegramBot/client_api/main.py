# /client_api/main.py

from pyrogram import Client

api_id = 22253903
api_hash = '97dfdbdc13fac973d16922d09dedd0c2'

# Создаём программный клиент, передаём в него
# имя сессии и данные для аутентификации в Client API
app = Client('my_account', api_id, api_hash)

app.start()
# Отправляем сообщение
# Первый параметр - это id чата или имя получателя.
# Зарезервированное слово 'me' означает собственный аккаунт отправителя.
for i in range(30):
    app.send_message('kisyan', f'Привет, это я! + {i}')
app.stop()