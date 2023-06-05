# Подвиг 10 (на повторение). В нейронных сетях использую операцию под названием Max Pooling. Суть ее состоит в сканировании прямоугольной таблицы чисел (матрицы) окном определенного размера (обычно, 2x2 элемента) и выбора наибольшего значения в пределах этого окна:



#  Или, если окна выходят за пределы матрицы, то они пропускаются (игнорируются):



# Мы повторим эту процедуру. Для этого в программе нужно объявить класс с именем MaxPooling, объекты которого создаются командой:

# mp = MaxPooling(step=(2, 2), size=(2,2))
# где step - шаг смещения окна по горизонтали и вертикали; size - размер окна по горизонтали и вертикали.

# Параметры step и size по умолчанию должны принимать кортеж со значениями (2, 2).

# Для выполнения операции Max Pooling используется команда:

# res = mp(matrix)
# где matrix - прямоугольная таблица чисел; res - ссылка на результат обработки таблицы matrix (должна создаваться новая таблица чисел.

# Прямоугольную таблицу чисел следует описывать вложенными списками. Если при сканировании таблицы часть окна выходит за ее пределы, то эти данные отбрасывать (не учитывать все окно).

# Если matrix не является прямоугольной таблицей или содержит хотя бы одно не числовое значение, то должно генерироваться исключение командой:

# raise ValueError("Неверный формат для первого параметра matrix.")
# Пример использования класса (эти строчки в программе писать не нужно):

# mp = MaxPooling(step=(2, 2), size=(2,2))
# res = mp([[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]])    # [[6, 8], [9, 7]]
# Результатом будет таблица чисел:

# 6 8
# 9 7

class MaxPooling:
    def __init__(self, step=(2, 2), size=(2, 2)):
        self.step = step
        self.size = size

    def __call__(self, matrix):
        if not self._is_valid_matrix(matrix):
            raise ValueError("Неверный формат для первого параметра matrix.")

        pooled_matrix = []
        for i in range(0, len(matrix), self.step[0]):
            row = []
            for j in range(0, len(matrix[0]), self.step[1]):
                max_value = self._get_max_value(matrix, i, j)
                if max_value is not None:
                    row.append(max_value)
            if row:
                pooled_matrix.append(row)

        return pooled_matrix

    def _is_valid_matrix(self, matrix):
        if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
            return False
        for row in matrix:
            if not all(isinstance(element, (int, float)) for element in row):
                return False
        return True

    def _get_max_value(self, matrix, i, j):
        values = []
        for x in range(i, min(i+self.size[0], len(matrix))):
            for y in range(j, min(j+self.size[1], len(matrix[0]))):
                values.append(matrix[x][y])
        return max(values) if values else None

mp = MaxPooling(step=(2, 2), size=(2,2))
res = mp([[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]])    # res =  [[6, 8], [9, 7]]
print(res)