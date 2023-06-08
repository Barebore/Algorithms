from typing import Any


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        if not(self.a < self.b + self.c and self.b < self.a + self.c and self.c < self.a + self.b):
            raise ValueError("с указанными длинами нельзя образовать треугольник")

    def __setattr__(self, __name: str, __value: Any) -> None:
        if __name in ("a", "b", "c"):
            if __value < 0:
                raise ValueError("длины сторон треугольника должны быть положительными числами")
            if '.' in str(__value):
                super().__setattr__(__name, float(__value))
            else:
                super().__setattr__(__name, int(__value))

    def __len__(self):
        return int(self.a + self.b + self.c)
    
    def tr(self):
        p = len(self)/2
        return (p * (p-self.a) * (p-self.b) * (p-self.c))**0.5
    
tr = Triangle(5, 4, 3)
assert tr.a == 5 and tr.b == 4 and tr.c == 3, "дескрипторы вернули неверные значения"
try:
    tr = Triangle(-5, 4, 3)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

try:
    tr = Triangle(10, 1, 1)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"
    
tr = Triangle(5, 4, 3)
assert len(tr) == 12, "функция len вернула неверное значение"
assert 5.9 < tr() < 6.1, "метод __call__ вернул неверное значение"