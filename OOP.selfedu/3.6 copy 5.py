class Dimensions:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        if self.a<0 or self.b<0 or self.c<0:
            raise ValueError("габаритные размеры должны быть положительными числами")

    def __hash__(self):
        return hash((self.a, self.b, self.c))
    
    def __setattr__(self, name, value):
        if '.' in str(value):
            super().__setattr__(name, float(value))
        else:
            super().__setattr__(name, int(value))

    

s_inp = input()  # эту строку (переменную s_inp) в программе не менять

lst_dims = []
for string in s_inp.split(';'):
    lst_dims.append(Dimensions(*string.split()))

lst_dims = sorted(lst_dims, key=lambda x: hash(x))


