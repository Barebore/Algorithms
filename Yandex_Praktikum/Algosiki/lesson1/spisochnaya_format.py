a = input()
b = input()
if len(b) > len(a):
    a, b = b, a
for i in b:
    a = a.replace(i,'',1)
print(a)