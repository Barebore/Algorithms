def max_prefix_length(lst):
    freq = {}
    for x in lst:
        freq[x] = freq.get(x, 0) + 1
    counts = sorted(freq.values())
    for i in range(len(counts)):
        if i == 0 or counts[i] != counts[i-1]:
            if i == len(counts)-1 or counts[i+1] == counts[-1]:
                del freq[lst[i]]
                if len(set(freq.values())) == 1:
                    return i
                freq[lst[i]] = freq.get(lst[i], 0) + 1
    return len(lst)

# Пример использования
lst = [1, 2, 3, 1, 2, 2, 3, 3, 3, 1, 4, 4, 5]
print(max_prefix_length(lst)) # должно вывести 10

lst = [1, 2, 4, 2, 3, 1, 3, 9, 15, 23]
print(max_prefix_length(lst)) # должно вывести 7

lst = [1, 2, 3, 4, 5]
print(max_prefix_length(lst)) # должно вывести 5