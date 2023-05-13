from collections import Counter

n = int(input())
arr = list(map(int, input().split()))
counter = Counter(arr)

for i in range(3):
    print((str(i) + ' ') * counter[i], end='')