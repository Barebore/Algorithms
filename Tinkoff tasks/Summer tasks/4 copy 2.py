n = int(input())
a = list(map(int, input().split()))


# определяем функцию для проверки, является ли массив скучным
def is_boring(arr):
    count = {}
    for num in arr:
        count[num] = count.get(num, 0) + 1
    freqs = list(count.values())
    max_freq = max(freqs)
    min_freq = min(freqs)
    if max_freq == min_freq:
        return True
    if freqs.count(max_freq) == 1 and max_freq - 1 == min_freq and freqs.index(max_freq) == len(freqs) - 1:
        return True
    if freqs.count(min_freq) == 1 and min_freq == 1 and freqs.index(min_freq) == 0:
        return True
    return False


# ищем максимальное l, что префикс длины l массива a является скучным
for i in range(n, 1, -1):
    if is_boring(a[:i]):
        print(i)
        break
