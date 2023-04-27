# 86504994
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
    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: y - x,
        '*': lambda x, y: x * y,
        '/': lambda x, y: y // x,
    }
    for value in input_string:
        if value in operations.keys():
            st.push(operations[value](st.pop(), st.pop()))
        else:
            st.push(int(value))
    print(st.pop())