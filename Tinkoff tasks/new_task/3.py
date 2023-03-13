s = input() # считываем строку s
chars_count = {'a': 0, 'b': 0, 'c': 0, 'd': 0} # инициализируем словарь chars_count
min_length = float('inf') # инициализируем переменную min_length
start = 0 # инициализируем переменную start

for end in range(len(s)): # перебираем символы в строке s
    if s[end] in chars_count: # если текущий символ принадлежит алфавиту, то обновляем словарь chars_count
        chars_count[s[end]] += 1
    while all(count > 0 for count in chars_count.values()): # если все символы присутствуют в словаре, то обновляем min_length и start
        min_length = min(min_length, end - start + 1)
        if s[start] in chars_count:
            chars_count[s[start]] -= 1
        start += 1

if min_length == float('inf'): # если не найдено хороших подстрок, выводим -1
    print(-1)
else: # иначе выводим минимальную длину хорошей подстроки
    print(min_length)