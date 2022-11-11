class Shop:
    def __init__(self, name):
        self.name = name
        self.goods = []
    
    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        del self.goods[self.goods.index(product)]

class Product:
    id = 0
    dct = {'id' : [int],'name': [str], 'weight': [int, float], 'price': [int]}


    @classmethod
    def get_id(cls):
        cls.id += 1
        return cls.id

    def __init__(self, name, weight, price):
        self.id = self.get_id()
        self.name = name
        self.weight = weight
        self.price = price

    def __setattr__(self, key, value):
        if key == id or type(value) in self.dct[key]:
            if key == 'weight' or key == 'price':
                if value < 0:
                    raise TypeError('Значения weight or key должны быть положительными')
            object.__setattr__(self, key, value)
        else:
            raise TypeError('Неверный тип присваиваемых данных.')
    def __delattr__(self, item):
        if item == 'id':
            raise AttributeError('Атрибут id удалять запрещено')
        object.__delattr__(self, item)

shop = Shop('магазин')
a = Product('5',0,-1)
b = Product('6',5,5)
shop.add_product(a)
shop.add_product(b)
# print(a.__dict__)
# print(b.__dict__)
del shop.goods[0].name

