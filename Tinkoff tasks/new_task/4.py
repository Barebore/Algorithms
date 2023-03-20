import doctest


def boring_check(numbers_set: list):
    '''
    Выводит максимальное l, что префикс длины l массива является скучным.
    Набор чисел является скучным, если из  него можно удалить один элемент так,
    чтобы каждое число в нём встречалось одинаковое количество раз.

    >>> boring_check(1, 2, 3, 1, 2, 2, 3, 3, 3, 1, 4, 4, 5)
    10

    >>> boring_check(1, 2, 4, 2, 3, 1, 3, 9, 15, 23)
    7

    >>> boring_check(1, 2, 3, 4, 5)
    5
    '''
    pass


if __name__ == '__main__':
    doctest.testmod()

length_set = int(input())
number_set = list(input())
print(boring_check(number_set))

