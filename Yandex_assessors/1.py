def two_min_numbers(numbers):
    min = second_min = float('inf')
    for num in numbers:
        if num < min:
            second_min = min
            min = num
        elif num < second_min:
            second_min
    return min, second_min

numbers = map(int, input().split())

print(two_min_numbers(numbers))