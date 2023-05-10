
# lst = list(map(int, input().split()))

lst = [1, 2, 3, 4, 1, 10, 12, 19, 139, 130 ,133]

length = 1
result = ''
while lst != []:
    temp = []
    print
    for i, value in enumerate(lst):
        if len(str(value)) == length:
            temp.append(value)
    lst = [value for value in lst if len(str(value)) > length]
    result += ''.join(map(str, sorted(temp, reverse=True)))
    length += 1
    print('temp', temp)
    print('lst', lst)

print(result)
