lst_in = [
    [1, 0, 1, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 1],
    [1, 0, 1, 0]
]

rows = [0 for i in range(len(lst_in)+2)]
new_lst_in = [[0] + rows + [0] for rows in lst_in]
new_lst_in.insert(0,rows)
new_lst_in.append(rows)
bool = 1
for i in range(1,len(new_lst_in)-1):
    for j in range(1,len(new_lst_in)-1):
        if new_lst_in[i][j] == 1:
            if (1 == new_lst_in[i-1][j-1] or
            1 == new_lst_in[i-1][j] or
            1 == new_lst_in[i-1][j+1] or
            1 == new_lst_in[i][j-1] or
            1 == new_lst_in[i][j+1] or
            1 == new_lst_in[i+1][j-1] or
            1 == new_lst_in[i+1][j] or
            1 == new_lst_in[i+1][j+1]):
                bool = 0
                break
        
    if bool == 0:
        break
print('ДА' if bool == 1 else 'НЕТ')