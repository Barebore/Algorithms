
    def digital_root(n):
        if n // 10 == 0:
            return n
        return (n % 10) + digital_root(n // 10)



print(digital_root(16))
print(digital_root(942))
print(digital_root(123))
print(digital_root(123))

# print(1//10)