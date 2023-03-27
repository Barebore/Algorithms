n = int(input("Введите количество кубиков: "))
values = []
for i in range(n):
    values.append(set(map(int, input(f"Введите значения на кубике {i+1} через пробел: ").split())))
length = 0
print(values)
for i in values:
    length += len(i)
    print(length)
znach = length / len(values)
print(length/len(values))

print(1 + (znach - 1) * n)