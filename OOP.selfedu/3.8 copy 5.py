class StackObj:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.length = 0

    def push(self, obj):
        self.length += 1
        if self.top == None:
            self.top = obj
        else:
            obj.next = self.top
            self.top = obj

    def pop(self):
        self.length -= 1
        temp = self.top
        self.top = self.top.next
        return temp
    
    def __getitem__(self, index):
        if index < 0 or type(index) != int or index >= self.length:
            raise IndexError('неверный индекс')
        temp = self.top
        for i in range(self.length - index -1):
            temp = temp.next
        return temp
    
    def __setitem__(self, index, obj):
        if index < 0 or type(index) != int or index >= self.length:
            raise IndexError('неверный индекс')
        temp = self.top
        for i in range(index):
            temp = temp.next
        temp.data = obj.data



st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
st[1] = StackObj("new obj2")
print(st[2].data) # obj3
print(st[1].data) # new obj2
# res = st[3] # исключение IndexError