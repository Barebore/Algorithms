class MyQueueSized:
    def __init__(self, n):
        self.queue = [None] * n
        self.max_size = n
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, x):
        if self.size != self.max_size:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_size
            self.size += 1
        else:
            print('error')

    def pop(self):
        if self.size == 0:
            print('None')
            return
        print(self.queue[self.head])
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_size
        self.size -= 1

    
    def peek(self):
        if self.size == 0:
            print('None')
            return
        print(self.queue[self.head])

    
n = int(input())
k = int(input())
queue = MyQueueSized(k)
for i in range(n):
    command = input()
    if command == 'peek':
        queue.peek()
    elif command == 'pop':
        queue.pop()
    elif command.split()[0] == 'push':
        queue.push(int(command.split()[1]))
    elif command == 'size':
        print(queue.size)