# n = int(input())
# s = input()
# n = 7
# s = 'dbbccca'
# n = 16
# s = 'aaaabbbbccccdddd'
n = 12
s = 'aabbccddbadd'
# Инициализация переменных-счетчиков
count_a, count_b, count_c, count_d = 0, 0, 0, 0
left, right = 0, 0
min_length = float('inf')

while right < n:
    # Увеличиваем счетчик текущего символа
    if s[right] == 'a':
        count_a += 1
    elif s[right] == 'b':
        count_b += 1
    elif s[right] == 'c':
        count_c += 1
    elif s[right] == 'd':
        count_d += 1

    # Сдвигаем левый указатель, пока все символы встречаются хотя бы один раз
    while count_a > 0 and count_b > 0 and count_c > 0 and count_d > 0:
        min_length = min(min_length, right - left + 1)

        # Уменьшаем счетчик левого символа и сдвигаем левый указатель
        if s[left] == 'a':
            count_a -= 1
        elif s[left] == 'b':
            count_b -= 1
        elif s[left] == 'c':
            count_c -= 1
        elif s[left] == 'd':
            count_d -= 1
        left += 1

    right += 1
    print(right, left)

if min_length == float('inf'):
    print(-1)
else:
    print(min_length)