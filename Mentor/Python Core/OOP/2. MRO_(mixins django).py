# Method Resoilution Order (MRO)

class Goods:
    def __init__(self, name, weight, price):
        print('init MixinLog')
        self.name = name
        self.weight = weight
        self.price = price
    
    def print_info(self):
        print()

class MixinLog:
    ID = 0

