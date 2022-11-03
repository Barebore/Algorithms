class LinkedList:
    def __init__(self, obj = 0):
        self.__data = []
        self.head = None
        self.tail = None
        if obj != 0:
            self.add_obj(ObjList(obj))
    def add_obj(self,obj):
        self.__data.append(obj)
        if len(self.__data) >= 2:
            self.__data[len(self.__data)-1].set_prev(self.__data[len(self.__data)-2])
            self.__data[len(self.__data)-2].set_next(self.__data[len(self.__data)-1])
            self.tail = self.__data[len(self.__data)-1]
        # print('ololololo', len(self.__data), self.__data)
    def remove_obj(self):
        del self.__data[len(self.__data)]
        self.tail = self.__data[len(self.__data)]
    def get_data(self):
        return self.__data
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
print(lst.get_data())
# print(res[3])
# print(res[2])
# print(res[1])
# print(res[0])
# print()
# print(res[3].get_prev())
# print(res[2].get_prev())
# print(res[1].get_prev())
# print(res[0].get_prev())
# print()
# print(res[3].get_next())
# print(res[2].get_next())
# print(res[1].get_next())
# print(res[0].get_next())