import itertools

n, s = map(int, input().split())

# Создаем список диапазонов баллов для каждого ученика
ranges = []
for i in range(n):
    r = tuple(map(int, input().split()))
    ranges.append(range(r[0], r[1]+1))

# Генерируем все возможные комбинации баллов для всех учеников
combinations = itertools.product(*ranges)

# Отфильтровываем комбинации, которые нарушают ограничения на максимальный суммарный балл
combinations = filter(lambda c: sum(c) <= s, combinations)

# Отфильтровываем комбинации, которые нарушают ограничения на минимальную и максимальную оценку учеников
combinations = filter(lambda c: all(r[0] <= x <= r[-1] for r, x in zip(ranges, c)), combinations)

# Находим максимальный медианный балл
max_median = 0
for c in combinations:
    sorted_c = sorted(c)
    median = sorted_c[n//2] if n % 2 == 1 else (sorted_c[n//2-1] + sorted_c[n//2]) / 2
    max_median = max(max_median, median)

print(max_median)