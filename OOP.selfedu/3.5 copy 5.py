class CentralBank:
    rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

    def __new__(cls):
        return None
    
    def __call__(self):
        return None

    @classmethod
    def register(cls, wallet):
        wallet.cb = cls


class MoneyD:
    def __init__(self, volume=0):
        self.__cb = None
        self.__volume = volume

    @property
    def cb(self):
        return self.__cb
    
    @cb.setter
    def cb(self, cb):
        self.__cb = cb

    @property
    def volume(self):
        if self.check_register():
            return self.__volume
        else:
            raise ValueError('Неизвестен курс валют.')
    @volume.setter
    def volume(self, volume):
        self.__volume = volume

    @classmethod
    def check_register(cls):
        return cls.cb is not None
    
    def __eq__(self, other):
        compare_value = 0
        if isinstance(other, MoneyD):
            compare_value = other.volume * other.cb.rates['rub']
        if isinstance(other, MoneyE):
            compare_value = other.volume * other.cb.rates['euro'] * other.cb.rates['rub']
        if isinstance(other, MoneyR):
            compare_value = other.volume
        return (self.volume * self.cb.rates['dollar']) - compare_value < 0.1
    
    def __lt__(self, other):
        self.check_register()
        other.check_register()
        compare_value = 0
        if isinstance(other, MoneyD):
            compare_value = other.volume * other.cb.rates['dollar']
        if isinstance(other, MoneyE):
            compare_value = other.volume * other.cb.rates['dollar'] * other.cb.rates['euro']
        if isinstance(other, MoneyR):
            compare_value = other.volume
        return self.volume < compare_value
    
    def __ge__(self, other):
        self.check_register()
        other.check_register()
        compare_value = 0
        if isinstance(other, MoneyD):
            compare_value = other.volume * other.cb.rates['dollar']
        if isinstance(other, MoneyE):
            compare_value = other.volume * other.cb.rates['dollar'] * other.cb.rates['euro']
        if isinstance(other, MoneyR):
            compare_value = other.volume
        return self.volume >= compare_value
    
    def __gt__(self, other):
        compare_value = 0
        if isinstance(other, MoneyD):
            compare_value = other.volume * other.cb.rates['rub']
        if isinstance(other, MoneyE):
            compare_value = other.volume * other.cb.rates['euro'] * other.cb.rates['rub']
        if isinstance(other, MoneyR):
            compare_value = other.volume
        return self.volume * self.cb.rates['rub']  > compare_value
    




class MoneyE:
    def __init__(self, volume=0):
        self.__cb = None
        self.__volume = volume

    @property
    def cb(self):
        return self.__cb
    
    @cb.setter
    def cb(self, cb):
        self.__cb = cb

    @property
    def volume(self):
        return self.__volume
    
    @volume.setter
    def volume(self, volume):
        self.__volume = volume
    
    @classmethod
    def check_register(cls):
        if cls.cb != None:
            return True
        return ValueError('Неизвестен курс валют.')
    def __eq__(self, other):
        self.check_register()
        other.check_register()
        compare_value = 0
        if isinstance(other, MoneyD):
            compare_value = other.volume * other.cb.rates['dollar']
        if isinstance(other, MoneyE):
            compare_value = other.volume * other.cb.rates['dollar'] * other.cb.rates['euro']
        if isinstance(other, MoneyR):
            compare_value = other.volume
        return self.volume == compare_value
    
    def __lt__(self, other):
        self.check_register()
        other.check_register()
        compare_value = 0
        if isinstance(other, MoneyD):
            compare_value = other.volume * other.cb.rates['rub']
        if isinstance(other, MoneyE):
            compare_value = other.volume * other.cb.rates['euro'] * other.cb.rates['rub']
        if isinstance(other, MoneyR):
            compare_value = other.volume
        return self.volume * self.cb.rates['euro'] * self.cb.rates['dollar']  < compare_value
    
    def __ge__(self, other):
        self.check_register()
        other.check_register()
        compare_value = 0
        if isinstance(other, MoneyD):
            compare_value = other.volume * other.cb.rates['dollar']
        if isinstance(other, MoneyE):
            compare_value = other.volume * other.cb.rates['dollar'] * other.cb.rates['euro']
        if isinstance(other, MoneyR):
            compare_value = other.volume
        return self.volume >= compare_value
    
    def __gt__(self, other):
        self.check_register()
        other.check_register()
        compare_value = 0
        if isinstance(other, MoneyD):
            compare_value = other.volume * other.cb.rates['dollar']
        if isinstance(other, MoneyE):
            compare_value = other.volume * other.cb.rates['dollar'] * other.cb.rates['euro']
        if isinstance(other, MoneyR):
            compare_value = other.volume
        return self.volume > compare_value

class MoneyR:
    def __init__(self, volume=0):
        self.__cb = None
        self.__volume = volume

    @property
    def cb(self):
        return self.__cb
    
    @cb.setter
    def cb(self, cb):
        self.__cb = cb

    @property
    def volume(self):
        self.check_register()
        return self.__volume
    
    @volume.setter
    def volume(self, volume):
        self.__volume = volume

    @classmethod
    def check_register(cls):
        if cls.cb == None:
            raise ValueError('Неизвестен курс валют.')
        return True
    
    def __eq__(self, other):
        if isinstance(other, MoneyD):
            if other.cb == None:
                raise ValueError('Неизвестен курс валют.')
            compare_value = other.volume * other.cb.rates['dollar']
        if isinstance(other, MoneyE):
            compare_value = other.volume * other.cb.rates['dollar'] * other.cb.rates['euro']
        if isinstance(other, MoneyR):
            compare_value = other.volume
        return self.volume == compare_value
    
    def __lt__(self, other):
        self.check_register()
        other.check_register()
        compare_value = 0
        if isinstance(other, MoneyD):
            if other.cb == None:
                raise ValueError('Курс валют не задан.')
            compare_value = other.volume * other.cb.rates['dollar']
        if isinstance(other, MoneyE):
            compare_value = other.volume * other.cb.rates['dollar'] * other.cb.rates['euro']
        if isinstance(other, MoneyR):
            compare_value = other.volume
        return self.volume < compare_value
    
    def __ge__(self, other):
        self.check_register()
        other.check_register()
        compare_value = 0
        if isinstance(other, MoneyD):
            compare_value = other.volume * other.cb.rates['rub']
        if isinstance(other, MoneyE):
            compare_value = other.volume * other.cb.rates['euro'] * other.cb.rates['euro']
        if isinstance(other, MoneyR):
            compare_value = other.volume
        return self.volume >= compare_value
    
    def __gt__(self, other):
        self.check_register()
        other.check_register()
        compare_value = 0
        if isinstance(other, MoneyD):
            test = other.volume
            test1 = other.cb.rates['rub']
            print()
            compare_value = other.volume * other.cb.rates['rub']
        if isinstance(other, MoneyE):
            compare_value = other.volume * other.cb.rates['euro'] * other.cb.rates['rub']
        if isinstance(other, MoneyR):
            compare_value = other.volume
        return self.volume > compare_value


rub = MoneyR()   # с нулевым балансом
dl = MoneyD(1501.25) # с балансом в 1501.25 долларов
euro = MoneyE(100)  # с балансом в 100 евро

CentralBank.rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

r = MoneyR(45000)
d = MoneyD(500)
# print(r.volume)
# print(d.volume)
# print(r.cb)
# print(d.cb)
# # CentralBank.register(r)
# # CentralBank.register(d)
# print(r.cb)
# print(d.cb)
# print(r.volume)
# print(d.volume)
# print(d.cb.rates)
# print(r.cb.rates)
if r < d:
    print("неплохо")
else:
    print("нужно поднажать")