n, m = map(int, input().split())
a = [list(map(int, input())) for _ in range(n)]

min_weeds = float('inf')
min_i, min_j = 0, 0

for i in range(n):
    for j in range(m):
        # прополняем i-ую строку и j-ый столбец
        a[i][j] = 0
        
        # находим максимальную высоту сорняков
        max_weeds = max(max(row) for row in a)
        
        # если текущая максимальная высота сорняков меньше минимальной,
        # обновляем минимальную максимальную высоту и координаты
        if max_weeds < min_weeds:
            min_weeds = max_weeds
            min_i, min_j = i, j
        
        # восстанавливаем i-ую строку и j-ый столбец
        a[i][j] = max(max(row[j] for row in a), max(a[i]))
        
print(min_i + 1, min_j + 1)  # добавляем 1 к индексам для вывода номеров строк и столбцов, начинающихся с 1
# 5 4
# 4412
# 3212
# 0121
# 2192
# 4903