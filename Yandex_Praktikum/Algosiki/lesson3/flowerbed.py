n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

result = []
for value in arr:
    if result == []:
        result.append(value)
    flag = 0
    for i in result:
        if i[0] - 1 <= value[0] and i[1] + 1 >= value[1]:
            i[0] = value[0]
            i[1] = value[1]
            flag = True
            break
        if i[0] - 1 <= value[0]:
            i[0] = value[0]
            flag = True
        if i[1] + 1 >= value[1]:
            i[1] = value[1]
            flag = True
        if value[0] >= i[0] and value[1] <= i[1]:
            flag = True
            break
    if not flag:
        result.append(value)


print(arr)
print(result)