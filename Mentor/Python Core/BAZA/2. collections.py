# COLLECTIONS
import collections

'''
namedtuple - тип данных, ведущий себя как кортеж, с тем дополнением, что каждому элементу присваивается имя,
по которому можно получать доступ'''
Point = collections.namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x) #1
print(p.y) #2
print(p) #Point(x=1, y=2)

'''
OrderedDict - словарь, которые помнит порядок, в котором ему были даны ключи
'''
dct = collections.OrderedDict()
dct['a'] = 1
dct['b'] = 2
dct['c'] = 3
dct.popitem(last=False) # удаляет последнии элемент
print(dct)
dct.move_to_end('c', last=False) # меняет порядоковый номер ключа
print(dct)

'''
collectios.defaultdict - подкласс словаря, который обеспечивает значение по умолчанию для ключей, которых ещё нет
в словаре
'''

dct = collections.defaultdict(int)
print(dct['a'])
print(dct)


'''
Counter - подкласс словаря, которые используется для подсчёта числа вхождений элементов в последовательности
'''

my_list = ['apple', 'banana', 'apple', 'banana', 'apple', 'banana', 'apple', 'banana', 'apple', 'banana']
dct = collections.Counter(my_list)
print(dct) # Counter({'banana': 5, 'apple': 5})

'''
collections.deque - двусторочнняя очередь, позволяющая добавлять и удалять элементы с обоих концов
'''

deque = collections.deque()
deque.append(1)
deque.append(2)
deque.append(3)
deque.appendleft(4)

print(deque) # deque([4, 1, 2, 3])
deque.pop() # 3
deque.popleft() # 4