n = int(input("Введите количество кубиков: "))
values = []
for i in range(n):
    values.append(list(map(int, input(f"Введите значения на кубике {i+1} через пробел: ").split())))

import itertools

combination = itertools.product(*values)
value = set([sum(i) for i in combination])
print(value)
print(len(value))