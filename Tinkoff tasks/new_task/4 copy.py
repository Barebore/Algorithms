import doctest
from collections import defaultdict


def boring_check(a: list):
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
    n = len(a)

    counts = defaultdict(int)
    for x in a:
        counts[x] += 1

    def is_boring_prefix(l):
        prefix_counts = defaultdict(int)
        freq_counts = [0]*(n+1)
        for i in range(l):
            prefix_counts[a[i]] += 1
            freq_counts[prefix_counts[a[i]]] += 1
        max_count = max(prefix_counts.values())
        min_count = min(prefix_counts.values())
        if max_count == min_count or (max_count == min_count + 1 and freq_counts[max_count] == 1):
            # This prefix is boring
            return True
        for i in range(l, n):
            prefix_counts[a[i-l]] -= 1
            freq_counts[prefix_counts[a[i-l]]+1] -= 1
            if prefix_counts[a[i-l]] == 0:
                del prefix_counts[a[i-l]]
            prefix_counts[a[i]] += 1
            freq_counts[prefix_counts[a[i]]] += 1
            max_count = max(prefix_counts.values())
            min_count = min(prefix_counts.values())
            if max_count == min_count or (max_count == min_count + 1 and freq_counts[max_count] == 1):
                # This prefix is boring
                return True
        # This prefix is not boring
        return False

    # Binary search for the maximum boring prefix length
    left = 0
    right = n
    while left < right:
        mid = (left + right + 1) // 2
        if is_boring_prefix(mid):
            left = mid
        else:
            right = mid - 1
    return left


if __name__ == '__main__':
    doctest.testmod()

length_set = int(input())
numbers_set = list(input())
# numbers_set = [1, 2, 3, 1, 2, 2, 3, 3, 3, 1, 4, 4, 5]
# print(boring_check(numbers_set))
# numbers_set = [1, 2, 4, 2, 3, 1, 3, 9, 15, 23]
# print(boring_check(numbers_set))
# numbers_set = [1, 2, 3, 4, 5]
# print(boring_check(numbers_set))


