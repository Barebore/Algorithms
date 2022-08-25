def max2(x,y):
    if x > y:
        return x
    return y


def max3(x,y,z):
    return max2(x,max2(y,z))

x = 3
y = 4
z = 5
# max3(x,y,z)
print(max2(x,y))
print(max3(x,y,z))
print(max3('a','ab','abc'))

def hello_separated(name='World', separator='-'):
    print('Hello', name, sep=separator)  

hello_separated('John', '***') 
hello_separated(separator = '***')
hello_separated(separator = '***',
                name = 'John')
hello_separated()

def is_simple_number(x):
    ''' Является ли число простым.
        x - целое, положительное число.
        Если простое, то возвращает True,
        а иначе - False
    '''
    divisor = 2
    while divisor < x:
        if x%divisor == 0:
            return False
        devisor += 1 
    return True

print(is_simple_number(142))

