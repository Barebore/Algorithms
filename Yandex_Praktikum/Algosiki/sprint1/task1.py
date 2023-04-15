import doctest


def distance_houses(length_street, number_home):
    """
    Функция возвращает список расстояний до пустых участков,
    где каждый элемент это учасок: 0 - пустой участкок,
    другие числа означают, что участок занятый и указывают
    на расстояние до ближайшего пустого участка.

    >>> distance_houses(5, [0, 1, 4, 9, 0])
    [0, 1, 2, 1, 0]

    >>> distance_houses(6, [0, 8, 9, 4, 8, 20])
    [0, 1, 2, 3, 4, 5]
    """

    l_out = []
    count_not_null = 0
    flag = 0
    for i, value in enumerate(number_home):
        if value != 0:
            count_not_null += 1
            l_out.append(count_not_null)
        elif value == 0:
            l_out.append(value)
            try:
                if flag == 1:
                    l_out[i - (count_not_null // 2):i] = (
                        list(range(count_not_null // 2, 0, -1)))
                else:
                    l_out[:i] = list(range(count_not_null, 0, -1))
                count_not_null = 0
                flag = 1
            except:
                pass
    return l_out


if __name__ == '__main__':
    doctest.testmod()

    length_street = int(input())
    number_home = list(map(int, input().split()))
    print(*distance_houses(length_street, number_home))
