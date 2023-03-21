from collections import Counter

def foo(n, lst):
    for i in range(n, 2, -1):
        counts = Counter(lst[0:i])
        if counts.most_common(1)[0][1] - counts.most_common()[-1][1] == 1 and (1 in counts.values() or counts.most_common()[-1][1] == 1):
            return i

n = int(input())
lst = list(map(int, input().split()))
print(foo(n, lst))
