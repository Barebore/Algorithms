def foo(number):
    result = 0
    for numb in str(number):
        result += int(numb) ** len(str(number))
    return True if result == number else False

print(foo(7))
assert foo(153) == True
assert foo(1652) == False
assert foo(1652) == False