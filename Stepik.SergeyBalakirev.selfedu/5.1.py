n, m = map(int, input().split())
while n < m:
    print(n + (n + 1) % 2, end=' ')
    n += 2