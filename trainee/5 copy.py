n, m = map(int, input().split())
a = [list(map(int, input())) for i in range(n)]

min_weediness = float('inf')
best_i, best_j = 0, 0

for i in range(n):
    for j in range(m):
        weediness = max(a[p][q] - (p == i) * a[p][j] - (q == j) * a[i][q] + (p == i and q == j) * a[i][j] for p in range(n) for q in range(m))
        if weediness < min_weediness:
            min_weediness = weediness
            best_i, best_j = i, j

print(best_i + 1, best_j + 1)
