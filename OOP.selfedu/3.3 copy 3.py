from typing import Any


class LinkedList:
    def __init__(self,  head=None, tail=None):
        self.head = head
        self.tail = tail

    def add_obj(self, obj):
        obj.prev = self.tail

        if self.tail:
            self.tail.next = obj
        self.tail = obj

        if not self.head:
            self.head = obj

    def __get_obj_by_index(self, indx):
        obj = self.head
        for i in range(indx):
            obj = obj.next
        return obj
    
    def remove_obj(self, indx):
        obj = self.__get_obj_by_index(indx)
        if obj is None:
            return
        prev, next = obj.prev, obj.next
        if prev:
            prev.next = next
        if next:
            next.prev = prev

        if self.head == obj:
            self.head = next
        if self.tail == obj:
            self.tail = prev



    def __len__(self):
        obj = self.head
        count = 0
        while obj:
            count += 1
            obj = obj.next
        return count
    
    def __str__(self):
        obj = self.head
        s = ""
        while obj:
            s += f"{obj.data} "
            obj = obj.next
        return s
    
    def __call__(self, indx):
        if self.head is None:
            return None
        obj = self.head
        for i in range(indx):
            obj = obj.next
        return obj.data
        

class ObjList:
    def __init__(self, data, prev=None, next=None):
        self.__data = data
        self.__prev = prev
        self.__next = next

    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, value):
        self.__data = value
    
    @property
    def prev(self):
        return self.__prev
    
    @prev.setter
    def prev(self, obj):
        self.__prev = obj

    @property
    def next(self):
        return self.__next


    @next.setter
    def next(self, obj):
        self.__next = obj
    

# linked_lst = LinkedList()
# linked_lst.add_obj(ObjList("Sergey"))
# linked_lst.add_obj(ObjList("Balakirev"))
# linked_lst.add_obj(ObjList("Python"))
# linked_lst.remove_obj(2)
# linked_lst.add_obj(ObjList("Python ООП"))
# linked_lst.add_obj(ObjList("Python ООП"))

# linked_lst.remove_obj(0)
# linked_lst.remove_obj(0)
# # linked_lst.remove_obj(0)
# # linked_lst.remove_obj(0)

# n = len(linked_lst)  # n = 3
# # s = linked_lst(0) # s = Balakirev
# print(n)
# print(s)

# ln = LinkedList()
# ln.add_obj(ObjList("Сергей"))
# ln.add_obj(ObjList("Балакирев"))
# ln.add_obj(ObjList("Python ООП"))
# ln.remove_obj(2)
# assert len(ln) == 2, "функция len вернула неверное число объектов в списке, возможно, неверно работает метод remove_obj()"
# ln.add_obj(ObjList("Python"))
# assert ln(2) == "Python", "неверное значение атрибута __data, взятое по индексу"
# assert len(ln) == 3, "функция len вернула неверное число объектов в списке"
# assert ln(1) == "Балакирев", "неверное значение атрибута __data, взятое по индексу"
# n = 0
# h = ln.head
# while h:
#     assert isinstance(h, ObjList)
#     h = h._ObjList__next
#     n += 1
# assert n == 3, "при перемещении по списку через __next не все объекты перебрались"
# n = 0
# h = ln.tail
# while h:
#     assert isinstance(h, ObjList)
#     h = h._ObjList__prev
#     n += 1
# assert n == 3, "при перемещении по списку через __prev не все объекты перебрались"
# print('errorrrrrrrrrrrrrrrrrrrrrr')

# obj = ln.head
# while obj:
#     print('cycle', ln.head, ln.tail, obj.data)
#     obj =  obj.next
 