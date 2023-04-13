k = int(input())
matrix = [list(input()) for i in range(4)]
dct = dict()
for row in matrix:
    for value in row:
        if value in dct:
            dct[value] += 1
        else:
            dct[value] = 1
if '.' in dct:
    del(dct['.'])

count = (1 for value in dct.values() if value <= k*2)


print(sum(count))