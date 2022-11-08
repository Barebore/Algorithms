class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None
    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def next(self):
        return self.__next
    
    @next.setter
    def next(self, obj):
        if obj is None or isinstance(obj, StackObj):
            self.__next = obj

class Stack:

    def __init__(self) -> None: 
        self.top = None

    def push(self,obj):
        if self.top is None:
            self.top = obj
        else:
            next_temp = self.top
            while not(next_temp.next is None):
                next_temp = next_temp.next
            next_temp.next = obj

    def pop(self):
        if self.top is None:
            return
        if self.top.next is None:
            a = self.top
            self.top = None
            return a
        next_temp = self.top
        while not(next_temp.next.next is None):
            next_temp = next_temp.next
        a = next_temp.next
        next_temp.next = None
        return a

    def get_data(self):
        next_temp = self.top
        lst = []
        while next_temp:
            lst.append(next_temp.data)
            next_temp = next_temp.next
        return lst


st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
b = StackObj("obj3")
print(b)
st.push(b)
print(st.pop())
res = st.get_data()    # ['obj1', 'obj2']
print(res)