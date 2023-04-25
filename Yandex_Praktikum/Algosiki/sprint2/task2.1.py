# 86233158
class Stack:
    def __init__(self):
        self.__stack = []
    
    def push(self, value):
        self.__stack.append(value)

    def pop(self):
        if self.is_empty():
            return IndexError('Stack is empty')
        return self.__stack.pop()

    def is_empty(self):
        return len(self.__stack) == 0
    
if __name__ == "__main__":
    st = Stack()
    input_string = list(input().split())
    commands = {
        '+': '''st.push(st.pop() + st.pop())''',
        '-': '''temp1 = st.pop(); temp2 = st.pop(); st.push(temp2 - temp1);''',
        '*': '''st.push(st.pop() * st.pop())''',
        '/': '''temp1 = st.pop();temp2 = st.pop();st.push(temp2 // temp1);''',
    }
    for value in input_string:
        if value in commands.keys():
            exec(commands[value])
        else:
            st.push(int(value))
    print(st.pop())