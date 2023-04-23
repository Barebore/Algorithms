# 86233158
class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()

st = Stack()
s = list(input().split())
for value in s:
    if value == '+':
        st.push(st.pop() + st.pop())
    elif value == '-':
        temp1 = st.pop()
        temp2 = st.pop()
        st.push(temp2 - temp1)
    elif value == '*':
        st.push(st.pop() * st.pop())
    elif value == '/':
        temp1 = st.pop()
        temp2 = st.pop()
        st.push(temp2 // temp1)
    else:
        st.push(int(value))
print(st.pop())