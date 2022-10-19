def Balakirev(number):
    if number in [1,2,3]:
        for _ in range(number):
            yield 1
    else:
        x1, x2, x3 = 1, 1, 1
        numbers = [1, 1, 1]
        
        for _ in range(3):
            yield 1
            
        for _ in range(4, number + 1):
            x1, x2, x3 = x2, x3, x1 + x2 + x3
            yield x3
            

N = int(input())
result = Balakirev(N)
print(*result)