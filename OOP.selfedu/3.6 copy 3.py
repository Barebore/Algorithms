import sys
class ShopItem:
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    def __hash__(self):
        return hash((self.name.lower(), self.weight, self.price))
    
    def __eq__(self, other):
        return hash(self) == hash(other)
    
# Sample Input:
# Системный блок: 1500 75890.56
# Монитор Samsung: 2000 34000
# Клавиатура: 200.44 545
# Монитор Samsung: 2000 34000

lst_in = list(map(str.strip, sys.stdin.readlines()))
dct = {}
for item in lst_in:
    name = item.split(':')[0]
    weight, price = map(float, item.split(':')[1].split())
    if ShopItem(name, weight, price) in dct:
        dct[ShopItem(name, weight, price)][1] += 1
    else:
        dct[ShopItem(name, weight, price)] = [ShopItem(name, weight, price), 1]

print(dct)
