def func(x):
    def digital_root(n):
        if n // 10 == 0:
           return n
        return (n % 10) + digital_root(n // 10)

    while x > 9:
        x = digital_root(x)
    return x

print(func(71332156))