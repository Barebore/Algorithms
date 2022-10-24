n = int(input())
a = [[1],[1,1]]
if n > 1:
    for i in range(1,n):
        cache = []
        for j in range(len(a[i])+1):
            if j == 0:
                cache.append(1)
            elif j == len(a[i]):
                cache.append(1)
            else:
                cache.append(a[i][j-1]+a[i][j])
        a.append(cache)

for i in range(n):
    print(a[i])