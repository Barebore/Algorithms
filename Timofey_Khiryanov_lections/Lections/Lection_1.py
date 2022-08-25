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
print(-12%10)
print(-12//10)
print(-12%5)
print(12%5)
print(-12//5)
# x = int(input())
# while x > 0:
#     y = x
#     while y > 0:
#         y -= 1
#         print(y)
#     x -= 1
# print('stop')
for x in 1,5,2,4,3:
    print(x**2)
print (0.2 + 0.7)
print(2**100000)
x = 2 ** 100000
print(type(x))
print(dir(x))
2+2 == 4
import this