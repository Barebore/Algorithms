def fibonachi_recusrion(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fibonachi_recusrion(n-1) + fibonachi_recusrion(n-2)
n, k = map(int, input().split())
print(fibonachi_recusrion(n))
print(fibonachi_recusrion(n) % (10 * k))