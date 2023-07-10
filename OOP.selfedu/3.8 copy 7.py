class Thing:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
class Bag:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.items = []
        self.weight = 0

    def add_thing(self, thing):
        if self.weight + thing.weight > self.max_weight:
            raise ValueError('превышен суммарный вес предметов')
        self.items.append(thing)
        self.weight += thing.weight

    def __getitem__(self, index):
        return self.items[index]
    
    def __setitem__(self, index, value):
        if self.weight - self.items[index].weight + value.weight > self.max_weight:
            raise ValueError('превышен суммарный вес предметов')
        self.weight = self.weight - self.items[index].weight + value.weight
        self.items[index] = value   

    def __delitem__(self, index):
        del self.items[index]





b = Bag(700)
b.add_thing(Thing('книга', 100))
b.add_thing(Thing('носки', 200))
try:
    b.add_thing(Thing('рубашка', 500))
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"
assert b[0].name == 'книга' and b[0].weight == 100, "атрибуты name и weight объекта класса Thing принимают неверные значения"
t = Thing('Python', 20)
b[1] = t
assert b[1].name == 'Python' and b[1].weight == 20, "неверные значения атрибутов name и weight, возможно, некорректно работает оператор присваивания с объектами класса Thing"
del b[0]
assert b[0].name == 'Python' and b[0].weight == 20, "некорректно отработал оператор del"
try:
    t = b[2]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"
    
b = Bag(700)
b.add_thing(Thing('книга', 100))
print(b.weight)
b.add_thing(Thing('носки', 200))
print(b.weight)
b[0] = Thing('рубашка', 500)
print(b.weight)
try:
    b[0] = Thing('рубашка', 800)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError при замене предмета в объекте класса Bag по индексу"