lst_in = [
    [1, 0, 1, 1],
    [0, 1, 1, 0],
    [1, 0, 1, 1],
    [1, 0, 1, 1]
]

flag = 0

for i in range(len(lst_in)):
    for j in range(i+1,len(lst_in[i])):
        if lst_in[i][j] != lst_in[j][i]:
            flag = 1

print(['ДА','НЕТ'][flag])