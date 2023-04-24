def main_func():

    def second_func():
        print("second_func")

    return second_func #  именно без скобок, не вызывая

print(main_func())

b = main_func() # - это теперь функия second_func
print(11, b()) # - вызов функции second_func

'''
Замыкание - такая ситуация, когда функция, использует переменную, которая не объявляена в её теле
'''
def main_func():
    variable = 'Value'
    def second_func():
        print("second_func", variable) #вот тут и после отработки переменная не исчезнет

    return second_func #  именно без скобок, не вызывая

print(main_func())

b = main_func() # - это теперь функия second_func
print(22, b()) # - вызов функции second_func


def main_func(value):
    variable = value
    def second_func():
        print("second_func", variable) #вот тут и после отработки переменная не исчезнет

    return second_func #  именно без скобок, не вызывая


b = main_func(123) # - это теперь функия second_func
print(33, b()) # - вызов функции second_func