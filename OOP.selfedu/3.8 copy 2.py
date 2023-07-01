class Array:
    def __init__(self, max_length, cell):
        self.__max_length = max_length
        self.__cell = cell
        self.__lst = [self.__cell() for _ in range(self.__max_length)]

    def __getitem__(self, index):
        if - self.__max_length >= index >= self.__max_length:
            raise IndexError('Неверный индекc для доступа к элементам массива')
        if type(index) != int:
            raise ValueError('Значение должно быть целым числом')
        return self.__lst[index].value
    
    def __setitem__(self, key, value):
        if - self.__max_length >= key >= self.__max_length:
            raise IndexError('Неверный индекc для доступа к элементам массива')
        if type(value) != int:
            raise ValueError('неверный тип данноомассива')
        self.__lst[key].value = value
            

    def __repr__(self):
        return ' '.join(map(str, self.__lst))
    
    # def __str__(self):
    #     return ' '.join(map(str, self.__lst))

class Integer:
    def __init__(self, value=0):
        self.__value = value

    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, value):
        if type(value) != int:
            raise ValueError('Значение должно быть целым числом')
        self.__value = value

    def __repr__(self):
        return str(self.__value)
    
    # def __str__(self):
    #     return str(self.__value)


    
ar_int = Array(10, cell=Integer)
print(ar_int[3])
print(ar_int) # должны отображаться все значения массива в одну строчку через пробел
ar_int[0] = 5
ar_int[1] = 10
ar_int[2] = 15
print(ar_int)
print(ar_int[0])
print(ar_int[1])
print(ar_int[2])
# ar_int[1] = 10.5 # должно генерироваться исключение ValueError
# ar_int[10] = 1 # должно генерироваться исключение IndexError