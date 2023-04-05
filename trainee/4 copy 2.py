import itertools

n = int(input())
values = []
for i in range(n):
    values.append(list(map(int, input().split())))
combination = itertools.product(*values)
value = set([sum(i) for i in combination])
print(len(value))
