from re import A


print()
print('Hello, World')
x = 'Hello, World'
print(x)
print(type(x))
x = 1 + 2 + 3 * 2
print(x)
print(type(x))
a = 2
b = 5
#tmp = a
#a = b
#b = tmp
a,b = b,a # обмен переменныхз через временный кортеж из двух переменных (сковородки с блинами)
print(a,b)
print(a**b)
print(a**b**b)
a = -a
print(a)
print(2/3)
x = 16
y = 3
print(x//y) # деление с отбрасыванием остатка (5)
print(x%y) # остаток от деления (3)