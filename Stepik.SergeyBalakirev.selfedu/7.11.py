def func_decorator(func):
    def wrapper(*args):
        print('что-то перед')
        func(*args)
        print('что-то после')
    return wrapper
 
def some_func(title,tag):
    print(f'вызов функции some_func {title} {tag}')


f = func_decorator(some_func)
some_func = func_decorator(some_func)
#f()
some_func('asdsad','asd')