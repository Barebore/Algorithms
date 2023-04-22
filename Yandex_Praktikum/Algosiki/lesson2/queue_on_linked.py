class Node:  
    def __init__(self, value, next_item=None):  
        self.value = value  
        self.next_item = next_item

class QueueLinkedList:

    def __init__(self) -> None:
        self.size = 0
        self.head = None
        self.tail = None

    def put(self, x):
        if self.size == 0:
            object = Node(x)
            self.head = object
            self.tail = object
        else:
            self.head.next_item = Node(x)
            self.head = self.head.next_item
        self.size += 1

    def get(self):
        if self.size == 0:
            print('error')
            return
        print(self.tail.value)
        self.tail = self.tail.next_item
        self.size -= 1

n = int(input())
queue = QueueLinkedList()
for i in range(n):
    command = input()
    if command == 'get':
        queue.get()
    elif command.split()[0] == 'put':
        queue.put(int(command.split()[1]))
    elif command == 'size':
        print(queue.size)