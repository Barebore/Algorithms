'''
Декоратор - функция, которая принимает в качестве аргумента функцию и
расширяет её функционал без изменения последней.
'''

def func_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).replace('----', '-').replace('---', '-').replace('--', '-')
    return wrapper

@func_decorator
def cir_to_lat(str1):
    t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya',
     ' ': '-', '"': '-', ':': '-', ';': '-', '.': '-', ',': '-', '_': '-', '-': '-'}

    return ''.join([t[value] if value in t.keys() else value for value in str1.lower() ])

s = input()
print(cir_to_lat(s))