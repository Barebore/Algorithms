data = input().split(" ")
n = int(data[0])
k = int(data[1])
flag = False
sum_ = 0
result = 0
begin = 0
lst = list(map(int, input().split()))

for i in range(n):
    temp = lst[i]
    temp_list = []
    temp_list.append(lst[i])
    sum_ += temp
    if sum_ <= k and (not flag or (flag and temp != 0)):
        if temp == 0:
            flag = True
    else:
        while not(sum_ <= k and (not flag or (flag and temp != 0))):
            temp_list.append(lst[begin])
            sum_ -= lst[begin]
            if lst[begin] == 0:
                flag = False
            begin += 1
    if temp_list.count(0) <= 1:
        result += i - begin + 1

print(result)
