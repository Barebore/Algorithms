def is_free(lst):
    return any(map(lambda x: '#' in x,lst))
st = ['# x o', 'x # x', 'o o #']
print(is_free(st))



