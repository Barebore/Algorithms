
def lib(s1,s2):
    s1 = s1.split()
    s2 = s2.split()
    return s1,s2

a, b = lib('12 23 45 as sd cr','asd asdas asd')
print(*lib('34 34534 354534','asd asdas asd'))
print(a)

print(dict(a))