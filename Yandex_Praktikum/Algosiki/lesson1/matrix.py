n = int(input())
m = int(input())
matrix = [list(map(int, input().split())) for i in range(n)]
x = int(input())
y = int(input())

output_lst = []
# print("LOOOL")
# print(matrix[x][y])
try:
    # print("LOOOL")
    output_lst.append(matrix[x][y-1 if y-1 >= 0 else None])
except:
    pass
try:
    # print("LOOOL")
    output_lst.append(matrix[x+1][y])
except:
    pass
try:
    # print("LOOOL")
    output_lst.append(matrix[x][y+1])
except:
    pass
try:
    # print("LOOOL")
    output_lst.append(matrix[x-1 if x-1 >= 0 else None][y])
except:
    pass

print(*sorted(output_lst))

# print(n)
# print(m)
# print(matrix)
# print(x)
# print(y)