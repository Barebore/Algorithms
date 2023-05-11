n = int(input())
arr = []
for i in range(n):
    temp = list(map(int, input().split()))
    if temp not in arr:
        arr.append(temp)

result = []
arr = sorted(arr)
for val in arr:
    if result == []:
        result.append(val)
    else:
        flag = False
        for res in result:
            # когда диапазон включает в себя текущий
            if val[0] <= res[0] and val[1] >= res[1]:
                res[0], res[1] = val[0], val[1]
                flag = False
                break
            #когда оба значения входят в диапазон
            if val[0] >= res[0] and val[1] <= res[1]:
                flag = False
                break
            # когда пересечений нет
            if (val[0] < res[1] and val[1] < res[1] or
                val[0] > res[1] and val[1] > res[1]):
                flag = True
            # когда правое занчение касается диапазона слева
            if val[0] < res[0] and (val[1] == res[1] or val[1]+1 == res[1]):
                res[0] = val[1]
                flag = False
                break
            # когда левое занчение касается диапазона справа
            if (val[0] <= res[1] or val[0] + 1 == res[1])  and (val[1] > res[1]):
                res[1] = val[1]
                flag = False
                break
            # когда левое значение попадает в диапазон
            if val[0] <= res[0] and val[1] >= res[1]:
                res[1] = val[1]
                flag = False
                break
        if flag:
            result.append(val)

for i in result:
    print(*i)
# print(arr)
# print(result)