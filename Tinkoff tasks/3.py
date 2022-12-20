def isPrime(n):
    ''' Проверка: простое ли число'''
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n

def task3(n):
    a = 1
    b = n - 1
    if isPrime(n):
        return a,b
    for i in range(2, n // 2 + 1):
        if isPrime(i):
            if n % i == 0:
                a = int( n / i )
                b = n - a
                return a, b


a = int(input())
print(*task3(a))