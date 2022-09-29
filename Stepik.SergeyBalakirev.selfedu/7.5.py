import sys


def verify(lst_in):
    flag = 1
    for i in range(len(lst_in)-1):
        for j in range(len(lst_in[i])):
            if lst_in[i][j] == 1:
                flag *= is_isolate(i,lst_in)
    return bool(flag)

def is_isolate(*args):
    flag = 1
    number_row = args[0]
    lst = args[1]
    lst_check = []
    for i in range(len(lst)):
        lst_check.append(lst[number_row][i]+lst[number_row+1][i])
    for x in range(1,len(lst_check)):
        if lst_check[x] == 1:
            if lst_check[x] == lst_check[x-1]:
                flag = 0
        if lst_check[x] == 2:
            flag = 0
    return flag


print(verify([[1, 0, 1, 0, 0, 0],
              [0, 0, 0, 0, 1, 0],
              [0, 1, 0, 0, 0, 0], 
              [0, 0, 0, 1, 0, 0], 
              [0, 0, 0, 0, 0, 1],
              [0, 1, 0, 1, 0, 0]]))
