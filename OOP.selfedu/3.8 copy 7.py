class TicTacToe:
    def __init__(self):
        self.pole = tuple((tuple((Cell() for i in range(3))) for i in range(3)))
        # print(self.pole)
    
    def clear(self):
        for row in self.pole:
            for cell in row:
                cell.value = 0
                cell.is_fee = True

    def __setitem__(self, key, value):
        if 0 > key[0] > 3 or 0 > key[0] > 3:
            raise IndexError('неверный индекс клетки')
        self.pole[key[0]][key[1]].value = value

    def __getitem__(self, key):
        if isinstance(key, tuple) and isinstance(key[1], slice):
            #возвращаем строку из таблице
            temp = []
            for i in range(3):
                temp.append(self.pole[key[0]][i].value)
            return tuple(temp)
        if isinstance(key, tuple) and isinstance(key[0], slice):
            # возвращаем столбец из таблице
            temp = []
            for row in self.pole:
                temp.append(row[key[1]].value)
            return tuple(temp)
        if 0 > key[0] > 3 or 0 > key[0] > 3:
            raise IndexError('неверный индекс клетки')
        return self.pole[key[0]][key[1]].value

class Cell:
    def __init__(self):
        self.is_free = True
        self.value = 0

    def __getitem__(self, key):
        return self.value
    
    def __setitem__(self, key, value):
        self.value = value

    def __bool__(self):
        return self.is_free

g = TicTacToe()
g.clear()
assert g[0, 0] == 0 and g[2, 2] == 0, "начальные значения всех клеток должны быть равны 0"
g[1, 1] = 1
g[2, 1] = 2
assert g[1, 1] == 1 and g[2, 1] == 2, "неверно отработала операция присваивания новых значений клеткам игрового поля (или, некорректно работает считывание значений)"
try:
    res = g[3, 0]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError при считывании из несуществующей ячейки"
    
try:
    g[3, 0] = 5
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError при записи в несуществующую ячейку"

g.clear()
g[0, 0] = 1
g[1, 0] = 2
g[2, 0] = 3
assert g[0, :] == (1, 0, 0) and g[1, :] == (2, 0, 0) and g[:, 0] == (1, 2, 3), "некорректно отработали срезы после вызова метода clear() и присваивания новых значений"
cell = Cell()
assert cell.value == 0, "начальное значение атрибута value класса Cell должно быть равно 0"
res = cell.is_free
cell.is_free = True
assert bool(cell), "функция bool вернула False для свободной клетки"