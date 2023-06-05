class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 10000

    def __init__(self, a,b,c):
        self.__a = a
        self.__b = b
        self.__c = c

    @classmethod
    def validate_dimension(cls, value):
        return value <= cls.MIN_DIMENSION and value <= cls.MAX_DIMENSION

    @property
    def a(self):
        return self.__a
    
    @a.setter
    def a(self, value):
        if self.validate_dimension(value):
            self.__a = value

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, value):
        if self.validate_dimension(value):
            self.__b = value

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, value):
        if self.validate_dimension(value):
            self.__c = value

    def size(self):
        return self.a * self.b * self.c
    
    # >=
    def __ge__(self, other):
        return self.size() >= other.size()
    
    # <=
    def __le__(self, other):
        return self.size() <= other.size()
    
    # >
    def __gt__(self, other):
        return self.size() > other.size()
    
    # <
    def __lt__(self, other):
        return self.size() < other.size()
    

class ShopItem:
    def __init__(self, name, price, dim):
        self.name = name
        self.price = price
        self.dim = dim

trainers = ShopItem('кеды', 1024, Dimensions(40, 30, 120))
umbrella = ShopItem('зонт', 500.24, Dimensions(10, 20, 50))
fridge = ShopItem('холодильник', 40000, Dimensions(2000, 600, 500))
chair = ShopItem('табуретка', 2000.99, Dimensions(500, 200, 200))
lst_shop = (trainers, umbrella, fridge, chair)
lst_shop_sorted = sorted(lst_shop, key=lambda x: x.dim.size())
# print([item.name for item in lst_shop_sorted])