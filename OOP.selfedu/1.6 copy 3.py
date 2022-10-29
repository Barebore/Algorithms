class Point:
    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls)
        setattr(obj, 'x', args[0])
        setattr(obj, 'y', args[1])
        return obj

    def clone(self):
        return Point(self.x, self.y)


pt = Point(1,2)
pt_clone = pt.clone()