class Track:
    points = []

    def __init__(self, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y
        

    def add_point(self, x, y, speed):
        self.points.append([x, y, speed])

    def __getitem__(self, item):
        return tuple(self.points[item-1][:2]), self.points[item-1][2]

    def __setitem__(self, key, value):
        if len(self.points) <= key + 1:
            self.points[key-1][2] = value
        else:
            raise IndexError('некорректный индекс')
            # print(len(self.points), key)


tr = Track(10, -5.4)
tr.add_point(20, 0, 100) # первый линейный сегмент: indx = 0
tr.add_point(50, -20, 80) # второй линейный сегмент: indx = 1
tr.add_point(63.45, 1.24, 60.34) # третий линейный сегмент: indx = 2

tr[2] = 60
c, s = tr[2]
print(c, s)

res = tr[3] # IndexError


