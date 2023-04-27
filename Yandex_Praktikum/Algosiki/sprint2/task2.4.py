# 
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

def calc(st, znak):
    commands = {
        '+': lambda: st.pop() + st.pop(),
        '-': lambda: -st.pop() + st.pop(),
        '*': lambda: st.pop() * st.pop(),
        '/': lambda: st.pop() // st.pop(),
    }
    return commands[znak]()

if __name__ == "__main__":
    st = Stack()
    input_string = list(input().split())
    for value in input_string:
        if value in ['+', '-', '*', '/']:
            st.push(calc(st, value))
        else:
            st.push(int(value))
    print(st.pop())