class TableValues:
    def __init__(self, rows, cols, cell=None):
        if cell is None:
            raise ValueError('параметр cell не указан')
        self.rows = rows
        self.cols = cols
        self.cell = cell
        self.cells = []
        for i in range(rows):
            self.cells.append([cell() for i in range(cols)])

    def __getitem__(self, key):
        return self.cells[key[0]][key[1]].value
    
    def __setitem__(self, key, value):
        self.cells[key[0]][key[1]] = self.cell(value)

class IntegerValue:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]
    
    def __set__(self, instance, value):
        if type(value) != int:
            raise ValueError('возможны только целочисленные значения')
        instance.__dict__[self.name] = value

class CellInteger:
    value = IntegerValue()
    
    def __init__(self, start_value=0):
        self.value = start_value

    # def __getitem__(self, key):
    #     print('asdasdas')
    #     return self.value

tb = TableValues(3, 2, cell=CellInteger)
tb[0, 0] = 1
assert tb[0, 0] == 1, "некорректно работает запись и/или считывание значения в ячейку таблицы по индексам"
try:
    tb[2, 1] = 1.5
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"
for row in tb.cells:
    for x in row:
        assert isinstance(x, CellInteger), "коллекция cells должна содержать только объекты класса  CellInteger"
cell = CellInteger(10)
assert cell.value == 10, "дескриптор value вернул неверное значение"