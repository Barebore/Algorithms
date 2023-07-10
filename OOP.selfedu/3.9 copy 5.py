class StackObj:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.length = 0

    def push_back(self, obj):
        obj.next = self.top
        self.top = obj
        self.length += 1


    def push_front(self, obj):
        temp = self.top
        while temp.next is not None:
            temp = temp.next
        temp.next = obj
        self.length += 1

    def __getitem__(self, index):
        if index < 0 or type(index) != int or index >= self.length:
            raise IndexError('неверный индекс')
        temp = self.top
        for i in range(self.length - index -1):
            temp = temp.next
        return temp.data
    
    def __setitem__(self, index, data):
        if index < 0 or type(index) != int or index >= self.length:
            raise IndexError('неверный индекс')
        temp = self.top
        for i in range(self.length - index - 1):
            temp = temp.next
        temp.data = data

    def __iter__(self):
        temp = self.top
        while temp is not None:
            yield temp
            temp = temp.next

st = Stack()
st.push_back(StackObj("1"))
st.push_front(StackObj("2"))
assert st[0] == "2" and st[1] == "1", "неверные значения данных из объектов стека, при обращении к ним по индексу"
# assert st[0] == "0", "получено неверное значение из объекта стека, возможно, некорректно работает присваивание нового значения объекту стека"
# for obj in st:
#     assert isinstance(obj, StackObj), "при переборе стека через цикл должны возвращаться объекты класса StackObj"
# try:
#     a = st[3]
# except IndexError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение IndexError"
 
