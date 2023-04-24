# 86232015 
class Deque:
    def __init__(self, n):
        self.__queue = [None] * n
        self.__head = 0
        self.__tail = 0
        self.max_size = n
        self.size = 0
    
    def is_empty(self):
        return self.size == 0

    def push_back(self, value):
        if self.size == self.max_size:
            print('error')
            return
        self.__queue[self.__tail] = value
        self.__tail = (self.__tail + 1) % self.max_size
        self.size += 1

    def push_front(self, value):
        if self.size == self.max_size:
            print('error')
            return
        self.__queue[self.__head - 1] = value
        self.__head = (self.__head - 1) % self.max_size
        self.size += 1
    
    def pop_front(self):
        if self.size == 0:
            print('error')
            return
        print(self.__queue[self.__head])
        self.__queue[self.__head] = None
        self.__head = (self.__head + 1) % self.max_size
        self.size -= 1

    def pop_back(self):
        if self.size == 0:
            print('error')
            return
        print(self.__queue[self.__tail - 1])
        self.__queue[self.__tail - 1] = None
        self.__tail = (self.__tail - 1) % self.max_size
        self.size -= 1

if __name__ == "__main__":
    command_count = int(input())
    max_size = int(input())
    queue = Deque(max_size)
    commands = {
        'peek': '''queue.peek()''',
        'pop_back': '''queue.pop_back()''',
        'pop_front': queue.pop_front(),
        'push_back': '''queue.push_back(int(input_command.split()[1]))''',
        'push_front': '''queue.push_front(int(input_command.split()[1]))''',
        'size': '''queue.size()''',
    }
    for i in range(command_count):
        input_command = input()
        exec(commands[input_command.split()[0]])
