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

def evaluate_expression(obj, expression):
    commands = {
        '+': lambda: obj.push(obj.pop() + obj.pop()),
        '-': lambda: obj.push(-obj.pop() + obj.pop()),
        '*': lambda: obj.push(obj.pop() * obj.pop()),
        '/': lambda: obj.push(obj.pop() // obj.pop()),
        'n': lambda x: obj.push(int(x)),
    }
    for value in expression:
        if value in commands:
            commands[value]()
        else:
            obj.push(int(value))
    return obj.pop()


if __name__ == "__main__":
    st = Stack()
    input_string = input().split()
    print(evaluate_expression(st, input_string))
