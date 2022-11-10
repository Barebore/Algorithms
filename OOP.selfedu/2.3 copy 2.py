class StringValue:
    def __init__(self, min_length = 2, max_length = 50):
        self.min_length = min_length
        self.max_length = max_length
    
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if type(value) == str and self.max_length >= len(value) >= self.min_length:
            setattr(instance, self.name, value)
    

class PriceValue:
    def __init__(self, max_value = 100):
        self.max_value = max_value
    
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if (type(value) == int or type(value) == float) and self.max_value >= value >= 0:
            setattr(instance, self.name, value)


class SuperShop:
    def __init__(self, name):
        self.name = name
        self.goods = []

    def add_product(self, product):
        self.goods.append(product)
        
    def remove_product(self, product):
        del self.goods[self.goods.index(product)]

class Product():
    name = StringValue()
    price = PriceValue()

    def __init__(self, name, price) -> None:
        self.price = price
        self.name = name


shop = SuperShop("У Балакирева")
shop.add_product(Product("name", 100))
shop.add_product(Product("name", 100))
assert shop.name == "У Балакирева", "атрибут name объекта класса SuperShop содержит некорректное значение"

for p in shop.goods:
    # print(p.__dict__)
    assert p.price == 100, "дескриптор price вернул неверное значение"
    assert p.name == "name", "дескриптор name вернул неверное значение"
t = Product("name 123", 1000)
shop.add_product(t)
shop.remove_product(t)
assert len(shop.goods) == 2, "неверное количество товаров: возможно некорректно работают методы add_product и remove_product"
assert hasattr(shop.goods[0], 'name') and hasattr(shop.goods[0], 'price')
t = Product(1000, "name 123")
if hasattr(t, '_name'):
    assert type(t.name) == str, "типы поля name должнен быть str"
if hasattr(t, '_price'):
    assert type(t.price) in (int, float), "тип поля price должнен быть int или float"