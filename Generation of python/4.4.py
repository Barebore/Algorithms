matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
n = 3
mn13 = 0

print(matrix)

for i in range(n):
    mn13 = min(matrix[i][:i+1])

print(min)
