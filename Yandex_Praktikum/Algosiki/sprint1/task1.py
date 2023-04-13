# n = 5
# l = [0, 1, 4, 9, 0]
n = int(input())
l = list(map(int, input().split()))

l_out = []
count_not_null = 0
flag = 0
for i, value in enumerate(l):
    # while i < len(l):
    if value != 0:
        count_not_null += 1
        l_out.append(count_not_null)
    elif value == 0:
        l_out.append(value)
        try:
            if flag == 1:
                l_out[i - (count_not_null // 2):i] = list(range(count_not_null // 2, 0, -1))
            else:
                l_out[:i] = list(range(count_not_null, 0, -1))
            count_not_null = 0
            flag = 1
        except:
            pass
    # i += 1
print(*l_out)