n = int(input())
segments = [list(map(int, input().split())) for _ in range(n)]

# Сортируем отрезки по координате начала
segments.sort(key=lambda x: x[0])

# Слияние отрезков
result = []
prev_end = -1
for start, end in segments:
    if start <= prev_end:
        # Текущий отрезок сливается с предыдущим
        prev_end = max(prev_end, end)
    else:
        # Предыдущий отрезок добавляется в результат
        if prev_end != -1:
            result.append([prev_start, prev_end])
        prev_start, prev_end = start, end

# Добавляем последний отрезок в результат
if prev_end != -1:
    result.append([prev_start, prev_end])

# Выводим результат
for start, end in result:
    print(start, end)