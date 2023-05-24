class ListMath:
    def __init__(self, value=[]):
        self.lst_math = [value for value in value if ((isinstance(value, int) or isinstance(value, float))
                                                  and not isinstance(value, bool))]
    
    def get_item(self):
        return self.lst_math
    
    def __add__(self, other):
        return ListMath([value + other for value in self.lst_math])

    def __radd__(self, other):
        return self + other
    
    def __sub__(self, other):
        return ListMath([value - other for value in self.lst_math])
    
    def __rsub__(self, other):
        return ListMath([other - value for value in self.lst_math])
    
    def __mul__(self, other):
        return ListMath([value * other for value in self.lst_math])
    
    def __rmul__(self, other):
        return self * other
    
    def __truediv__(self, other):
        return ListMath([value / other for value in self.lst_math])
    
    def __rtruediv__(self, other):
        return self / other
    
    
    
    # def __iadd__(self, other):
    #     return self + other
    

lst = ListMath([1, "abc", -5, 7.68, True]) # ListMath: [1, -5, 7.68]
print(lst.get_item())
lst = lst + 76
print(lst.get_item())
lst = 6.5 + lst
print(lst.get_item())
lst += 76.7
print(lst.get_item())
lst = lst - 76 # вычитание из каждого числа списка определенного числа
print(lst.get_item())
lst = 7.0 - lst # вычитание из числа каждого числа списка
print(lst.get_item())
lst -= 76.3
print(lst.get_item())
lst = lst * 5 # умножение каждого числа списка на указанное число (в данном случае на 5)
print(lst.get_item())
lst = 5 * lst # умножение каждого числа списка на указанное число (в данном случае на 5)
print(lst.get_item())
lst *= 5.54
print(lst.get_item())
lst = lst / 13 # деление каждого числа списка на указанное число (в данном случае на 13)
print(lst.get_item())