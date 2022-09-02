def fib(n):
    ''''функция выисления числа Фибоначчи, асимтотика большая, быстро разрастается
        занимате много памяти, так как держит адреса возврата функций в стеке и пр.
    '''
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

print(fib(10))

def fib(n):
    fib = [0,1] + [0]*(n-1)
    for i in range(2, n+1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib[n]

print(fib(10))