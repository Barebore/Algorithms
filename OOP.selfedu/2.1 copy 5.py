class Point:
    def __init__(self, *args):
        self.set_coord(*args)

    def set_coord(self, *args):
        self.__x, self.__y = args

    def get_coords(self):
        return self.__x, self.__y

class Rectangle:
    def __init__(self, *args):
        if isinstance(args[0], Point):
            self.set_coords(*args)
        else:
            self.__sp, self.__ep = Point(args[0], args[1]), Point(args[2], args[3])

    def set_coords(self, *args):
        self.__sp, self.__ep = args

    
    def get_coords(self):
        return self.__sp, self.__ep
    
    def draw(self):
        print(f"Прямоугольник с координатами: ({self.__sp}) ({self.__ep})")

    
#r1 = Rectangle(Point(1, 2), Point(3, 4))
#r2 = Rectangle(1, 2, 3, 4)
rect = Rectangle(0,0,20,34)
rect.draw()

r = Rectangle(1, 2.6, 3.3, 4)
r.set_coords(Point(1, 2), Point(3, 4))
sp, ep = r.get_coords()
print(sp, ep)
a, b = sp.get_coords()
# c, d = ep.get_coords()
'''Подвиг 8. Объявите в программе два класса Point и Rectangle. Объекты первого класса должны создаваться командой:
pt = Point(x, y)
где x, y - координаты точки на плоскости (целые или вещественные числа). При этом в объектах класса Point должны формироваться следующие локальные свойства:
__x, __y - координаты точки на плоскости.
и один геттер:
get_coords() - возвращение кортежа текущих координат __x, __y
Объекты второго класса Rectangle (прямоугольник) должны создаваться командами:
r1 = Rectangle(Point(x1, y1), Point(x2, y2))
или
r2 = Rectangle(x1, y1, x2, y2)
Здесь первая координата (x1, y1) - верхний левый угол, а вторая координата (x2, y2) - правый нижний. При этом, в объектах класса Rectangle (вне зависимости от способа их создания) должны формироваться следующие локальные свойства:
__sp - объект класса Point с координатами x1, y1 (верхний левый угол);
__ep - объект класса Point с координатами x2, y2 (нижний правый угол).
Также к классе Rectangle должны быть реализованы следующие методы:
set_coords(self, sp, ep) - изменение текущих координат, где sp, ep - объекты класса Point;
get_coords(self) - возвращение кортежа из объектов класса Point с текущими координатами прямоугольника (ссылки на локальные свойства __sp и __ep);
draw(self) - отображение в консоли сообщения: "Прямоугольник с координатами: (x1, y1) (x2, y2)". Здесь x1, y1, x2, y2 - соответствующие числовые значения координат.
Создайте объект rect класса Rectangle с координатами (0, 0), (20, 34).
P.S. На экран ничего выводить не нужно.'''