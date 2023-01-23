# словарь перевода с языка станка на язык клавиатуры
translator_dict = {
    '0x0030': 0,
    '0x0031': '>',
    '0x002A': 'Edit',
    '0x0032': 2,
    '0x0037': 7,
}

# данные, которые читаем из файла
input_data = '0x00320x00310x00370x00300x00310x002A0x0037'
# делаем из строки список, элементами которого будут являться каждая команда в виде кода
n = 6
input_list = [input_data[i:i+n] for i in range(0, len(input_data), n)]
for elem in input_list:
    if elem in translator_dict:
        print(translator_dict[elem])
    else:
        print('Команда не найдена в словаре')