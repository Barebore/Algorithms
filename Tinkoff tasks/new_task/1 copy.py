import doctest


def check_stang_height(h1: int, h2: int, h3: int, h4: int) -> str:
    '''
    Функция, которая выводит YES, если люди стоят по возрастанию
    или убыванию, в противном случае выводит NO

    >>> check_stang_height(1,2,3,4)
    'YES'
    >>> check_stang_height(4,3,2,1)
    'YES'
    >>> check_stang_height(4,4,4,4)
    'YES'
    >>> check_stang_height(4,3,3,4)
    'NO'
    '''
    if h1 >= h2 >= h3 >= h4 or h1 <= h2 <= h3 <= h4:
        return 'YES'
    else:
        return 'NO'


if __name__ == '__main__':
    doctest.testmod()

h1, h2, h3, h4 = map(int, input().split())
print(check_stang_height(h1, h2, h3, h4))