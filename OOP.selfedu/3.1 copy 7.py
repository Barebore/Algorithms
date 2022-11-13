import time

class GeyserClassic:
    MAX_DATE_FILTER = 100
    def __init__(self):
        self.slot_1 = None
        self.slot_2 = None
        self.slot_3 = None

    def add_filter(self, slot_num, filter):
        if slot_num == 1 and self.slot_1 == None and type(filter) == Mechanical:
            self.slot_1 = filter
        if slot_num == 2 and self.slot_2 == None and type(filter) == Aragon:
            self.slot_2 = filter
        if slot_num == 3 and self.slot_3 == None and type(filter) == Calcium:
            self.slot_3 = filter
    
    def get_filters(self):
        return (self.slot_1, self.slot_2, self.slot_3)

    def remove_filter(self, slot_num):
        if slot_num == 1:
            self.slot_1 = None
        if slot_num == 2:
            self.slot_2 = None
        if slot_num == 3:
            self.slot_3 = None


    def water_on(self):
        if self.slot_1 != None and self.slot_2 != None and self.slot_3 != None:
            if (0 <= (time.time() - self.slot_1.date) <= self.MAX_DATE_FILTER and
            0 <= (time.time() - self.slot_2.date) <= self.MAX_DATE_FILTER and
            0 <= (time.time() - self.slot_3.date) <= self.MAX_DATE_FILTER):
                return True
        return False

    @staticmethod
    def check_date(value):
        return type(value) == float and value > 0
    

class Mechanical:
    def __init__(self, date):
        if GeyserClassic.check_date(date):
            self.date = date

    def __setattr__(self, key, value):
        if key not in self.__dict__.keys():
            object.__setattr__(self, key, value)

class Aragon:
    def __init__(self, date):
        if GeyserClassic.check_date(date):
            self.date = date
        
    def __setattr__(self, key, value):
        if key not in self.__dict__.keys():
            object.__setattr__(self, key, value)

class Calcium:
    def __init__(self, date):
        if GeyserClassic.check_date(date):
            self.date = date

    def __setattr__(self, key, value):
        if key not in self.__dict__.keys():
            object.__setattr__(self, key, value)


import time
my_water = GeyserClassic()
my_water.add_filter(1, Mechanical(time.time()))
my_water.add_filter(2, Aragon(time.time()))
assert my_water.water_on() == False, "метод water_on вернул True, хотя не все фильтры были установлены"
my_water.add_filter(3, Calcium(time.time()))
assert my_water.water_on(), "метод water_on вернул False при всех трех установленных фильтрах"
f1, f2, f3 = my_water.get_filters()
assert isinstance(f1, Mechanical) and isinstance(f2, Aragon) and isinstance(f3, Calcium), "фильтры должны быть устанлены в порядке: Mechanical, Aragon, Calcium"
my_water.remove_filter(1)
assert my_water.water_on() == False, "метод water_on вернул True, хотя один из фильтров был удален"
my_water.add_filter(1, Mechanical(time.time()))
assert my_water.water_on(), "метод water_on вернул False, хотя все три фильтра установлены"
f1, f2, f3 = my_water.get_filters()
my_water.remove_filter(1)
my_water.add_filter(1, Mechanical(time.time() - GeyserClassic.MAX_DATE_FILTER - 1))
assert my_water.water_on() == False, "метод water_on вернул True, хотя у одного фильтра истек срок его работы"
f1 = Mechanical(1.0)
f2 = Aragon(2.0)
f3 = Calcium(3.0)
assert 0.9 < f1.date < 1.1 and 1.9 < f2.date < 2.1 and 2.9 < f3.date < 3.1, "неверное значение атрибута date в объектах фильтров"
f1.date = 5.0
f2.date = 5.0
f3.date = 5.0
print(f1.date, f2.date, f3.date)
#assert 0.9 < f1.date < 1.1 and 1.9 < f2.date < 2.1 and 2.9 < f3.date < 3.1, "локальный атрибут date в объектах фильтров должен быть защищен от изменения"