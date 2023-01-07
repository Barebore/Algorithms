def get_count(sentence):
    lst = ['a', 'e', 'i', 'o', 'u']
    result = 0
    for char in sentence:
        if char in lst:
            result += 1
    return result

a = 'priivet'
print(get_count(a))