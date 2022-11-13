import random

class RandomPassword:
    def __init__(self, psw_chars, min_lenght, max_lenght):
        self.psw_chars = psw_chars
        self.min_lenght = min_lenght
        self.max_lenght = max_lenght
    
    def __call__(self):
        psw = ''
        random_lenght = random.randint(self.min_lenght, self.max_lenght)
        for i in range(random_lenght):
            psw += random.choice(self.psw_chars)
        return psw 

min_lenght = 5
max_lenght = 20
psw_chars = "qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*"
rnd = RandomPassword(psw_chars, min_lenght, max_lenght)
psw = rnd()
lst_pass = [rnd() for i in range(3)]
print(lst_pass)


'''Подвиг 2. Объявите класс RandomPassword для генерации случайных паролей. Объекты этого класса должны создаваться командой:
rnd = RandomPassword(psw_chars, min_length, max_length)
где psw_chars - строка из разрешенных в пароле символов; min_length, max_length - минимальная и максимальная длина генерируемых паролей.
Непосредственная генерация одного пароля должна выполняться командой:
psw = rnd()
где psw - ссылка на строку длиной в диапазоне [min_length; max_length] из случайно выбранных символов строки psw_chars.
С помощью генератора списка (list comprehension) создайте список lst_pass из трех сгенерированных паролей объектом rnd класса 
RandomPassword, созданного с параметрами: 
min_length = 5
max_length = 20
psw_chars = "qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*"
P.S. Выводить на экран ничего не нужно, только создать список из паролей.
P.P.S. Дополнительное домашнее задание: попробуйте реализовать этот же функционал с использованием замыканий функций.'''