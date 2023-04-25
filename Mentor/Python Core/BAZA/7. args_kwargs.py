# *args - передача позиционных аргуменов

def sum_numbers(*args):
    for i in args:
        print(i)

print(sum_numbers(1, 2, 3, 4, 5))


# **kwargs - передача именованных аргументов


def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name="Alice", age=25, city="New York")

my_dict = {"name": "Alice", "age": 25, "city": "New York"}
print_kwargs(**my_dict)
