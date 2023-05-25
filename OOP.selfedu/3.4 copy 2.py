class StackObj:
    def __init__(self, data, next=None) -> None:
        self.__data = data
        self.__next = next

    @property
    def next(self):
        return self.__next
    
    @next.setter
    def next(self, value):
        self.__next = value


class Stack:
    def __init__(self, top=None):
        self.top = top

    def push_back(self, obj):
        if self.top == None:
            self.top = obj
        else:
            temp = self.top
            while temp.next:
                temp = temp.next
            temp.next = obj
            
    def pop_back(self):
        self.top = self.top.next

    def __add__(self, other):
        self.push_back(other)
        return self

    def __iadd__(self, other):
        self.push_back(other)
        return self

    def __mul__(self, data_list):
        for data in data_list:
            self.push_back(StackObj(data))
        return self
    
    def __imul__(self, other):
        return self * other
    


assert hasattr(Stack, 'pop_back'), "класс Stack должен иметь метод pop_back"
st = Stack()
top = StackObj("1")
st.push_back(top)
assert st.top == top, "неверное значение атрибута top"
st = st + StackObj("2")
st = st + StackObj("3")
obj = StackObj("4")
st += obj
st = st * ['data_1', 'data_2']
st *= ['data_3', 'data_4']
d = ["1", "2", "3", "4", 'data_1', 'data_2', 'data_3', 'data_4']
h = top
i = 0
while h:
    assert h._StackObj__data == d[i], "неверное значение атрибута __data, возможно, некорректно работают операторы + и *"
    h = h._StackObj__next
    i += 1
    
assert i == len(d), "неверное число объектов в стеке"


# stack = Stack()
# stack.push_back(StackObj(1))
# stack.push_back(StackObj(2))
# stack.push_back(StackObj(3))
# print(stack.top)
# print(stack.top.next)
# print(stack.top.next.next)
# print('213')
# stack.pop_back()
# print(stack.top)
# print(stack.top.next)
# print(stack.top.next.next)
# print('213')
# stack.pop_back()
# print(stack.top)
# print(stack.top.next)
# print('213')
# stack.pop_back()
# print(stack.top)
# print('213')
# print(stack.top)

