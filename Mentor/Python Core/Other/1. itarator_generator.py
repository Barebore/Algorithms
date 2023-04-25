'''
Генератор - это специальная функция в Python, которая позволяет вам создавать
последовательности значений на лету, без необходимости хранить все значения в памяти.
Пример генератора может выглядеть так:
'''


def square_numbers(n):
    for i in range(n):
        yield i**2

# Создаем генератор
my_generator = square_numbers(5)

# Печатаем значения, создаваемые генератором
for num in my_generator:
    print(num)



'''Итератор - это объект, который позволяет вам перебирать последовательность значений.
В Python все итераторы являются объектами класса, реализующего методы __iter__ и __next__.
Вот пример итератора, который печатает все числа от 0 до 4:'''


class MyIterator:
    def __init__(self):
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 5:
            self.current += 1
            return self.current - 1
        else:
            raise StopIteration

# Создаем итератор
my_iterator = MyIterator()

# Печатаем значения, создаваемые итератором
for num in my_iterator:
    print(num)