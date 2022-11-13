class Dimensions:

    MIN_DIMENSION = 10
    MAX_DIMENSION = 1000

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @property
    def a(self):
        return self.__a
    @a.setter
    def a(self, value):
        if Dimensions.check_value(value):
            self.__a = value
    
    @property
    def b(self):
        return self.__b
    @b.setter
    def b(self, value):
        if Dimensions.check_value(value):
            self.__b = value

    @property
    def c(self):
        return self.__c
    @c.setter
    def c(self, value):
        if Dimensions.check_value(value):
            self.__c = value

    @classmethod
    def check_value(cls, value):
        return type(value) in (int,float) and cls.MAX_DIMENSION >= value >= cls.MIN_DIMENSION

    def __setattr__(self, key, value):
        if key == 'MIN_DIMENSION' or key == 'MAX_DIMENSION':
            raise AttributeError('Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено.')
        object.__setattr__(self, key, value)

d = Dimensions(10.5, 20.1, 30)
d.a = 8
d.b = 15
print(d.__dict__)
print(d.c)
a, b, c = d.a, d.b, d.c  # a=10.5, b=15, c=30
print(a,b,c)
# d.MAX_DIMENSION = 10  # исключение AttributeError