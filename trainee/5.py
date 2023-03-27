n = int(input("Введите количество кубиков: "))
values = list(map(int, input("Введите значения на кубиках через пробел: ").split()))

# Создаем список возможных сумм
sums = [0]*(6*n+1)
sums[0] = 1

# Считаем количество возможных сумм
for i in range(n):
    for j in range(6*n, -1, -1):
        for k in range(6):
            if j-k-1 >= 0:
                sums[j] += sums[j-k-1]

# Считаем количество различных целых чисел
count = 0
for i in range(sum(values), 6*n+1):
    count += sums[i]

print("Количество различных целых чисел:", count)