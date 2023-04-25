#86380771
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
    
    def add(self):
        temp1 = self.pop()
        temp2 = self.pop()
        self.push(temp2 + temp1)

    def subtract(self):
        temp1 = self.pop()
        temp2 = self.pop()
        self.push(temp2 - temp1)

    def multiply(self):
        temp1 = self.pop()
        temp2 = self.pop()
        self.push(temp2 * temp1)

    def divide(self):
        temp1 = self.pop()
        temp2 = self.pop()
        self.push(temp2 // temp1)


if __name__ == "__main__":
    st = Stack()
    input_string = list(input().split())
    commands = {
        '+': st.add,
        '-': st.subtract,
        '*': st.multiply,
        '/': st.divide,
    }
    for value in input_string:
        if value in commands.keys():
            commands[value]()
        else:
            st.push(int(value))
    print(st.pop())