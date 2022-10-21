def get_sort(d):
    print(list(d.items()).sort())
    # print('func', d)
    return sorted(d.values())

d = {'cat': 'кот', 'horse': 'лошадь', 'tree': 'дерево', 'dog': 'собака', 'book': 'книга'}
print(d)
print(get_sort(d))
