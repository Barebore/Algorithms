'''
Декоратор - функция, которая принимает в качестве аргумента функцию и
расширяет её функционал без изменения последней.
'''

def decorator_with_arguments(decorator_arg1, decorator_arg2):
    def decorator(function):
        def wrapper(*args, **kwargs):
            print(f"Начало выполнения функции. Аргументы декоратора: {decorator_arg1}, {decorator_arg2}")
            result = function(*args, **kwargs)
            print("Завершение выполнения функции")
            return result
        return wrapper
    return decorator

@decorator_with_arguments("параметр1", "параметр2")
def my_function(arg1, arg2):
    print(f"Выполнение функции. Аргументы функции: {arg1}, {arg2}")

my_function("аргумент1", "аргумент2")
