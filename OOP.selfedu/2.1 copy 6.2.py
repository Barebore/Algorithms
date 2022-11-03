class LinkedList:
    def __init__(self, obj = 0):
        self.__data = []
        self.head = None
        self.tail = None
        if obj != 0:
            self.add_obj(ObjList(obj))
    def add_obj(self,obj):
        self.__data.append(obj)
        if len(self.__data) >= 1:
            self.head = self.__data[0]
        if len(self.__data) >= 2:
            self.__data[len(self.__data)-1].set_prev(self.__data[len(self.__data)-2])
            self.__data[len(self.__data)-2].set_next(self.__data[len(self.__data)-1])
            self.tail = self.__data[len(self.__data)-1]
        # print('ololololo', len(self.__data), self.__data)
    def remove_obj(self):
        del self.__data[len(self.__data)-1]
        if len(self.__data) > 1:
            self.tail = self.__data[len(self.__data)-1]
        elif len(self.__data) == 0:
            self.tail = None
    def get_data(self):
        a = []
        for _ in self.__data:
            a.append(_.get_data())
        return a
class ObjList:
    def __init__(self, data):
        self.set_data(data)
        self.set_next(None)
        self.set_prev(None)
    def set_next(self, obj):
        self.__next = obj
    def set_prev(self, obj):
        self.__prev = obj
    def get_next(self):
        return self.__next
    def get_prev(self):
        return self.__prev
    def set_data(self, data):
        self.__data = data
    def get_data(self):
        return self.__data

ob = ObjList('данные 1')
lst = LinkedList(ObjList('данные 1'))
lst.add_obj(ObjList('данные 1'))
lst.add_obj(ObjList('данные 2'))
lst.add_obj(ObjList('данные 3'))
res = lst.get_data() #данные 1, данные 2, данные 3


ls = LinkedList()
ls.add_obj(ObjList("данные 1"))
ls.add_obj(ObjList("данные 2"))
ls.add_obj(ObjList("данные 3"))
ls.add_obj(ObjList("данные 34"))
assert ls.get_data() == ['данные 1', 'данные 2', 'данные 3', 'данные 34'], "метод get_data вернул неверные данные"
ls_one = LinkedList()
ls_one.add_obj(ObjList(1))
assert ls_one.get_data() == [1], "метод get_data вернул неверные данные"
h = ls_one.head
n = 0
while h:
    n += 1
    h = h.get_next()
    
assert n == 1, "неверное число объектов в списке: возможно некорректно работает метод add_obj"
ls_one.remove_obj()
assert ls_one.get_data() == [], "метод get_data вернул неверные данные для пустого списка, возможно, неверно работает метод remove_obj"
ls2 = LinkedList()
assert ls.head != ls2.head, "атрибут head должен принадлежать объекту класса LinkedList, а не самому классу"
assert ls.tail != ls2.tail, "атрибут tail должен принадлежать объекту класса LinkedList, а не самому классу"
h = ls.head
n = 0
while h:
    n += 1
    h = h.get_next()
    
assert n == 4, "неверное число объектов в списке: возможно некорректно работает метод add_obj"
h = ls.head
n = 0
while h:
    h = h._ObjList__next
    n += 1
    
assert n == 4, "неверное число объектов в списке: возможно некорректные значения в атрибутах __next"    
h = ls.tail
n = 0
while h:
    n += 1
    h = h.get_prev()
assert n == 4, "неверное число объектов в списке: возможно некорректно работает метод add_obj"
h = ls.tail
n = 0
while h:
    h = h._ObjList__prev
    n += 1
    
assert n == 4, "неверное число объектов в списке: возможно некорректные значения в атрибутах __prev"