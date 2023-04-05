n, m = map(int, input().split())

grid = []
for i in range(n):
    row = list(map(int, input().strip()))
    grid.append(row)

# находим максимальную высоту сорняков на огороде
max_height = max(max(row) for row in grid)

# для каждой строки и столбца находим сумму высот сорняков
row_sum = [sum(row) for row in grid]
col_sum = [sum(grid[i][j] for i in range(n)) for j in range(m)]

# ищем строку и столбец с максимальной суммой и находим их индексы
max_row_sum = max(row_sum)
max_col_sum = max(col_sum)
max_row_index = row_sum.index(max_row_sum)
max_col_index = col_sum.index(max_col_sum)

# если максимальная высота сорняков на огороде меньше или равна 1, то удалять строку и столбец не нужно
if max_height <= 1:
    print("0 0")
else:
    # если максимальная сумма в строке больше максимальной суммы в столбце,
    # то удаляем строку с максимальной суммой, иначе удаляем столбец с максимальной суммой
    if max_row_sum >= max_col_sum:
        print(max_row_index + 1, 0)
    else:
        print(0, max_col_index + 1)
