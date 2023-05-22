class PolyLine:
    def __init__(self, *args):
        self.coords = list(args)

    def add_coord(self, x,y):
        self.coords.append((x,y))

    def remove_coord(self, index):
        del(self.coords[index])

    def get_coords(self):
        return self.coords


poly = PolyLine((1, 2), (3, 5), (0, 10), (-1, 8))

print(poly.get_coords())