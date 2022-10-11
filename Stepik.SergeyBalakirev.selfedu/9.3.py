a = ['house=дом', 'car=машина', 'men=человек', 'tree=дерево']
b = [[j for j in i.split('=')] for i in a]
print(b)
print(tuple(b))
c = tuple(tuple(map(str,i.split('='))) for i in a)
print(c)
d = tuple(tuple(i.split('=')) for i in a)
print(d)