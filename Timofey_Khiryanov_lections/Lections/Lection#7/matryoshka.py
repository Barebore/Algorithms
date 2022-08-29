def matryoshka(n):
    if n == 1:
        print('Матрёшечка')
    else:
        print('Верх матерёшки n=', n)
        matryoshka(n-1)
        print('Низ матрёшки n=', n)

matryoshka(5)
print(matryoshka)