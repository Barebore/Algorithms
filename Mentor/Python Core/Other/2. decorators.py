'''
Декоратор - функция, которая принимает в качестве аргумента функцию и
расширяет её функционал без изменения последней.
'''

def show_menu(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        for i, value in enumerate(res):
            print(f'{i}. {value}')
    return wrapper

@show_menu
def get_menu(s):
    return list(s.split())
