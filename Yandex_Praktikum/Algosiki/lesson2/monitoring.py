i = int(input())
j = int(input())
matrix = [list(input().split()) for row in range(i)]
# print(matrix)
for i1 in range(j):
    for j1 in range(i):
        print(matrix[j1][i1], end=" ")
    print()