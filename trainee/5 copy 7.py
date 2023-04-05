import copy

M, N = map(int, input().split()) # считываем размеры матрицы
matrix = [list(map(int, input())) for _ in range(M)] # считываем матрицу

min_max_value = float('inf') # задаем начальное значение минимального максимального значения
min_row = 0 # задаем начальные значения для строки и столбца, которые нужно изменить
min_col = 0

temp_matrix = copy.deepcopy(matrix)
max_element = 99999
min_i = 0
min_j = 0

for i in range(M):
    for j in range(N):
        temp_matrix[i] = [0] * len(temp_matrix[i])
        for k in range(M):
            temp_matrix[k][j] = 0
        # print(*temp_matrix)
        # print('-------')
        # print(max(max(row) for row in temp_matrix))
        if max_element > max(max(row) for row in temp_matrix):
            max_element = max(max(row) for row in temp_matrix)
            # print('ololo', max_element)
            min_i = i
            min_j = j
        temp_matrix = copy.deepcopy(matrix)
        # print('original',matrix)
print(min_i+1, min_j+1)
        
        
        # temp = sum(matrix[i]) + sum([matrix[k][j] for k in range(M)])
        # max_element = max(max(row) for row in matrix)
        # print('max',max_element)
        # # print('строка', matrix[i])
        # # print('столбец', [matrix[k][i] for k in range(M)])
        # print(temp)

# for i in range(M):
#     for j in range(N):
#         # изменяем значение в строке i и столбце j на 0
#         matrix[i][j] = 0
#         # находим максимальное значение в матрице после изменения
#         max_value = max([max(row) for row in matrix])
#         # если максимальное значение меньше текущего минимального максимального значения
#         if max_value < min_max_value:
#             # обновляем значения минимального максимального значения, строки и столбца
#             min_max_value = max_value
#             min_row = i
#             min_col = j
#         # изменяем значение в строке i и столбце j обратно на исходное
#         matrix[i][j] = int(input_str[j])
        
# print(min_row, min_col)
