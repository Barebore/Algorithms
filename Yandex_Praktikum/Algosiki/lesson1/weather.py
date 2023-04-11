n = int(input())
lst = list(map(int, input().split()))
count = 0
for i in range(1, n-1):
    if lst[i-1] < lst[i] > lst[i+1]:
        count += 1

if lst[n-1] > lst[n-2]:
    count += 1
try:
    if lst[0] > lst[1]:
        count += 1
except:
    count = 1
print(count)