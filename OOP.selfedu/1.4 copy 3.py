a = ['1 Сергей 35 120000', '2 Федор 23 12000', '3 Иван 13 1200']
FIELDS = ('id', 'name', 'old', 'salary')
b = {}
c = []

for i in a:
    c.append({y:x for x,y in zip(i.split(),FIELDS)})


print(c)