class StackMax:
    def __init__(self) -> None:
        self.items = []
        self.max_items = []
    
    def push(self, item):
        self.items.append(item)
        if self.max_items == [] or item >= self.max_items[-1]:
            self.max_items.append(item)
    
    def pop(self):
        if self.is_empty():
            print('error')
        else:
            if self.items[-1] == self.max_items[-1]:
                self.max_items.pop()
            self.items.pop()
    
    def is_empty(self):
        return self.items == []
    
    def get_max(self):
        if self.is_empty():
            print(None)
        else:
            print(self.max_items[-1])

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
