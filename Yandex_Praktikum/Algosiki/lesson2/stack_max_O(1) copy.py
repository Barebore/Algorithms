class StackMax:
    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, x):
        self.stack.append(x)
        if not self.max_stack or x >= self.max_stack[-1]:
            self.max_stack.append(x)

    def pop(self):
        if self.stack[-1] == self.max_stack[-1]:
            self.max_stack.pop()
        self.stack.pop()

    def top(self):
        return self.stack[-1]

    def get_max(self):
        return self.max_stack[-1]

n = int(input())
stack = StackMax()
for i in range(n):
    command = input()
    if command == 'get_max':
        stack.get_max()
    elif command == 'pop':
        stack.pop()
    elif command.split()[0] == 'push':
        stack.push(int(command.split()[1]))
