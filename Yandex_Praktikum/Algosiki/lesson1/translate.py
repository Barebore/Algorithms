def func():
    number = int(input())
    if number == 0:
        print(0)
        return None
    binary = ''
    while number > 0:
        print(number % 2)
        binary += str(number % 2)
        number = number // 2

    print(binary[::-1])

func()