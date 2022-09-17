# a = input().split()
# #if 'Москва' in a:
# #    a.pop(a[a.index('Москва')])
# print(a.pop(a.index('Москва'))
# a.pop(2)
# print(a)
a = 811235
print(a%10000//1000+a%100000//10000+a%100000//100000)
print(a%100000//100000)
print(a//100000)
b = list(str(a))
print(b)
c = int(''.join(b))
print(c,type(c))