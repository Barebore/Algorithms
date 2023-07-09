class RadiusVector:
    def __init__(self, *args, **kwargs):
        self.coords = [*args]
    
    def __getitem__(self, key):
        if isinstance(key, slice):
            return tuple(self.coords[key.start:key.stop:key.step])
        return self.coords[key]
    
    def __setitem__(self, index, value):
        self.coords[index] = value


v = RadiusVector(1, 1, 1, 1)
print(v[1]) # 1
v[:] = 1, 2, 3, 4
print(v[2]) # 3
print(v[1:]) # (2, 3, 4)
v[0] = 10.5