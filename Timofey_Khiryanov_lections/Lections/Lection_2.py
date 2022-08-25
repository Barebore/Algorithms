#translation number system

number = []
number_revers = []
base = 2
x = int(input())
while x > 0:
    digit = x % base
    print(digit, end = '')
    number.append(digit)
    x //= base
print(end = '\n')

for i in range(len(number)):
    number_revers.append(number[-1-i])


for i in number_revers:
    print(i, end = '')