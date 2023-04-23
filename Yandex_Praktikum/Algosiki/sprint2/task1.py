# 86232015 
class Deque:
    def __init__(self, n):
        self.queue = [None] * n
        self.max_size = n
        self.head = 0
        self.tail = 0
        self.size = 0
    
    def is_empty(self):
        return self.size == 0

    def push_back(self, value):
        if self.size != self.max_size:
            self.queue[self.tail] = value
            self.tail = (self.tail + 1) % self.max_size
            self.size += 1
        else:
            print('error')

    def push_front(self, value):
        if self.size != self.max_size:
            self.queue[self.head - 1] = value
            self.head = (self.head - 1) % self.max_size
            self.size += 1
        else:
            print('error')
    
    def pop_front(self):
        if self.size == 0:
            print('error')
            return
        print(self.queue[self.head])
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_size
        self.size -= 1

    def pop_back(self):
        if self.size == 0:
            print('error')
            return
        print(self.queue[self.tail - 1])
        self.queue[self.tail - 1] = None
        self.tail = (self.tail - 1) % self.max_size
        self.size -= 1

n = int(input())
k = int(input())
queue = Deque(k)
for i in range(n):
    command = input()
    if command == 'peek':
        queue.peek()
    elif command == 'pop_back':
        queue.pop_back()
    elif command == 'pop_front':
        queue.pop_front()
    elif command.split()[0] == 'push_back':
        queue.push_back(int(command.split()[1]))
    elif command.split()[0] == 'push_front':
        queue.push_front(int(command.split()[1]))
    if command == 'size':
        print(queue.size)