class Vector:
    def __init__(self, *args, **kwargs):
        self.values = list(args)


    def __add__(self, other):
        if len(self.values) != len(other.values):
            raise ArithmeticError('размерности векторов не совпадают')
        temp = []
        for i in range(len(self.values)):
            temp.append(self.values[i] + other.values[i])
        return Vector(*temp)
    
    def __sub__(self, other):
        if len(self.values) != len(other.values):
            raise ArithmeticError('размерности велиторов не совпадают')
        temp = []
        for i in range(len(self.values)):
            temp.append(self.values[i] - other.values[i])
        return Vector(*temp)
    
    def __mul__(self, other):
        if len(self.values) != len(other.values):
            raise ArithmeticError('размерности велиторов не совпадают')
        temp = []
        for i in range(len(self.values)):
            temp.append(self.values[i] * other.values[i])
        return Vector(*temp)

    def __iadd__(self, other):
        if isinstance(other, int):
            for i in range(len(self.values)):
                self.values[i] += other
            return self
        if len(self.values) >= len(other.values):
            for i in range(len(other.values)):
                self.values[i] += other.values[i]
        elif len(self.values) < len(other.values):
            for i in range(len(self.values)):
                self.values[i] += other.values[i]
        return self
        
    def __isub__(self, other):
        if isinstance(other, int):
            for i in range(len(self.values)):
                self.values[i] -= other
            return self
        if len(self.values) >= len(other.values):
            for i in range(len(other.values)):
                self.values[i] -= other.values[i]
        elif len(self.values) < len(other.values):
            for i in range(len(self.values)):
                self.values[i] -= other.values[i]
        
        return self
    

    def __eq__(self, other):
        if len(self.values) != len(other.values):
            return False
        for i in range(len(self.values)):
            if self.values[i] != other.values[i]:
                return False
        return True
    
    def __ne__(self, other):
        return not self == other

v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
print((v1 + v2).values)  # [5, 7, 9]
print((v1 - v2).values)  # [-3, -3, -3]
print((v1 * v2).values)  # [4, 10, 18]

v1 += 10
print(v1.values)  # [11, 12, 13]
v1 -= 10
print(v1.values)  # [1, 2, 3]
v1 += v2
print(v1.values)  # [5, 7, 9]
v2 -= v1
print(v2.values)  # [-1, -2, -3]

print(v1 == v2)  # False
print(v1 != v2)  # True