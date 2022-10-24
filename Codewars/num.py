def square_digits(num):
    a = [str(int(i)**2) for i in str(num)]
    b = ''.join(a)
    return b
a = [1,2,3,4]
print(*a, sep = '')
b = 213
print(square_digits(b))