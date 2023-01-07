def high_and_low(numbers):
    lst = list(map(int, numbers.split()))
    numbers = str(max(lst)) + ' ' + str(min(lst))
    return numbers


print(high_and_low('1 2 3 4 5 6 7 -1 -5 3 -10'))