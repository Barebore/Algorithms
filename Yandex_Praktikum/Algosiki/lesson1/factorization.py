def primes_sieve(n):
    # Создаем список чисел от 2 до n
    numbers = list(range(2, n + 1))
    # Перебираем все числа до корня из n
    for i in range(2, int(n**0.5) + 1):
        # Если i все еще находится в списке numbers,
        # то вычеркиваем все его кратные числа
        if i in numbers:
            for j in range(i**2, n+1, i):
                if j in numbers:
                    numbers.remove(j)
    return numbers
n = int(input())
a = n ** 0.5
lst2 = primes_sieve(int(a))
lst = []

while n > 1:
    for i in lst2:
        print(n % i)
        if n % i == 0:
            n = n / i
            lst.append(i)
            break
print(*lst)