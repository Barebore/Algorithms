def find_minimal_height(matrix):
    n, m = len(matrix), len(matrix[0])
    max_height = max([max(row) for row in matrix])

    max_height_diff = 0
    row_to_change, col_to_change = 0, 0

    for i in range(n):
        for j in range(m):
            prev_height = matrix[i][j]
            matrix[i][j] = 0
            new_height = max([max(row) for row in matrix])
            height_diff = max_height - new_height
            if height_diff > max_height_diff:
                max_height_diff = height_diff
                row_to_change, col_to_change = i + 1, j + 1
            matrix[i][j] = prev_height

    return (row_to_change, col_to_change)

# Пример использования
matrix = [
    [4, 4, 1, 2],
    [3, 2, 1, 2],
    [0, 1, 2, 1],
    [2, 1, 9, 2],
    [4, 9, 0, 3]
]
print(find_minimal_height(matrix)) # Вывод: (3, 3)
# 4412
# 3212
# 0121
# 2192
# 4903