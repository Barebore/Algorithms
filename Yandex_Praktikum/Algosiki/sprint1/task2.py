import doctest


def point_counter(max_count_choice, game_data):
    """
    Функция, вычисляющая максимальное количество
    баллов, которое могут набрать участники.

    >>> point_counter(3, [\
        ['1', '2', '3', '1'],\
        ['2', '.', '.', '2'],\
        ['2', '.', '.', '2'],\
        ['2', '.', '.', '2']\
        ])
    2
    """

    dct = dict()
    for row in game_data:
        for value in row:
            if value in dct:
                dct[value] += 1
            else:
                dct[value] = 1
    if '.' in dct:
        del (dct['.'])

    count = (1 for value in dct.values() if value <= max_count_choice*2)
    return sum(count)


if __name__ == '__main__':
    doctest.testmod()
    correct_answer = int(input())
    game_data = [list(input()) for i in range(4)]
    print(point_counter(correct_answer, game_data))
