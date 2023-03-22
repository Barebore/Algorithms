import itertools

n, s = map(int, input().split())
grades = []
for i in range(n):
    a, b = map(int, input().split())
    grades.append(list(range(a, b+1)))

max_median = 0
for chosen_grades in itertools.product(*grades):
    if sum(chosen_grades) <= s:
        median = sorted(chosen_grades)[n//2]
        if median > max_median:
            max_median = median

print(max_median)