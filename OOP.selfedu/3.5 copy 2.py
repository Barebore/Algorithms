import re

class StringText:
    def __init__(self, words):
        self.words = words

    def __str__(self):
        return ' '.join(self.words)

    def __lt__(self, other):
        return len(self.words) < len(other.words)

    def __le__(self, other):
        return len(self.words) <= len(other.words)

    def __gt__(self, other):
        return len(self.words) > len(other.words)

    def __ge__(self, other):
        return len(self.words) >= len(other.words)


# исходный текст
stich = ["Я к вам пишу – чего же боле?",
        "Что я могу еще сказать?",
        "Теперь, я знаю, в вашей воле",
        "Меня презреньем наказать.",
        "Но вы, к моей несчастной доле",
        "Хоть каплю жалости храня,",
        "Вы не оставите меня."]

lst_text = []

for line in stich:
    line = re.sub(r'[–?!,.;]', '', line)  # убираем знаки препинания
    words = line.split()  # разбиваем строку на слова
    st = StringText(words)  # создаем объект StringText
    lst_text.append(st)  # добавляем в список

# сортируем по убыванию числа слов
lst_text_sorted = sorted(lst_text, reverse=True)

# преобразуем в список строк
lst_text_sorted = [str(st) for st in lst_text_sorted]
