n = int(input("Введите количество кубиков: "))
values = []
for i in range(n):
    values.append(list(map(int, input(f"Введите значения на кубике {i+1} через пробел: ").split())))

# Создаем список возможных сумм
sums = [0]*(3*6*n+1)
sums[0] = 1

# Считаем количество возможных сумм
for i in range(n):
    for j in range(3*6*n, -1, -1):
        for k in range(6):
            if j-k-1 >= 0:
                sums[j] += sums[j-k-1]

# Считаем количество возможных вариантов значений
count = 0
for i in range(3, 3*6*n+1):
    for j in range(3, 3*6*n+1):
        for k in range(3, 3*6*n+1):
            if i+j+k-sum([sum(x) for x in values]) == n*3:
                count += sums[i]*sums[j]*sums[k]

print("Количество возможных вариантов значений:", count)