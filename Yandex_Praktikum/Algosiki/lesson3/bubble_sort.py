 = int(input())
a = list(map(int, input().split()))

for i in range(n):
    flag = False
    for j in range(n - i - 1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            flag = True
    print(*a)
    if not flag:
        break