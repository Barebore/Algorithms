n = int(input())

triangle = [1]
for i in range(1,n+1):
    row = [1 for i in range(i)]
    for j in range(1, len(row)-1):
        row[j] = triangle[i-1][j-1] + triangle[i-1][j]
    triangle.append(row)

for row in triangle:
    print(row)