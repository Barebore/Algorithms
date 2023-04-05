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
    sum_ += temp
    if sum_ <= k and (not flag or (flag and temp != 0)):
        if temp == 0:
            if lst[begin:i].count(0) == 0:
                flag = True
            else:
                break
    else:
        while not(sum_ <= k and (not flag or (flag and temp != 0))):
            sum_ -= lst[begin]
            if lst[begin] == 0:
                flag = False
            begin += 1
        if lst[begin:i+1].count(0) > 1:
            break
    result += i - begin + 1

print(result)
