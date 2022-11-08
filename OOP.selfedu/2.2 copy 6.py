import math

class  PathLines:
    def __init__(self, *args):
        i = 0
        self.lst = []
        lst_temp = args
        while i < len(lst_temp):
            self.lst.append(lst_temp[i])
            i += 1

    def get_path(self):
        return self.lst

    def get_length(self):
        i = 0
        x0 = 0
        y0 = 0
        dlina = 0
        while i < len(self.lst):
            dlina += math.sqrt((self.lst[i].x - x0) ** 2 + (self.lst[i].y - y0) ** 2)
            x0 =  self.lst[i].x
            y0 = self.lst[i].y
            i += 1
        return dlina

    def add_line(self, line):
        self.lst.append(line)

class LineTo:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y






p = PathLines(LineTo(10, 20), LineTo(10, 30))
p.add_line(LineTo(20, -10))
dist = p.get_length()
print('dist',dist)