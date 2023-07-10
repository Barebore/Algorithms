
from collections import defaultdict
class Cell:
    def __init__(self, value):
        self.value = value

class SparseTable:
    def __init__(self, rows=0, cols=0):
        self.rows = rows
        self.cols = cols
        self.table = defaultdict()

    def update_index(self):
        self.rows = max(key[0] for key in self.table)
        self.cols = max(key[1] for key in self.table)

    def add_data(self, row, col, data):
        self.table[(row, col)] = data
        self.update_index()
        # if self.rows < row:
        #     self.rows = row
        # # if self.cols < col:
        # #     self.cols = col
        # self.rows += row
        # self.cols += col

    def remove_data(self, row, col):
        if row > self.rows or col > self.cols:
            raise IndexError('ячейка с указанными индексами не существует')
        del self.table[(row, col)]
        # counter_row = 0
        # max_row = 0
        # if row == self.rows:
        #     for value in self.table.values():
        #         if value.row == row:
        #             break
        #         else:
        #             counter_row += 1
        #     if counter_row == len(self.table.value()):
        #         for value in self.table.values():
        #             if value.row > max_row:
        #                 max_row = value.row
        #     self.rows = max_row

        # if col == self.cols:
        #     for value in self.table.values():
        #         if value.col == col:
        #             break
        #         else:
        #             counter_col += 1
        #     if counter_col == len(self.table.value()):
        #         for value in self.table.values():
        #             if value.col > max_col:
        #                 max_col = value.col
        #     self.cols = max_col

    def __setitem__(self, key, value):
        if key in self.table:
            self.table[key].value = value
        else:
            self.add_data(key[0], key[1], Cell(value))
        # if self.rows < key[0]:
        #     self.rows = key[0]
        # if self.cols < key[1]:
        #     self.cols = key[1]

    def __getitem__(self, item):
        if item in self.table:
            return self.table[item]
        else:
            raise ValueError('данные по указанным индексам отсутствуют')



st = SparseTable()
st.add_data(2, 5, Cell(25))
st.add_data(1, 1, Cell(11))
print(st.rows, st.cols)
# assert st.rows == 3 and st.cols == 6, "неверные значения атрибутов rows и cols"
# try:
#     v = st[3, 2]
# except ValueError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение ValueError"
# print(st.rows, st.cols)
# st[3, 2] = 100
# print(st[3, 2])
# assert st[3, 2] == 100, "неверно отработал оператор присваивания нового значения в ячейку таблицы"
# print(st.rows, st.cols)
# assert st.rows == 4 and st.cols == 6, "неверные значения атрибутов rows и cols"
# st.remove_data(1, 1)
# try:
#     v = st[1, 1]
# except ValueError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение ValueError"
    
# try:
#     st.remove_data(1, 1)
# except IndexError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение IndexError"
# d = Cell('5')
# assert d.value == '5', "неверное значение атрибута value в объекте класса Cell, возможно, некорректно работает инициализатор класса"
 